# Pibooth Uploader
Hello!
This is the pibooth uploader
(Well, really you could use it for any discord automated message or picture posting to a server channel.)
We are using it with pibooth to automatically upload photobooth pictures to our wedding discord server.

## Prerequisites:
### discord.py
This bot uses discord.py as a wrapper for the discord api
https://pypi.org/project/discord.py/


## Usage
Set your values in settings.py
**settings.py**
```
TOKEN = 'Discord Bot Token Here'
SERVER_NAME = 'Server Name Here'
CHANNEL_NAME = 'Channel Name Here'
PICTURE_DIRECTORY = 'Directory Path Here'
#This is how often the scheduled job will fire to check the picture directory for new pictures to upload
BATCH_INTERVAL_MINUTES = 5
```
Run the pibooth_uploader
```
python pibooth_uploader.py
```