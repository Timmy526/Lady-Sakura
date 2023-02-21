import asyncio
from discord.ext import commands


class BotManager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.wait_until_ready()
        await self.client.tree.sync(guild=None)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.message.delete()
        await ctx.send('Goodbye!', delete_after=5)
        await self.client.wait_until_ready()
        await asyncio.sleep(5)
        await self.client.close()

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, name: str):
        await ctx.message.delete()
        try:
            await self.client.reload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(e)
        await ctx.send(f'"**{name}**" Cog reloaded', delete_after=5)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, name: str):
        await ctx.message.delete()
        try:
            await self.client.unload_extension(f"cogs.{name}")
        except Exception as e:
            return await self.client.send(e)
        await ctx.send(f'"**{name}**" Cog unloaded', delete_after=5)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, name: str):
        await ctx.message.delete()
        try:
            await self.client.load_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(e)
        await ctx.send(f'"**{name}**" Cog loaded', delete_after=5)


async def setup(client):
    await client.add_cog(BotManager(client))
