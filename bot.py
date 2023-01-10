import discord
import responses
from discord.ext import commands
import tok

async def send_message(message, user_message, is_channel):
    try:
        response = responses.respond_handle(user_message)
        await message.channel.send(response) if is_channel else await message.author.send(response)
    except Exception as e:
        print(e)

bot = commands.Bot(command_prefix='$')

def run_bot():
    TOKEN = tok.token
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print("Bot is ready")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_msg = str(message.content)
        ch = str(message.channel)
        print(f"{username} in {ch}: {user_msg}")

        if user_msg.startswith("!"):
            user_msg = user_msg[1:]
            await send_message(message, user_msg, False)
        else:
            await send_message(message, user_msg, True)
        
    @client.command(pass_context=True)
    async def join(ctx):
        channel = ctx.message.author.voice.voice_channel
        await client.join_voice_channel(channel)

        
    client.run(TOKEN)
