import sys
import os
import settings
from datetime import datetime as dt
import logging
from pibooth_bot import PiBoothBot

try:
    ( 
        PiBoothBot([{'upload': settings.PICTURE_DIRECTORY + "\\" + sys.argv[1]}],
                    lambda: os.rename(settings.PICTURE_DIRECTORY + "\\" + sys.argv[1], settings.PICTURE_DIRECTORY + "\\uploaded\\" + sys.argv[1]))
    )
except:
    today = dt.now().strftime("%Y%m%d")
    logging.basicConfig(filename="pibooth_uploader." + today + ".log",level=logging.INFO)
    logging.exception("There was an error uploading file: " + settings.PICTURE_DIRECTORY + "\\" + sys.argv[1])