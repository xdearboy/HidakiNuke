import disnake
from disnake.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", description="Проверка пинга")
    async def ping(self, ctx):
        message = await ctx.send("Пингуем...")
        embed = disnake.Embed(title="Пинг", color=disnake.Color.from_rgb(48, 49, 54))
        embed.add_field(
            name="Понг! 🏓", value=f"`{round(self.bot.latency * 1000)}ms`", inline=False
        )
        await message.edit(embed=embed)


def setup(bot):
    bot.add_cog(Ping(bot))
