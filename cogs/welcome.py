from discord import Embed
from discord.ext import commands
from datetime import datetime

class welcome(commands.Cog, 
           name = "Welcome", 
           description = "This is for the welcome"):

  def __init__(self, client):
    self.client = client

  #Description:
  #  This is the welcome embed
  #Command Usage:
  #  N/A
  @commands.Cog.listener()
  async def on_member_join(self, member):
    if member.bot:
        return
    welc = member.guild.get_channel(1058274196423184474)
    embed = Embed(
      title = f"Welcome {member} to Sakura Sanctuary!",
      colour = 	0xffb7c5,
      description = "I hope you enjoy your stay!\n Please read <#1058274286575571014>\n Grab some <#1058274342682771466>\n Introduce yourself in <#1058274427529334804>"
    )
    embed.set_thumbnail(url=member.display_avatar)
    embed.set_image(url="https://media0.giphy.com/media/NKicvKt6iisXS/giphy.gif?cid=ecf05e477wjyfhss2829re983x9vmay0apw0cohllk3x6pwd&rid=giphy.gif&ct=g")
    embed.set_footer(text=f"You are member #{len(member.guild.members)}!")
    embed.timestamp = datetime.utcnow()
    await welc.send(content=f'Welcome {member.mention}', embed=embed)

async def setup(client):
  await client.add_cog(welcome(client))