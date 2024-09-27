from fastapi import FastAPI
from infra.message_brokers.base import BaseMessageBroker
from logic.init import init_container


async def start_kafka(app: FastAPI):
    container = init_container()
    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker)
    await message_broker.producer.start()


async def close_kafka(app: FastAPI):
    container = init_container()
    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker)
    await message_broker.producer.stop()