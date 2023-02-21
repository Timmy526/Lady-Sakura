from typing import Optional
from discord.ext import commands, tasks
from modules import birthday
from datetime import datetime
import traceback
import discord
from discord import app_commands


class birthdays(commands.Cog, 
           name = "Birthday", 
           description = "This is created for Birthdays!"):

  def __init__(self, client):
    self.client = client
    try:
      self.birthdayloop.start()
    except:
      pass

  def cog_unload(self):
    self.birthdayloop.cancel()

  #Description:
  #  This command is used to set your birthday
  #Command Usage:
  #   /setbirthday (m/d/Y)
  @app_commands.command()
  async def setbirthday(self, interaction: discord.Interaction, date: str):
    try:
      await birthday.setBirthday(interaction.user, date)
      await interaction.response.send_message(f"{self.client.success} I will remember your birthday! Don't Worry!", emphermal=True)
    except:
      await interaction.response.send_message(f"{self.client.error} Something went wrong, contact support!", emphermal=True)
      traceback.print_exc()
  
  #Description:
  #  This is the loop to check for birthdays
  #Command Usage: 
  #  N/A
  @tasks.loop(seconds=60)
  async def birthdayloop(self):
    now = datetime.utcnow()
    if now.hour == 00 and now.minute == 00:
      try:
        birthdays = await birthday.findBirthdays()
        if birthdays is None:
          return
        d = datetime.utcnow().strftime("%m/%d/%Y")
        today = []
        guild = self.client.get_guild(1058263210148499498)
        for b in birthdays:
          if d == b["date"].strftime("%m/%d/%Y"):
            m = guild.get_member(b["id"])
            today.append(m.mention)
    
        if len(today) > 0:
          birthdayStr = "\n".join(today)
          c = guild.get_channel(1077368786719617105)
          await c.send(birthdayStr)
      except:
        traceback.print_exc()
        
  #Description:
  #  This is a listener to remove a birthday if a member leaves
  #Command Usage: 
  #  N/A
  @commands.Cog.listener()
  async def on_member_remove(self, member):
    try:
      await birthday.removeBirthday(member)
    except:
      traceback.print_exc()
  

async def setup(client):
  await client.add_cog(birthdays(client))
