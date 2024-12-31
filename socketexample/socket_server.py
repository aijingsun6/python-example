import dataclasses
import sys
import logging
import socket
import struct
import json
import traceback

from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format="%(asctime)s %(name)s %(threadName)s %(levelname)s %(lineno)d %(message)s")
logger = logging.getLogger(__name__)


class SocketServer(object):
    sock: socket.socket
    addr: str
    port: int
    backlog: int
    worker_count: int
    executor: ThreadPoolExecutor

    def __init__(self, addr, port, backlog, worker_count):
        self.addr = addr
        self.port = port
        self.backlog = backlog
        self.worker_count = worker_count
        self.executor = ThreadPoolExecutor(max_workers=self.worker_count,
                                           thread_name_prefix="server-worker-")

    def send_data(self, client: socket.socket, data: any):
        try:
            if not isinstance(data, bytes):
                data = json.dumps(data).encode("utf-8")
            logger.info("send {}".format(data))
            client.sendall(struct.pack("!i", len(data)) + data)
        except Exception as ex:
            logger.error("{} {} {}".format(ex, type(ex), traceback.format_exc()))

    def recv_data(self, client: socket.socket) -> dict:
        try:
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

    def action(self, data: dict, client: socket.socket) -> bool:
        action = data.get("action")
        loop = True
        if action == "ping":
            self.send_data(client=client, data={"action": "pong"})
        elif action == "close":
            logger.info("close {}".format(client))
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            loop = False
        elif action == "shutdown":
            how = data.get("how", socket.SHUT_RDWR)
            logger.info("shutdown {} {}".format(client, how))
            client.shutdown(how)
        elif action == "timeout":
            timeout = data.get("timeout", None)
            logger.info("timeout {} {}".format(client, timeout))
            client.settimeout(timeout)
        else:
            self.send_data(client=client, data=data)
        return loop

    def handle(self, client: socket.socket):
        logger.info("handle {} start".format(client))
        loop = True
        while loop and client.fileno() > 0:
            data = self.recv_data(client=client)
            loop = self.action(data=data, client=client)
        logger.info("handle {} end".format(client))

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.addr, self.port))
        self.sock.listen(self.backlog)
        logger.info("bind {}".format(self.port))
        idx = 1
        while True:
            (client, address) = self.sock.accept()
            logger.info("recv new client {} {} {}".format(idx, client, address))
            idx += 1
            self.executor.submit(self.handle, client)


if __name__ == "__main__":
    server = SocketServer(addr="127.0.0.1", port=10080, backlog=10, worker_count=10)
    server.start()
