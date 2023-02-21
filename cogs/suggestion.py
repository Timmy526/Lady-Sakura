from discord import Embed
from discord.ext import commands
from datetime import datetime

class suggest(commands.Cog, 
             name = "Suggestion",
             description = "This command is used for creating suggestions."):

  def __init__(self, client):
    self.client = client

  #Description:
  #  This command is used to make a suggestion embed + thread
  #Command Usage:
  #  *suggest (suggestion) or /suggest (suggestion)
  @commands.hybrid_command(with_app_command=True, 
                           description = "This command is used for creating suggestions.")
  async def suggest(self, ctx, *, suggestion):
    text = suggestion
    embed = Embed(
      title = "Suggestion",
      colour = 	0xffb7c5,
    )
    embed.set_thumbnail(url=ctx.author.display_avatar)
    embed.add_field(name="Submitted by", value = (ctx.author), inline = True)
    embed.add_field(name="Suggestion", value = text, inline = False)
    embed.set_footer(text=f"User ID: {str(ctx.author.id)}")
    embed.timestamp = datetime.utcnow()

    if ctx.interaction is None:
      await ctx.message.delete()
    m = await ctx.send(embed=embed)
    thumbup='👍'
    thumbdown='👎'
    await m.add_reaction(thumbup)
    await m.add_reaction(thumbdown)
    await m.create_thread(name=f"Suggest from {(ctx.author)}")
    
async def setup(client):
  await client.add_cog(suggest(client))

