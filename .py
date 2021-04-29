from discord.ext.commands import Bot
from dotenv import load_dotenv
load_dotenv()
import os
BOT_TOKEN= os.getenv('BOT_TOKEN')
client = Bot('mg.')

if __name__ == '__main__':
    extensions = ['cmd', 'info', 'fun']
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f'Loaded Cog {extension} successfully')
        except Exception as error:
            print(f'Failed to load Cog {extension}. Reason: {error}')
    print('Bot ready')

    
client.run(BOT_TOKEN)
