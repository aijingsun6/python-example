import logging
import time

logger = logging.getLogger(__name__)

def useful():
    # 一条从库中记录的代表性事件
    logger.debug('Hello from webapplib!')
    # 休眠一下以便其他线程能够运行
    time.sleep(0.01)