import settings
import discord

#Example:
#   bot = PiBoothBot([{'say': 'Yo'},
#                     {'upload':'test-bw.jpg'},
#                     {'say': 'Whats Up?'},
#                     {'upload':'test.jpg'}])
class PiBoothBot():

    def __init__(self, actions, success=None):
        #Create discord.py client
        self._client = discord.Client()
        
        #Wire up Event to process all bot actions when client is ready
        @self._client.event
        async def on_ready():        
            print('We have logged in as {0.user}'.format(self._client)) 
            # Set Channel
            self._channel = discord.utils.get(self._client.get_all_channels(), guild__name=settings.SERVER_NAME, name=settings.CHANNEL_NAME)
            # Process Bot Actions
            for actionSet in actions:
                for action, data in actionSet.items():
                    print('Action: {0}, Data: {1}'.format(action, data))
                    response = await self._process(action, data)
                    if success != None:
                        success()
            # Logout
            await self._logout()
        self._client.run(settings.TOKEN)

    async def _process(self, action, data):
        method = getattr(self, '_' + action)
        return await method(data)

    async def _upload(self, filename):
            fp = open(filename,'rb')
            discordFile=discord.File(fp, filename=filename)
            result = await self._channel.send(file=discordFile)
            fp.close()  
            return result
    
    async def _say(self, message):
        return await self._channel.send(message)
    
    async def _logout(self):
        await self._client.logout()
        print('{0.user} has been logged out'.format(self._client))
        


