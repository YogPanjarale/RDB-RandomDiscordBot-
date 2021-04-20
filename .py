from discord.ext.commands import Bot
client = Bot('!')
client.load_extension('cmd','info','fun')

if __name__ == '__main__':
    extensions = ['cmd', 'info', 'fun']
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f'Loaded Cog {extension} successfully')
        except Exception as error:
            print(f'Failed to load Cog {extension}. Reason: {error}')
    print('Bot ready')


print('Bot Ready')
client.run('Nzg2MDY1MzM0Mjg0NTgyOTIy.X9A-ZA.gATX7E4OjH93tlq-Ph5Ye4-WYIU')
