from typing import Optional
from discord import Embed, Member
from discord.ext import commands

class info(commands.Cog, 
           name = "Information", 
           description = "This command returns information about a given user"):

  def __init__(self, client):
    self.client = client

  #Description:
  #  This is an info command to get information of a user.
  #Command Usage:
  #  *info (user)
  @commands.command()
  async def info(self, ctx, target: Optional[Member]):
    
    target = target or ctx.author
    embed = Embed(
      title = "User Information",
      colour = 	0xffb7c5,
    )

    embed.set_thumbnail(url=target.display_avatar)
    
    fields = [
      ("Name", str(target) , True),
      ("ID", target.id, False),
      ("Created", target.created_at.strftime("%m/%d/%Y"), True),
      ("Joined", target.joined_at.strftime("%m/%d/%Y"), True),
      ("Booster", bool(target.premium_since), True)
    ]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)
   
    await ctx.message.delete()
    await ctx.send(embed=embed)

async def setup(client):
  await client.add_cog(info(client))
