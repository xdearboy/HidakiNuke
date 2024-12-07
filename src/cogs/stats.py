import disnake
from disnake.ext import commands

from ..utils.counter import AttackCounter


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.attack_counter = AttackCounter()

    @commands.command()
    async def stats(self, ctx):
        total_attacks = self.attack_counter.get_total_attacks()
        daily_attacks = self.attack_counter.get_daily_attacks()
        avg_attack_duration = self.attack_counter.get_avg_attack_duration()

        embed = disnake.Embed(
            title="Статистика атак", color=disnake.Color.from_rgb(48, 49, 54)
        )
        embed.add_field(name="Всего атак:", value=total_attacks, inline=False)
        embed.add_field(name="Сегодняшние атаки:", value=daily_attacks, inline=False)
        embed.add_field(
            name="Средняя продолжительность атаки (сек):",
            value=f"{avg_attack_duration:.2f}",
            inline=False,
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Stats(bot))
