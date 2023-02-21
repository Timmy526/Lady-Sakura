import discord
from discord.ext import commands
from discord import Embed

class Rolemembers(commands.Cog,
                  name = "Role Members", 
                  description = "This command returns the members in a role group"):

  def __init__(self, client):
    self.client = client

  #Description:
  #  This command is used to check members in a role group
  #Command Usage:
  #  
  @commands.command(aliases=['rm', 'rolemem', 'rmem'])
  @commands.is_owner()
  async def Rolemembers(self, ctx, role: discord.Role):
    embed = Embed(
      title = f"Role Group: {role}",
      colour = 	0xffb7c5, 
    )
    embed.set_footer(text=f"Members Count: {len(role.members)}")


    count = 0
    list = []
    for member in role.members:
      count += 1
      list.append(f'{count}. {member.mention}')
    embed.add_field(
        name = "Members in the Role Group",
        value = ("\n".join(str(m) for m in list))
    )

    await ctx.send(embed=embed)
async def setup(client):
  await client.add_cog(Rolemembers(client))
