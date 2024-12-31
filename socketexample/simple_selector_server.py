import selectors
import socket
import logging
import sys
from collections import deque

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format="%(asctime)s %(name)s %(threadName)s %(levelname)s %(lineno)d %(message)s")
logger = logging.getLogger(__name__)

sel = selectors.DefaultSelector()
logger.info("sel {} {}".format(sel, type(sel)))

send_data_map: dict[any, deque] = dict()


def read(conn, mask):
    data = conn.recv(1000)  # 应当已就绪
    if data:
        if conn not in send_data_map:
            send_data_map[conn] = deque()
        send_data_map[conn].append(data)
    else:
        logger.info("closing {} ,mask {}".format(conn, mask))
        sel.unregister(conn)
        conn.close()


def write(conn, mask):
    logger.info("write {} {}".format(conn, mask))
    if conn in send_data_map:
        q = send_data_map[conn]
        while len(q) > 0:
            data = q.popleft()
            logger.info("echo {} to {} ,mask {}".format(data, conn, mask))
            conn.sendall(data)


def accept(sock, mask):
    conn, addr = sock.accept()  # 应当已就绪
    logger.info("accepted {} from {} mark {}".format(conn, addr, mask))
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ | selectors.EVENT_WRITE, handle)


def handle(conn, mask):
    if mask & selectors.EVENT_READ > 0:
        read(conn, mask)

    if mask & selectors.EVENT_WRITE > 0:
        write(conn, mask)


sock = socket.socket()
sock.bind(('localhost', 10080))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        logger.info("key {} mask {}".format(key, mask))
        callback = key.data
        logger.info("callback {}".format(callback))
        callback(key.fileobj, mask)
