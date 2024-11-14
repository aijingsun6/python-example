import sys
import logging
logging.basicConfig(stream=sys.stdout,level=logging.INFO,format="%(asctime)s %(name)s %(threadName)s %(taskName)s %(levelname)s %(funcName)s %(message)s")
LOGGER = logging.getLogger(__name__)