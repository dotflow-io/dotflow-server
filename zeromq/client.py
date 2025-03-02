"""Example using zmq with asyncio coroutines"""

# Copyright (c) PyZMQ Developers.
# This example is in the public domain (CC-0)

# import asyncio

import zmq
from zmq import Context

url = 'tcp://127.0.0.1:5555'

ctx = Context.instance()


def sender() -> None:
    """send a message every second"""
    push = ctx.socket(zmq.PUSH)
    push.connect(url)
    print("sending")
    push.send(b"Hello")


def main() -> None:
    sender()


if __name__ == "__main__":
    main()
