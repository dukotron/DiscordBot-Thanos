import discord
import asyncio
import secret
from random import shuffle

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

        bot_channel = client.get_channel(485156296950153216)
        print(bot_channel.category)
        async for msg in bot_channel.history(limit=100):
            await msg.delete()

        thanos_silence = discord.utils.get(bot_channel.guild.roles, name='SILENCED by Thanos')
        if thanos_silence == None:
            thanos_silence = await bot_channel.guild.create_role(name='SILENCED by Thanos', hoist=True, colour=discord.Colour(0x7f8c8d))
            await bot_channel.category.set_permissions(thanos_silence, send_messages=False)

        thanos_color = discord.utils.get(bot_channel.guild.roles, name='Thanos_Color')
        if thanos_color == None:
            thanos_color = await bot_channel.guild.create_role(name='Thanos_Color', colour=discord.Colour(0xe74c3c))
        await bot_channel.guild.get_member(483411950009712650).add_roles(thanos_color)
        
        e = discord.Embed(title='Dread it. Run from it. Destiny still arrives. Or should I say, I have.')
        e.set_image(url='https://media.giphy.com/media/3oxHQG3DcmkbYYob2o/giphy-downsized.gif')
        await bot_channel.send(embed = e)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('!snap SILENCE'):
            all_member_ids = []
            bot_channel = client.get_channel(485156296950153216)
            thanos_silence = discord.utils.get(bot_channel.guild.roles, name='SILENCED by Thanos')
            
            all_members = message.guild.members
            tmp = await message.channel.send('Infinity gauntlet processing snap...')
            for member in all_members:
                if not member.bot:
                    all_member_ids.append(member.id)
            print(all_member_ids)
            shuffle(all_member_ids)
            print(all_member_ids)
            
            await tmp.delete()
            e = discord.Embed(title='When I am done, half of the server will still speak. Perfectly balanced, as all things should be.')
            e.set_image(url='https://media1.tenor.com/images/61823d70493db1620a4e7b57e41d39b0/tenor.gif?itemid=12393235')
            await bot_channel.send(embed = e)

            for ID in all_member_ids[len(all_member_ids) // 2:]:
                await bot_channel.guild.get_member(ID).add_roles(thanos_silence)
        elif message.content.startswith('!sleep'):
            with message.channel.typing():
                await asyncio.sleep(5.0)
                await message.channel.send('Done sleeping.')

client = MyClient()
client.run(secret.TOKEN)
