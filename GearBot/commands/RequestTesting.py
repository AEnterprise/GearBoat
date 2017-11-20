import discord

import Variables
from Util import configuration
from commands.RoleCommands import RoleCommand


class RequestTesting(RoleCommand):
    """Requests testers to test something"""

    def __init__(self) -> None:
        super().__init__()
        self.extraHelp["info"] = "Pings the tester group with a message"

    async def execute(self, client: discord.Client, channel: discord.Channel, user: discord.user.User, params) -> None:
        role: discord.Role = discord.utils.get(channel.server.roles, id=configuration.getConfigVar("TESTER_ROLE_ID"))
        await client.edit_role(channel.server, role, mentionable=True)
        embed = discord.Embed(title="New things to test!", description=" ".join(params[0::]))
        await client.send_message(Variables.ANNOUNCEMENTS_CHANNEL, f"<@&{configuration.getConfigVar('TESTER_ROLE_ID')}>", embed=embed)
        await client.edit_role(channel.server, role, mentionable=False)

    def onReady(self, client: discord.Client):
        self.role = configuration.getConfigVar("DEV_ROLE_ID")
