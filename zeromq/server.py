"""Example using zmq with asyncio coroutines"""

# Copyright (c) PyZMQ Developers.
# This example is in the public domain (CC-0)

import asyncio

import zmq
from zmq.asyncio import Context, Poller

url = 'tcp://127.0.0.1:5555'

ctx = Context.instance()


async def receiver() -> None:
    """receive messages with polling"""
    pull = ctx.socket(zmq.PULL)
    pull.connect(url)
    poller = Poller()
    poller.register(pull, zmq.POLLIN)
    while True:
        events = await poller.poll()
        if pull in dict(events):
            print("recving", events)
            msg = await pull.recv_multipart()
            print('recvd', msg)


async def main() -> None:
    await asyncio.wait([asyncio.create_task(receiver())])


if __name__ == "__main__":
    asyncio.run(main())
