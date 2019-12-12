# from . import logger
import logging

handler = logging.FileHandler("logfile")
formatter = logging.Formatter("%(asctime)s <%(levelname)s>: %(message)s")
handler.setFormatter(formatter)

logger = logging.getLogger("root")
logger.setLevel(logging.DEBUG)

logger.addHandler(handler)

a = 2 
b = 3
logger.debug("Stiamo per summare {} e {}".format(a, b))
res = 2 + 3
logger.info("Risultato: {}".format(res))
c = 0
logger.debug("Stiamo per dividire {} e {}".format(a, c))

try:
    res = a / c
except Exception:
    logger.error("Non puoi dividere per 0")