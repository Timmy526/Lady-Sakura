import discord
from discord import app_commands
from discord.ext import commands


class say(commands.Cog,
          name = "Top Secret", 
          description = "Top Secret Command"):
    def __init__(self, client):
        self.client = client

    #Description:
    #  This command is to make the bot talk in a channel
    #Command Usage:
    #  /say (message) optional(channel)
    @app_commands.command(name="say", description="Send a message as the bot in a channel")
    @commands.is_owner()
    async def say(self, interaction: discord.Interaction, message: str,   channel: discord.TextChannel = None):
        if channel is None:
            channel = interaction.channel
        await channel.send(message.replace('\\n', '\n').replace('\\t', '\t'))
        await interaction.response.send_message('Message sent!', ephemeral=True)

    #Description:
    #  This command is used to make the bot reply to a message id in gen chat
    #Command Usage:
    #  *reply (messageId)
    @commands.command()
    @commands.is_owner()
    async def reply(self, ctx, messageId: int, *, msg: str):
        await ctx.message.delete()
        c = ctx.guild.get_channel(1058274500556357732)
        m = await c.fetch_message(messageId)
        await m.reply(msg)

async def setup(client):
    await client.add_cog(say(client))