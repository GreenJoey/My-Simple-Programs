import asyncio
import logging
import random
import string
import uuid
import attr


@attr.s
class PubSubMessage:
    instance_name = attr.ib()
    message_id = attr.ib(repr=False)
    hostname = attr.ib(repr=False, init=False)

    def __attrs_post_init__(self):
        self.hostname = f"{self.instance_name}.debian.local"


# simulating an external publisher of events
async def publish(queue):
    choices = string.ascii_lowercase + string.digits

    while True:
        msg_id = str(uuid.uuid4())
        host_id = ''.join(random.choices(choices, k=4))
        instance_name = f"cattle-{host_id}"
        msg = PubSubMessage(message_id=msg_id, instance_name=instance_name)
        # Using asyncio.create_task instead await for actually concurrency
        asyncio.create_task(queue.put(msg))
        logging.info(f"Published {msg} messages")

        await asyncio.sleep(random.random())


    await queue.put(None)  # Done publishing


async def consume(queue):
    while True:
        # wait for an item from the publisher
        msg = await queue.get()
        if msg is None:  # publisher is done
            break

        # process and log message
        logging.info(f"Consumed {msg}")
        await asyncio.sleep(random.random())

        
if __name__ == '__main__':
    logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s: %(message)s",
            datefmt="%H:%M:%S"
    )

    queue = asyncio.Queue()
    # This code for >= 3.7. Earlier versions need manual setup and teardown of event loop
    # asyncio.run(publish(queue, 5))
    # asyncio.run(consume(queue))
    # But for this tutorial we are sticking with the < 3.7 boilerplate, since this is a good habit for clean-up in a service that runs continually.
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(publish(queue))
        loop.create_task(consume(queue))
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Shutting down as requested....")
    finally:
        loop.close()
        logging.info("Shutdown the Mayhem service...")

