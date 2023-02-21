import asyncio
#import logging
import os
import traceback
import keep_alive
import discord
from datetime import datetime
from discord.ext import commands
from pretty_help import PrettyHelp, EmojiMenu
from modules import config
import json
import os
import aiofiles

keep_alive.keep_alive()


class Bot(commands.Bot):
    async def setup_hook(self) -> None:
        # A hook called after the bot has been logged in.
        # It is NOT an event, and gets called once per uptime.
        async with aiofiles.open("config.json", "r") as f:
          self.config = json.loads(await f.read())
          print(f"[ Log ] Loaded config file")
        print(f"[ Guild ] {config.get('DISCORD', 'guildId')}")
        self.success = discord.PartialEmoji(name="yes", id=1053563004257583114, animated=True)
        self.error = discord.PartialEmoji(name="no", id=1053563003154485318, animated=True)
        self.notify = discord.PartialEmoji(name="notify", id=1053563005385842749, animated=True)
        self.loading = discord.PartialEmoji(name="loading2", id=1053563073077723218, animated=True)
        self.wait = discord.PartialEmoji(name="loading", id=1053562999748698112, animated=True)
        self.warning = discord.PartialEmoji(name="warning", id=1059530379679248514, animated=True)
      
        # await self.load_extension("jishaku")

        loaded = 0
        # load all Cogs
        for cog in os.listdir("cogs"):
            if cog.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{cog[:-3]}")
                    print(f"[ Log ] Cog {cog[:-3]} loaded")
                    loaded += 1
                except Exception as ex:
                    print(f"[ Log ] Failed to load cog {cog[:-3]}\n{ex}")
                    traceback.print_exc()
        print(f"[ Log ] {loaded} Cogs loaded")


async def main():
    bot = Bot(auto_sync_commands=True,
              command_prefix=commands.when_mentioned_or(config.get("DISCORD", "PREFIX")),
              intents=discord.Intents.all(),
              help_command=PrettyHelp(
                menu=EmojiMenu(delete_after_timeout=True),
                color=0xffb7c5
              ),
              description="Bot",
              case_insensitive=True,
              start_time=datetime.utcnow(),
              owner_id=224262978759950338,  # <<<<< REPLACE WITH YOUR USER ID, THIS IS FOR BOT OWNER ONLY COMMANDS
              activity=discord.Activity(
                  type=discord.ActivityType.watching,
                  name="Sakura Sanctuary"),
              )
  
    @bot.event
    async def on_ready():
        print(f'[ Log ] Logged in as {bot.user}')

    async with bot:
        await bot.start(config.get("DISCORD", "TOKEN"))


asyncio.run(main())
