=========================
WechatBot
=========================

.. image:: https://travis-ci.org/chuanwu/WechatBot.svg?branch=master

*WechatBot* is a wechat bot built for geeks.

===================
0. deprecated
===================

微信官方在加强对网页版爬虫的限制。所以我们转变思路，尝试逆向APK，尝试提供功能更为丰富的轮子。但由于一些特殊原因，不便开源，如有需求，可邮件我。

`ItChat <https://github.com/littlecodersh/ItChat>`_ 是一个更为优秀的轮子，没必要再继续画蛇添足。该项目已经废弃，请使用ItChat。
对此带来的不便，请谅解。

=====================
 1. 快速上手
=====================


---------------------
1.1 安装
---------------------

.. code-block:: python
       
       pip install wechatbot
 
---------------------
1.2 用法
---------------------

贴上示例代码， wechatbot/ping.py。

.. code-block:: python

    # -*- coding:utf-8 -*-
    from wechatbot import WechatBot


    class MyBot(WechatBot):
        def text_reply(self, msg):
            if "ping" in msg:
                return 'pong'


写完你的代码之后，可以执行`make develop`，根据提示扫描二维码之后，机器人就跑起来啦。
这时，可以向机器人发送一个ping的消息来看看服务是否正常。

========================
2. 规划
========================

接下来会把Bot做成一个更加基础的服务，只对外暴露两个模块:

- 在接受指令之后发送定制消息 [done]


- 主动向某个用户发送消息 [done]


谢谢阅读！


**Good luck, have fun!**
