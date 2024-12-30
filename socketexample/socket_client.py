import sys
import logging
import socket
import struct
import json
import time
import traceback
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format="%(asctime)s %(name)s %(threadName)s %(levelname)s %(lineno)d %(message)s")
logger = logging.getLogger(__name__)


class SocketClient(object):
    sock: socket.socket
    addr: str
    port: int

    def __init__(self, addr, port):
        self.addr = addr
        self.port = port

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

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.addr, self.port))

    def stop(self, how):
        self.sock.shutdown(how)
        self.sock.close()


if __name__ == "__main__":
    client = SocketClient(addr="127.0.0.1", port=10080)
    client.start()
    client.send_data({"action": "ping"})
    client.stop(socket.SHUT_RD)
    client.recv_data()
