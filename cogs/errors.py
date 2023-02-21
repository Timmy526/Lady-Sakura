import math
import sys
import traceback

import discord
from discord.ext import commands


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # get the original exception
        error = getattr(error, "original", error)

        if isinstance(error, commands.BotMissingPermissions):
            missing = [
                perm.replace("_", " ").replace("guild", "server").title()
                for perm in error.missing_permissions
            ]
            if len(missing) > 2:
                fmt = "{}, and {}".format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = " and ".join(missing)

            embed = discord.Embed(
                title="Missing Permissions",
                description=f"I am missing **{fmt}** permissions to run this command :(",
                color=0xFF0000,
            )
            return await ctx.reply(embed=embed)

        if isinstance(error, commands.DisabledCommand):
            await ctx.reply("This command has been disabled.")
            return

        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                title="Cooldown",
                description=f"This command is on cooldown, please retry in {math.ceil(error.retry_after)}s.",
                color=0xFF0000,
            )
            await ctx.reply(embed=embed)
            return

        if isinstance(error, commands.MissingPermissions):
            missing = [
                perm.replace("_", " ").replace("guild", "server").title()
                for perm in error.missing_permissions
            ]
            if len(missing) > 2:
                fmt = "{}, and {}".format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = " and ".join(missing)
            embed = discord.Embed(
                title="Insufficient Permission(s)",
                description=f"You need the **{fmt}** permission(s) to use this command.",
                color=0xFF0000,
            )
            await ctx.reply(embed=embed)
            return

        if isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send("This command cannot be used in direct messages.")
            except discord.Forbidden:
                raise error
            return

        if isinstance(error, discord.errors.Forbidden):
            try:
                embed = discord.Embed(
                    title="Forbidden",
                    description=f"Error - 403 - Forbidden | Missing perms",
                    color=0xFF0000,
                )
                await ctx.reply(embed=embed)
            except:
                print("Failed forbidden")
            return

        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(
                title="Permissions Not Satisfied",
                description=f"You do not have permissions to use this command",
                color=0xFF0000,
            )
            await ctx.reply(embed=embed)
            return

        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(
                title="Member Not Found",
                description=f"The member you specified was not found",
                color=0xFF0000,
            )
            await ctx.reply(embed=embed)
            return

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Missing Argument",
                description=f"You are missing a required argument",
                color=0xFF0000,
            )
            await ctx.reply(embed=embed)
            return

        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title="Bad Argument",
                description=f"The argument you gave was invalid",
                color=0xFF0000,
            )
            await ctx.reply(embed=embed)
            return

        if isinstance(error, commands.UserInputError):
            embed = discord.Embed(
                title="Invalid Input",
                description=f"The input you gave was invalid.\n {ctx.command.help}",
                color=0xFF0000,
            )
            await ctx.reply(embed=embed)
            return

        if isinstance(error, commands.CommandNotFound):
            return

        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

        # get error log channel
        error_channel = self.client.get_channel(1013189912666849381)

        # send error to error log channel
        embed = discord.Embed(
            title="Error",
            description=f"{ctx.author.mention} has encountered an error in **{self.client.prefix}{ctx.command.qualified_name}**",
            color=0xFF0000,
            timestamp=ctx.message.created_at,
        )
        embed.set_footer(text=f"Error occured on")
        embed.add_field(name="Trackback", value=f"```py\n{traceback.print_exc()}\n```")
        await error_channel.send(embed=embed)

        if hasattr(ctx.command, "on_error"):
            return


async def setup(client):
    await client.add_cog(Errors(client))