from collections import defaultdict

import xmltodict
from loguru import logger
from queue import SimpleQueue, Empty
from flask import Flask, jsonify, request

application = Flask(__name__)

account_task_queue = defaultdict(lambda: SimpleQueue())

def handle_msg(msg):
    '''
    接受好友消息，并返回`pong`
    '''
    logger.info(f'receive {msg}')
    return 'pong'

def to_list(row):
    if row is None:
        return
    if isinstance(row, (list, tuple)):
        return row
    return [row, ]

@application.route('/push_msg', methods=['POST'])
def message():
    data = request.json or {}
    account = data.get('account')
    if not account:
        return jsonify(code=400, message="缺少用户")
    logger.info(f"message data: {request.json}")

    msg_source = xmltodict.parse(data['msgSource'])['msgsource'] or {}
    msg = {
        'account': data['account'],
        'msg_type': data['msgType'],
        'from_user_name': data['fromUserName'],
        'to_user_name': data['toUserName'],
        'create_time': data['createTime'],
        'message': {
            'text': data['content'],
            'at_user_list': to_list(msg_source.get('atuserlist'))
        }
    }
    content = data['content']
    reply = handle_msg(content)

    if reply:
        job = {
            "username": data['fromUserName'],
            "content": reply
        }
        account_task_queue[account].put(job)
    return jsonify(code=200, message="success")


@application.route('/pull_task', methods=['POST'])
def pull_task():
    account = request.args.get('account')
    if not account:
        return jsonify(code=400, message="缺少用户")
    queue = account_task_queue[account]
    try:
        task = queue.get_nowait()
        return jsonify(code=200, message="success", data=task)
    except Empty:
        pass
    return jsonify(code=100, message="success", data=None)


@application.route('/add_task', methods=['POST'])
def add_task():
    account = request.json['account']
    data = request.json['data']
    #     data = {
    #         "username": "1234",
    #         "type": 1,
    #         "content": "hello",
    #         "at_list": []
    #     }
    queue = account_task_queue[account]
    queue.put(data)
    return jsonify(code=200, message="success")


if __name__ == '__main__':
    application.run(host='0.0.0.0')

