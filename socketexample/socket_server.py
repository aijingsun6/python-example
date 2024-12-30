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

    def action(self, data) -> dict:
        action = data.get("action")
        if action == "ping":
            return {"action": "pong"}
        return data

    def handle(self, client: socket.socket):
        while True:
            data = self.recv_data(client=client)
            reply = self.action(data)
            self.send_data(client=client, data=reply)

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.addr, self.port))
        self.sock.listen(self.backlog)
        logger.info("bind {}".format(self.port))
        while True:
            (clientsocket, address) = self.sock.accept()
            logger.info("recv new client {} {}".format(clientsocket, address))
            self.executor.submit(self.handle, clientsocket)


if __name__ == "__main__":
    server = SocketServer(addr="127.0.0.1", port=10080, backlog=10, worker_count=10)
    server.start()
