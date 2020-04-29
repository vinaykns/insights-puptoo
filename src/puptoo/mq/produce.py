from confluent_kafka import Producer

from ..utils import config


def init_producer():
    producer = Producer({"bootstrap.servers": ",".join(config.BOOTSTRAP_SERVERS), "message.max.bytes": int("20000000")})
    return producer
