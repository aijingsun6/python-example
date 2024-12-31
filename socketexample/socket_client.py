import sys
import logging
import socket
import struct
import json
import traceback
import time
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format="%(asctime)s %(name)s %(threadName)s %(levelname)s %(lineno)d %(message)s")
logger = logging.getLogger(__name__)


class SocketClient(object):
    sock: socket.socket
    addr: str
    port: int
    timeout: int

    def __init__(self, addr, port, timeout=None):
        self.addr = addr
        self.port = port
        self.timeout = timeout
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if timeout is not None:
            self.sock.settimeout(timeout)
        self.sock.connect((self.addr, self.port))

    def send_data(self, data: any):
        try:
            if not isinstance(data, bytes):
                data = json.dumps(data).encode("utf-8")
            logger.info("send {}".format(data))
            self.sock.sendall(struct.pack("!i", len(data)) + data)
        except Exception as ex:
            logger.error("{} {} {}".format(ex, type(ex), traceback.format_exc()))

    def recv_data(self) -> dict:
        try:
            client = self.sock
            data = b''
            while len(data) < 4:
                data += client.recv(4 - len(data))
            size = struct.unpack("!i", data)[0]
            data = b''
            while len(data) < size:
                data += client.recv(size - len(data))
            logger.info("recv {}".format(data))
            return json.loads(data.decode("utf-8"))
        except Exception as ex:
            logger.error("{} {} {}".format(ex, type(ex), traceback.format_exc()))

    def stop(self, how):
        self.sock.shutdown(how)
        self.sock.close()


def ok():
    client = SocketClient(addr="127.0.0.1", port=10080)
    client.send_data({"action": "ping"})
    client.recv_data()
    client.send_data({"action": "close"})
    client.recv_data()
    client.stop(socket.SHUT_RDWR)

def send_sleep_recv():
    client = SocketClient(addr="127.0.0.1", port=10080)
    client.send_data({"action": "ping"})
    time.sleep(5)
    client.recv_data()
    time.sleep(5)
    client.stop(socket.SHUT_RDWR)



def send_shutdown():
    client = SocketClient(addr="127.0.0.1", port=10080)
    client.send_data({"action": "ping"})
    client.recv_data()
    client.sock.shutdown(socket.SHUT_RDWR)
    time.sleep(10)

def send_shutdown_send():
    client = SocketClient(addr="127.0.0.1", port=10080)
    client.send_data({"action": "ping"})
    client.recv_data()
    client.sock.shutdown(socket.SHUT_RDWR)
    client.send_data({"action": "ping"})
    client.recv_data()

def close_send():
    client = SocketClient(addr="127.0.0.1", port=10080, timeout=1)
    client.send_data({"action": "close"})
    logger.info("{}".format(client.sock.fileno()))
    client.recv_data()
    client.send_data({"action": "ping"})
    client.recv_data()


def send_timeout_send():
    client = SocketClient(addr="127.0.0.1", port=10080)
    client.send_data({"action": "ping"})
    client.recv_data()
    client.send_data({"action": "timeout", "timeout": 2})
    time.sleep(5)
    client.send_data({"action": "ping"})
    client.recv_data()


def conn_too_much():
    for i in range(20):
        logger.info("start {} client".format(i+1))
        client = SocketClient(addr="127.0.0.1", port=10080)
        client.send_data({"action": "ping"})
        client.recv_data()


if __name__ == "__main__":
    try:
        # ok()
        # send_shutdown()
        # close_send()
        # send_timeout_send()
        # conn_too_much()
        # send_shutdown_send()
        send_sleep_recv()

    except Exception as ex:
        logger.error("{} {} {}".format(ex, type(ex), traceback.format_exc()))
