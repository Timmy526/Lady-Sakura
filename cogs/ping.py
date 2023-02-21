from discord.ext import commands


class Ping(commands.Cog,
          name = "Ping", 
          description = "This command returns the latency of the bot to Discord API"):

  def __init__(self, client):
    self.client = client

  #Description:
  #  This command is to check the ping of the bot
  #Command Usage:
  #  *ping
  @commands.command()  # You use commands.command() instead of bot.command()
  async def ping(self,
                 ctx):  # you must always have self, if not it will not work.
    await ctx.message.delete()
    await ctx.send('Pong! {0}ms'.format(round(self.client.latency * 1000)))

  # @commands.Cog.listener()  # You use commands.Cog.listener() instead of bot.event
  # async def on_ready(self):
  # print("Pong!")


async def setup(client):
  await client.add_cog(Ping(client))
