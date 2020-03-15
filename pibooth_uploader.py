import settings
import sys
import schedule
import time
from datetime import datetime as dt
import os
import subprocess
import logging

class PiBoothUploader():

    def __init__(self):
        self._count = 0
        now = dt.now().strftime("%Y%m%d%H%M")
        today = dt.now().strftime("%Y%m%d")
        logging.basicConfig(filename="pibooth_uploader." + today + ".log",level=logging.INFO)
        logging.info("[" + now + "] Pibooth uploader started." )

    def run(self):
        #self._job()                       
        schedule.every(settings.BATCH_INTERVAL_MINUTES).minutes.do(self._job)

        while True:
            schedule.run_pending()
            time.sleep(300)

    def _job(self):
        self._count += 1
        now = dt.now().strftime("%Y%m%d%H%M")
        for picture in [p for p in os.listdir(settings.PICTURE_DIRECTORY) if ".jpg" in p]:
            try:
                logging.info("[" + now + "] Found some pictures to upload! Uploading . . .")
                retcode = subprocess.call("python request_pibooth_bot_upload.py" + ' ' + picture, shell=True)
                if retcode < 0:
                    print("Child was terminated by signal", -retcode, file=sys.stderr)
                    logging.warning("[" + now + "] Child was terminated by signal. Return Code: " + retcode )
                else:
                    print("Child returned", retcode, file=sys.stderr)
            except OSError as e:
                print("Execution failed:", e, file=sys.stderr)
                logging.exception("[" + now + "] Execution failed.")

    
piBoothUploader = PiBoothUploader()
piBoothUploader.run()