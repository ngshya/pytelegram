import logging
from logging.config import fileConfig
from pytlg import tlgHandler, pytlg


fileConfig('logging_config.ini')
tmp = tlgHandler()
tmp.setLevel(logging.getLogger().level)
logging.getLogger().addHandler(tmp)


logging.info("INFO TEST MESSAGE")
logging.debug("DEBUG TEST MESSAGE")
