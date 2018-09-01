import discord
import asyncio
import secret
from random import shuffle

#I'll make the config file for ID values and such some day...
class MyClient(discord.Client):
    async def on_ready(self):
        print('Starting Thanos setup')

        print('Defining variables')
        self.silenced_ids = []

        #This will eventually be controlled by config
        print('Dev tool: clearing past messages')
        bot_channel = client.get_channel(485156296950153216)
        async for msg in bot_channel.history(limit=100): #development tool
            await msg.delete()
        print('Dev tool: past messages cleared')

        print('Checking if SILENCED by Thanos role exists')
        thanos_silence = discord.utils.get(bot_channel.guild.roles, name='SILENCED by Thanos')
        if thanos_silence == None:
            print('SILENCED by Thanos role not found, creating')
            thanos_silence = await bot_channel.guild.create_role(name='SILENCED by Thanos', hoist=True, colour=discord.Colour(0x7f8c8d))
            await bot_channel.category.set_permissions(thanos_silence, send_messages=False)
        print('SILENCED by Thanos role functional')

        print('Checking if Thanos_Color role exists')
        thanos_color = discord.utils.get(bot_channel.guild.roles, name='Thanos_Color')
        if thanos_color == None:
            print('Thanos_Color role not found, creating')
            thanos_color = await bot_channel.guild.create_role(name='Thanos_Color', colour=discord.Colour(0xe74c3c))
        await bot_channel.guild.get_member(483411950009712650).add_roles(thanos_color)
        print('Thanos_Color role functional')

        print('Showing intro image')
        e = discord.Embed(title='Dread it. Run from it. Destiny still arrives. Or should I say, I have.')
        e.set_image(url='https://media.giphy.com/media/3oxHQG3DcmkbYYob2o/giphy-downsized.gif')
        await bot_channel.send(embed = e)

        print('Thanos setup finished')
        print(self.user.name + ' bot running...')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if ' '.join(str(message.channel).split()[:2]) == 'Direct Message':
            e = discord.Embed(title='Chattering animal, you do not have the privilege to address the Great Titan.')
            e.set_image(url='https://media.melty.fr/article-3722110-raw/media.gif')
            await message.channel.send(embed = e)
        else:
            if message.content.startswith('!snap SILENCE'):
                all_member_ids = []
                thanos_silence = discord.utils.get(message.channel.guild.roles, name='SILENCED by Thanos')
                
                tmp = await message.channel.send('Infinity gauntlet processing snap...')
                for member in message.guild.members:
                    if not member.bot:
                        all_member_ids.append(member.id)
                shuffle(all_member_ids)
                await tmp.delete()
                
                e = discord.Embed(title='When I am done, half of the server will still speak. Perfectly balanced, as all things should be.')
                e.set_image(url='https://media1.tenor.com/images/61823d70493db1620a4e7b57e41d39b0/tenor.gif?itemid=12393235')
                await message.channel.send(embed = e)

                for ID in all_member_ids[len(all_member_ids) // 2:]:
                    await message.channel.guild.get_member(ID).add_roles(thanos_silence)
                self.silenced_ids = all_member_ids[len(all_member_ids) // 2:]
            elif message.content.startswith('!snap UNDO'):
                thanos_silence = discord.utils.get(message.channel.guild.roles, name='SILENCED by Thanos')

                e = discord.Embed(title='I require you to speak, mortals.')
                e.set_image(url='https://media1.tenor.com/images/3144f534f7ad91a8e162f9fa23caba15/tenor.gif?itemid=12255966')
                await message.channel.send(embed = e)
                
                for ID in self.silenced_ids:
                    await message.channel.guild.get_member(ID).remove_roles(thanos_silence)
            elif message.content.startswith('!sleep'):
                with message.channel.typing():
                    await asyncio.sleep(5.0)
                    await message.channel.send('Done sleeping.')

client = MyClient()
client.run(secret.TOKEN)
