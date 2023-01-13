import discord
import responses
from discord.ext.commands import Bot
from discord import FFmpegPCMAudio
import tok

async def send_message(message, user_message, is_channel):
    try:
        response = responses.respond_handle(user_message)
        await message.channel.send(response) if is_channel else await message.author.send(response)
    except Exception as e:
        print(e)


def run_bot():
    TOKEN = tok.tok()
    intents = discord.Intents.default()
    intents.message_content = True
    #client = discord.Client(intents = intents)
    bot = Bot(command_prefix='$', intents = intents)

    @bot.event
    async def on_ready():
        print("Bot is ready")
        
    @bot.command(pass_context=True)
    async def join(ctx):
        if(ctx.author.voice):
            channel = ctx.message.author.voice.channel
            connect = await channel.connect()
            greet = FFmpegPCMAudio('assets/kita1.wav')
            connect.play(greet)
        else:
            await ctx.send("I don't want to be alone.")

    @bot.command(pass_context=True)
    async def leave(ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("See you later✨")
        else:
            await ctx.send("I'm not in a voice channel!!")

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)
        if message.author == bot.user:
            return
        username = str(message.author)
        user_msg = str(message.content)
        ch = str(message.channel)
        print(f"{username} in {ch}: {user_msg}")

        if user_msg.startswith("!"):
            user_msg = user_msg[1:]
            await send_message(message, user_msg, False)
        elif user_msg.startswith("^"):
            user_msg = user_msg[1:]
            await send_message(message, user_msg, True)
        else:
            return
        
    bot.run(TOKEN)