import sys
import os
import settings
from datetime import datetime as dt
import logging
from pibooth_bot import PiBoothBot

try:
    foldercharacter = "\\"
    if settings.OS == "linux":
        foldercharacter = "/"
    ( 
        
        PiBoothBot([{'upload': settings.PICTURE_DIRECTORY + foldercharacter + sys.argv[1]}],
                    lambda: os.rename(settings.PICTURE_DIRECTORY + foldercharacter + sys.argv[1], settings.PICTURE_DIRECTORY + foldercharacter + "uploaded" + foldercharacter + sys.argv[1]))
    )
except:
    today = dt.now().strftime("%Y%m%d")
    logging.basicConfig(filename=settings.LOGGING_DIRETORY + foldercharacter + "pibooth_uploader." + today + ".log",level=logging.INFO)
    logging.exception("There was an error uploading file: " + settings.PICTURE_DIRECTORY + foldercharacter + sys.argv[1])