import discord
from discord.ext import commands
from random import shuffle

class ThanosCommandsCog:
    def __init__(self, bot):
        self.bot = bot
        self.silenced_ids = []

    @commands.command(name='snap-silence')
    async def snap_silence(self, ctx):
        all_member_ids = []
        thanos_silence = discord.utils.get(ctx.channel.guild.roles, name='SILENCED by Thanos')
        
        tmp = await ctx.channel.send('Infinity gauntlet processing snap...')
        for member in ctx.guild.members:
            if not member.bot:
                all_member_ids.append(member.id)
        shuffle(all_member_ids)
        await tmp.delete()
        
        e = discord.Embed(title='When I am done, half of the server will still speak. Perfectly balanced, as all things should be.')
        e.set_image(url='https://media1.tenor.com/images/61823d70493db1620a4e7b57e41d39b0/tenor.gif?itemid=12393235')
        await ctx.channel.send(embed = e)

        for ID in all_member_ids[len(all_member_ids) // 2:]:
            await ctx.channel.guild.get_member(ID).add_roles(thanos_silence)
        self.silenced_ids = all_member_ids[len(all_member_ids) // 2:]

    @commands.command(name='snap-undo')
    async def snap_undo(self, ctx):
        thanos_silence = discord.utils.get(ctx.channel.guild.roles, name='SILENCED by Thanos')

        e = discord.Embed(title='I require you to speak, mortals.')
        e.set_image(url='https://media1.tenor.com/images/3144f534f7ad91a8e162f9fa23caba15/tenor.gif?itemid=12255966')
        await ctx.channel.send(embed = e)
        
        for ID in self.silenced_ids:
            await ctx.channel.guild.get_member(ID).remove_roles(thanos_silence)

    async def on_message(self, message):
        if message.author.bot:
            return
        if ' '.join(str(message.channel).split()[:2]) == 'Direct Message':
            e = discord.Embed(title='Chattering animal, you do not have the privilege to address the Great Titan.')
            e.set_image(url='https://media.melty.fr/article-3722110-raw/media.gif')
            await message.channel.send(embed = e)

def setup(bot):
    bot.add_cog(ThanosCommandsCog(bot))
