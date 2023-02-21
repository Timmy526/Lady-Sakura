from discord import Embed
from discord.ext import commands


class botinfo(commands.Cog, 
              name = "Bot Information", 
              description = "This command returns information about Sakura Bot"):

  def __init__(self, client):
    self.client = client
  #Description: 
  #  Gives information regarding the Bot
  #Command Usage:
  #  *botinfo
  @commands.command()
  async def botinfo(self, ctx):
    embed = Embed(
      title="Bot Information",
      colour=0xffb7c5,
    )

    embed.set_thumbnail(url=self.client.user.avatar.url)

    fields = [("Name", self.client.user, True), 
              ("ID", self.client.user.id, False),
              ("Created by", "Timotree#0001", True),
              ("Guilds In", len(self.client.guilds), True),
              ("Created", self.client.user.created_at.strftime("%m/%d/%Y"), True),
              ("Coded In", "Python", True)
             ]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)
    await ctx.message.delete()
    await ctx.send(embed=embed)
  
  #Description: 
  #  Check servers the bot is in
  #Command Usage:
  #  *servers
  @commands.command()
  @commands.is_owner()
  async def servers(self, ctx):
    serverslist = []

    for guild in self.client.guilds:
      serverslist.append(f'`-` {guild.name} ({guild.id}) | {guild.owner} ({guild.owner.id}) | {len(guild.members)} members\n')
    await ctx.send("\n".join(serverslist))

  #Description:   
  #  Leave a server 
  #Command Usage:
  #  *leaveserver serverid
  @commands.command()
  @commands.is_owner()
  async def leaveserver(self, ctx, serverid: int):
    await self.client.get_guild(serverid).leave()

async def setup(client):
  await client.add_cog(botinfo(client))
