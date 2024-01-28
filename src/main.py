from discord import Intents, Client, Message
from discord.ext import commands
from dotenv import load_dotenv
import os
from typing import Final
import responses as r

load_dotenv()
DISCORD_TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    if client.user.mentioned_in(message):

        username: str = str(message.author)
        user_message: str = (str(message.content).split('>')[1])[1:]
        channel: str = str(message.channel)
        print(f'{username} said: "{user_message}" in the channel {channel}')

        await message.channel.send(r.get_response(f'User {username} says: {user_message}'))
        return


def main() -> None:
    client.run(token=DISCORD_TOKEN)


if __name__ == '__main__':
    main()
