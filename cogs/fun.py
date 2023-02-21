import discord
from discord import Embed
from discord.ext import commands
import random


class fun(commands.Cog,
          name = "Fun", 
          description = "Fun Commands"):

  def __init__(self, client):
    self.client = client

  #Description:
  #  This command is used to reverse a given message
  #Command Usage:
  #  *reverse (message)
  @commands.command(description="Reverse a Message")
  async def reverse(self, ctx, *, message: str):
    
    t_rev = message[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
    await ctx.send(f"🔁 {t_rev}")

  #Description:
  #  This command is to rate anything inputted
  #Command Usage:
  #  *rate (message)
  @commands.command(description="Rate Something")
  async def rate(self, ctx, *, message: str):
    
    rate_amount = random.uniform(0.0, 100.0)

    if message == '69':
      rate_amount = 420
    elif message == '420':
      rate_amount = 69
    else:
      rate_amount = round(rate_amount, 2)
    
    str = f"{message} is {rate_amount}% cool! <a:catnodyes:1032028076030316664>"
    
    await ctx.send(str)

  #Description:
  #  This command is a love calculator  
  #Command Usage:
  #  *love (user)
  @commands.command(description="Love Calculator")
  async def love(self, ctx, target: discord.Member = None):
    target = target or ctx.author
    if target == self.client.user:
      return await ctx.send("Get your hands off me.")
    random.seed(ctx.author.display_avatar.url + target.display_avatar.url + "69")
    r = random.randint(1,100)
    rand = r / 1.17
    str = f"{ctx.author.mention}'s love for {target.mention} is {round(rand, 2)}%.\n "
    
    if rand == 0:
      str += "Give up right now... "
    elif rand < 10:
      str += "Better go get a pet or something else to love"
    elif rand < 20:
      str += "I think you need a hug because this ain't going to happen bud"
    elif rand < 30: 
      str += f"I think {target.mention} is better off with me instead..."
    elif rand < 40: 
      str += "Seems like you are just friends... Keep it that way"
    elif rand < 50: 
      str += "Hey, there might be a chance if you get some rizz"
    elif rand < 60: 
      str += "You are close, but just not there... Maybe try being more cool... IDK"
    elif rand < 70: 
      str += "You are doing good, but you are somehow still blowing it...  **TRY HARDER**"
    elif rand < 80: 
      str += "Give it a few months, maybe you will win their love"
    elif rand < 90: 
      str += "This is pretty high... I hope you get both enjoy being in love!"
    elif rand < 100: 
      str += "What are you waiting for!?! You should both get married right now!"
   
    await ctx.send(str)

  #Description:
  #  This command is to print out lyrics to the song All Star
  #Command Usage:
  #  *allstar
  @commands.command(description="Self Explanatory If You Are Cool Enough")
  async def allstar(self, ctx):
    #target = target or ctx.author
    await ctx.send("Hey now, you're an all-star, get your game on, go play \nHey now, you're a rock star, get the show on, get paid \nAnd all that glitters is gold \nOnly shooting stars break the mold \n")

  #Description:
  #  This command is to check how how hot someone is
  #Command Usage:
  #  *hot (user)
  @commands.command(description="Hotness Scale Calculator")
  async def hot(self, ctx, user: discord.Member = None):
    user = user or ctx.author
    random.seed(user.display_avatar.url)
    r = random.randint(1, 100)
    hot = r / 1.17

    if user.id in [224262978759950338]:
      hot = random.randint(80, 100)
    
    if hot > 75:
      emoji = "🥵"
    elif hot > 50:
      emoji = "💖"
    elif hot > 25:
      emoji = "❤"
    else:
      emoji = "💔"

    await ctx.send(f"{user.name} is {round(hot, 2)}% hot {emoji}")

  #Description:
  #  This command is a troll bot command
  #Command Usage:
  #  *bothelp
  @commands.command(description="Bot Help")
  async def bothelp(self, ctx):
    await ctx.send("That's for me to know... and you to never find out... **LOSER**")
  
  #Description:
  #  This command is used for a coin flip
  #Command Usage:
  #  *coin
  @commands.command(description="Coin Flip")
  async def coin(self, ctx):
    coinsides = ["Heads", "Tails"]
    await ctx.send(f"{random.choice(coinsides)}!")

async def setup(client):
  await client.add_cog(fun(client))


