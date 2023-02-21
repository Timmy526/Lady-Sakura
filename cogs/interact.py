import random

import discord
from discord.ext import commands
from discord.app_commands import Group


class Interact(commands.Cog):
    def __init__(self, client):
        self.client = client

    interactGroup = Group(name="interact", description="Member interaction commands")

    #Description:
    #  This command is for a interaction slap
    #Command Usage:
    #  
    @interactGroup.command(name="slap", description="Slap yourself or another member")
    async def slap(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://gifdb.com/images/thumbnail/saki-saki-slap-hw8e4zgz8o2skwqs.gif",
            "https://64.media.tumblr.com/22bf30fb391795063b362e75d044f171/745f34757f4c1b7b-a0/s1280x1920"
            "/c33225a16339984f8fc9d7fb97bfb628e27072d2.gif",
            "https://i.kym-cdn.com/photos/images/newsfeed/000/940/326/086.gif",
            "https://gifimage.net/wp-content/uploads/2017/07/anime-slap-gif-20.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5, description=f'{interaction.user.mention} slapped {msg} 😵')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="kiss", description="Kiss yourself or another member")
    async def kiss(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://c.tenor.com/jnndDmOm5wMAAAAC/kiss.gif",
            "https://www.gifcen.com/wp-content/uploads/2022/03/anime-kiss-gif-1.gif",
            "https://acegif.com/wp-content/uploads/anime-kissin-15.gif",
            "https://acegif.com/wp-content/uploads/anime-kiss-6.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'

        embed = discord.Embed(colour=0xffb7c5, description=f'{interaction.user.mention} kissed {msg} 😘')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="hug", description="Hug yourself or another member")
    async def hug(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://i.pinimg.com/originals/f4/e9/79/f4e9792eb172908a19df95cd973ee64b.gif",
            "https://c.tenor.com/kCZjTqCKiggAAAAC/hug.gif",
            "https://aniyuki.com/wp-content/uploads/2022/06/anime-hugs-aniyuki-56.gif",
            "https://aniyuki.com/wp-content/uploads/2022/06/anime-hugs-aniyuki-22.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'

        embed = discord.Embed(colour=0xffb7c5, description=f'{interaction.user.mention} hugged {msg} 🤗')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="love", description="Love yourself or another member")
    async def love(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://i.pinimg.com/originals/23/6f/d9/236fd97aa26b093cb1dcb5ed35879ce5.gif",
            "https://c.tenor.com/eaFidDiTve0AAAAC/love-you-so-much-anime.gif",
            "https://c.tenor.com/lvXZ-8qNWFwAAAAC/anime-love-love.gif",
            "https://c.tenor.com/lQHpiaXOQuMAAAAC/anime-heart-eyes.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'

        embed = discord.Embed(colour=0xffb7c5, description=f'{interaction.user.mention} loves {msg} 😍')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="hate", description="Hate yourself or another member")
    async def hate(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://c.tenor.com/cYRAeQqpaUMAAAAC/anime-angry-slow-loop.gif",
            "https://i.pinimg.com/originals/19/97/28/199728c74eb00a12d2d2c8a1ad440574.gif",
            "https://media2.giphy.com/media/FAI5TtHYYEges/giphy.gif",
            "https://i.pinimg.com/originals/cb/7e/51/cb7e5176ab8f90e3acbd6db4a1643ef1.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'

        embed = discord.Embed(colour=0xffb7c5, description=f'{interaction.user.mention} hates {msg} 😠')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="simp", description="Simp for yourself or another member")
    async def simp(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://i.pinimg.com/originals/35/87/3f/35873fedb41933ec89346fd0e7cc330e.gif",
            "https://c.tenor.com/nOARJZENR9UAAAAC/anime-in-love.gif",
            "https://i.gifer.com/2q3j.gif",
            "https://gifdb.com/images/thumbnail/cute-anime-shion-in-love-9q3k3jblbpfedh2q.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'

        embed = discord.Embed(colour=0xffb7c5, description=f'<@{interaction.user.mention}> simps for {msg} 🤭')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="bark", description="Bark for yourself or another member")
    async def bark(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://c.tenor.com/5A-IpGp92VMAAAAC/barking-dogs-barking.gif",
            "https://media1.giphy.com/media/87aTc1Robknj9RL8yZ/giphy.gif",
            "https://media4.giphy.com/media/3oKIPusxB2uXOmoP0k/giphy.gif",
            "https://64.media.tumblr.com/6013be3450d7f83d0dfa24efb6156a6f/tumblr_oj948cl4FQ1ufzk7po1_500.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5, description=f'{interaction.user.mention} barked at {msg} 🐶')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="meow", description="Meow for yourself or another member")
    async def meow(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://media2.giphy.com/media/13lWraa7dfb7G0/giphy.gif",
            "https://media0.giphy.com/media/rIQHCUPuYAogw/giphy.gif",
            "https://media0.giphy.com/media/K1tgb1IUeBOgw/200.gif",
            "https://c.tenor.com/CcOsj1a1efAAAAAC/cat-cute.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5, description=f'{interaction.user.mention} meowing at {msg} 🐱')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="pat", description="Pat yourself or another member")
    async def pat(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://c.tenor.com/-hkJYNs7tUkAAAAC/anime-pat.gif",
            "https://i.pinimg.com/originals/d7/c3/26/d7c326bd43776f1e0df6f63956230eb4.gif",
            "https://gifimage.net/wp-content/uploads/2017/09/anime-head-pat-gif.gif",
            "https://64.media.tumblr.com/4cadc77fb9225e39dcdb8e2763bb80b6/2952b2b04a733a04-e6/s540x810"
            "/1a4b475a64321de741441d24436f3cbf373b6525.gif "
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5, description=f'{interaction.user.mention} is patting {msg} 🖐️')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="twerk", description="Twerk on yourself or another member")
    async def twerk(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://c.tenor.com/5R6BmgRA1joAAAAC/blazedpx-pokemon.gif",
            "https://c.tenor.com/YOQQrUhyd7wAAAAC/anime-girl.gif",
            "https://c.tenor.com/zegU1_9_oaQAAAAC/cat-twerk.gif",
            "https://www.gifcen.com/wp-content/uploads/2021/04/twerk-gif-15.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5, description=f'{interaction.user.mention} is twerking on {msg} 🤔')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="lick", description="Lick yourself or another member")
    async def lick(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://media1.giphy.com/media/YqQt3rkzFXbREtTURJ/giphy.gif",
            "https://c.tenor.com/jyv9sexi1fYAAAAC/anime-lick.gif",
            "https://2.bp.blogspot.com/-eIfbvrA9mwk/XW351cpjVYI/AAAAAAABnTs/tjrdbZ74dlsheSV1oJwI0emk3s_xw1xMwCKgBGAs"
            "/s1600/HenSuki%2B-%2BEpisode%2B6%2B-%2BSayuki%2BLicks%2BKeiki.gif",
            "https://c.tenor.com/al640NjsUccAAAAC/lick-intimate.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5,
                              description=f'{interaction.user.mention} licked {msg} 😝')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="yell", description="Yell at yourself or another member")
    async def yell(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://66.media.tumblr.com/fafed957708ab99f63be3132ebbe06cb/tumblr_pkmckhUima1th206io2_640.gif",
            "https://i.gifer.com/97QQ.gif",
            "https://c.tenor.com/ZqZtPdSlUC8AAAAC/angry-anime.gif",
            "https://c.tenor.com/Wu1pdRYgYUoAAAAC/angry-anime.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5, description=f'**{interaction.user.mention} is yelling at {msg}** 📢')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_messsage(content=user.mention, embed=embed)

    @interactGroup.command(name="makeout", description="Makeout with yourself or another member")
    async def makeout(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://acegif.com/wp-content/uploads/anime-kissin-2.gif",
            "https://c.tenor.com/_8oadF3hZwIAAAAC/kiss.gif",
            "https://c.tenor.com/V0nBQduEYb8AAAAC/anime-kiss-making-out.gif",
            "https://acegif.com/wp-content/uploads/anime-kissin-15.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5, description=f'{interaction.user.mention} is making out with {msg} 😳')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="poke", description="Poke yourself or another member")
    async def poke(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://c.tenor.com/3dOqO4vVlr8AAAAC/poke-anime.gif",
            "https://c.tenor.com/nRKOOicoT8YAAAAC/anime-poke.gif",
            "https://giffiles.alphacoders.com/186/186802.gif",
            "https://c.tenor.com/1VWcl-qLSpwAAAAC/milk-and-mocha-bears-poke.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5, description=f'{interaction.user.mention} just poked {msg} 👈')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="holdhands", description="Hold hands with yourself or another member")
    async def holdhands(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://c.tenor.com/WUZAwo5KFdMAAAAC/love-holding-hands.gif",
            "https://i.gifer.com/YjED.gif",
            "https://c.tenor.com/cxhP0s4TErAAAAAC/anime-hands-clasped.gif",
            "https://i.pinimg.com/originals/80/15/e2/8015e269b33d5f5e0de776fe7a0b26ec.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5, description=f'{interaction.user.mention} is holding hands with'
                                                          f' {msg} 🧑‍🤝‍🧑')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="bonk", description="Bonk yourself or another member")
    async def bonk(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://i.makeagif.com/media/11-14-2014/xdkFbA.gif",
            "https://media2.giphy.com/media/43bOrDOasXG6Y/200.gif",
            "https://static.wixstatic.com/media/67e371_3d2a2f4e757f430ab1257bd33efb5d7e~mv2.gif",
            "https://media1.giphy.com/media/dxJ0jmXBitv4Q/giphy.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5,
                              description=f'{interaction.user.mention} bonked {msg} 😈')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="pinch", description="Pinch yourself or another member")
    async def pinch(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://media.tenor.com/wp1yRUu9byYAAAAC/anime-pinch.gif",
            "https://64.media.tumblr.com/a4046e08081f14b1656cffcfd6544b14/tumblr_p3huk9tY4O1wn2b96o1_540.gif",
            "https://giffiles.alphacoders.com/137/13763.gif",
            "https://animeforums.net/uploads/monthly_2019_07/large.TvolNDS.gif.a03cd561e0085cfcc5b0db827412a74c.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5,
                              description=f'{interaction.user.mention} pinched {msg} 🤏')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="bite", description="Bite yourself or another member")
    async def bite(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://media.tenor.com/n0DPyBDtZHgAAAAC/anime-bite.gif",
            "https://c.tenor.com/48DDFOcNQBYAAAAC/anime-bite.gif",
            "https://c.tenor.com/_AkeqheWU-4AAAAC/anime-bite.gif",
            "https://gifimage.net/wp-content/uploads/2017/09/anime-bite-gif-10.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5,
                              description=f'{interaction.user.mention} bit {msg} 🫦')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="punch", description="Punch yourself or another member")
    async def punch(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://media.tenor.com/VrWzG0RWmRQAAAAC/anime-punch.gif",
            "https://media2.giphy.com/media/NuiEoMDbstN0J2KAiH/giphy.gif",
            "https://i.pinimg.com/originals/d7/c3/0e/d7c30e46a937aaade4d7bc20eb09339b.gif",
            "https://64.media.tumblr.com/a3a036b49974fc6a959523a8c2d6f677/tumblr_p8zgtvrr5e1r55oyno1_640.gif",
            "https://media.tenor.com/s0bU-NO1QIQAAAAC/anime-punch.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "themselves for some reason..."
        else:
            msg = f'{user.mention}'
        embed = discord.Embed(colour=0xffb7c5,
                              description=f'{interaction.user.mention} punched {msg} 👊')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)

    @interactGroup.command(name="cry", description="Cry by yourself or with another member")
    async def cry(self, interaction: discord.Interaction, user: discord.Member = None):
        gifs = [
            "https://media.tenor.com/YM3fW1y6f8MAAAAC/crying-cute.gif",
            "https://www.icegif.com/wp-content/uploads/sad-anime-icegif.gif",
            "https://media.tenor.com/C6X4B6T41K4AAAAC/sad-anime.gif",
            "https://aniyuki.com/wp-content/uploads/2021/09/aniyuki-sad-anime-gif-64.gif"
        ]
        if user is None:
            user = interaction.user
            msg = "for some reason..."
        else:
            msg = f'with {user.mention}'
        embed = discord.Embed(colour=0xffb7c5,
                              description=f'{interaction.user.mention} is crying {msg}'
                                          f' 😭')
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(content=user.mention, embed=embed)


async def setup(client):
    await client.add_cog(Interact(client))
