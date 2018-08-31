import discord
import asyncio
import secret

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        channel = client.get_channel(483548026535936012)
        e = discord.Embed(title='I have arrived...')
        e.set_image(url='https://media.giphy.com/media/3oxHQG3DcmkbYYob2o/giphy-downsized.gif')
        await channel.send(embed = e)


    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('!test'):
            counter = 0
            tmp = await message.channel.send('Calculating messages...')
            async for msg in message.channel.history(limit=100):
                if msg.author == message.author:
                    counter += 1

            await tmp.edit(content='You have {} messages.'.format(counter))
        elif message.content.startswith('!sleep'):
            with message.channel.typing():
                await asyncio.sleep(5.0)
                await message.channel.send('Done sleeping.')

client = MyClient()
client.run(secret.TOKEN)
