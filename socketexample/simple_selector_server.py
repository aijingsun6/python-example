import selectors
import socket
import logging
import sys

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format="%(asctime)s %(name)s %(threadName)s %(levelname)s %(lineno)d %(message)s")
logger = logging.getLogger(__name__)

accept_selector = selectors.DefaultSelector()

logger.info("accept_selector {}".format(accept_selector))

read_selector = selectors.DefaultSelector()

logger.info("read_selector {}".format(read_selector))


def read(conn, mask):
    data = conn.recv(1000)  # 应当已就绪
    if data:
        logger.info("send {} ,to {}".format(data, conn))
        conn.sendall(data)
    else:
        logger.info("closing {} ,mask {}".format(conn, mask))
        read_selector.unregister(conn)
        conn.close()


def accept(sock, mask):
    conn, addr = sock.accept()  # 应当已就绪
    logger.info("accepted {} from {} mark {}".format(conn, addr, mask))
    conn.setblocking(False)
    read_selector.register(conn, selectors.EVENT_READ, read)


sock = socket.socket()
sock.bind(('localhost', 10080))
sock.listen(100)
sock.setblocking(False)
accept_selector.register(sock, selectors.EVENT_READ, accept)
logger.info("server sock {}".format(sock))

while True:
    events = accept_selector.select(timeout=1)
    if len(read_selector.get_map()) > 0:
        ee = events_read = read_selector.select(timeout=1)
        events += ee

    for key, mask in events:
        # logger.info("key {} mask {}".format(key, mask))
        callback = key.data
        # logger.info("callback {}".format(callback))
        callback(key.fileobj, mask)
