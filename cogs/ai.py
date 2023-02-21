import asyncio
from discord.ext import commands


class ai(commands.Cog,
          name = "AI", 
          description = "This is an AI Description Command"):

  def __init__(self, client):
    self.client = client
  
  #Description: 
  #  Command to tell people what this bot is created by (Troll)
  #Command Usage:
  #  *ai or /ai
  @commands.hybrid_command(with_app_command=True, description = "This command is used for creating suggestions.")
  async def ai(self, ctx):
    m = await ctx.channel.send(f'{self.client.loading} Getting a fun fact...')
    await asyncio.sleep(3)
    await m.edit(content=f'Fun Fact: I have been trained using AI technology. My developer (Timotree#0001) trained me with 1.3 billion reddit comments and 5000 movie script lines. This means I can talk with the chat but I only have a small chance (5%) to talk per hour.')

async def setup(client):
  await client.add_cog(ai(client))
