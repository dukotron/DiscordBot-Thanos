import discord
from discord.ext import commands
import sys, traceback
import secret

initial_extensions = ['cogs.thanos_commands']
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), activity=discord.Activity(name="the sun rise on a grateful universe", type=3))

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f'\nLogged in as: {bot.user.name}\nVersion: {discord.__version__}\n')

    #This will eventually be controlled by config
    print('Dev tool: clearing past messages')
    bot_channel = bot.get_channel(485156296950153216)
    async for msg in bot_channel.history(limit=100): #development tool
        await msg.delete()
    print('Dev tool: past messages cleared')

    print('Checking if Thanos_Color role exists')
    thanos_color = discord.utils.get(bot_channel.guild.roles, name='Thanos_Color')
    if thanos_color == None:
        print('Thanos_Color role not found, creating')
        thanos_color = await bot_channel.guild.create_role(name='Thanos_Color', colour=discord.Colour(0xe74c3c))
    await bot_channel.guild.get_member(483411950009712650).add_roles(thanos_color)
    print('Thanos_Color role functional')

    print('Checking if SILENCED by Thanos role exists')
    thanos_silence = discord.utils.get(bot_channel.guild.roles, name='SILENCED by Thanos')
    if thanos_silence == None:
        print('SILENCED by Thanos role not found, creating')
        thanos_silence = await bot_channel.guild.create_role(name='SILENCED by Thanos', hoist=True, colour=discord.Colour(0x7f8c8d))
        await bot_channel.category.set_permissions(thanos_silence, send_messages=False)
    print('SILENCED by Thanos role functional')

    print('Showing intro image')
    e = discord.Embed(title='Dread it. Run from it. Destiny still arrives. Or should I say, I have.')
    e.set_image(url='https://media.giphy.com/media/3oxHQG3DcmkbYYob2o/giphy-downsized.gif')
    await bot_channel.send(embed = e)
        
bot.run(secret.TOKEN, bot=True, reconnect=True)
