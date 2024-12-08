from disnake.ext import commands, tasks

# Самый простой автоливер на планете земля.


class Autoleave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.leave_task.start()

    @tasks.loop(
        hours=4
    )  # Ставьте время, в часах/минутах/секундах, когда вы хотите, чтобы бот вышел из серверов.
    async def leave_task(self):
        for guild in self.bot.guilds:
            await guild.leave()


def setup(bot):
    bot.add_cog(Autoleave(bot))
