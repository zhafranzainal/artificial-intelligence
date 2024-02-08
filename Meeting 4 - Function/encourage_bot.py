import os
import discord

# create default set of intents then enable intent to receive message content
permissions = discord.Intents.default()
permissions.message_content = True

# create bot
bot = discord.Client(intents=permissions)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    # send message to each server the bot belongs to
    for guild in bot.guilds:
        channel = guild.system_channel
        await channel.send(f"{bot.user} is online!")


@bot.event
async def on_message(message):
    # skip messages from the bot itself
    if message.author == bot.user:
        return

    if message.content.lower().startswith("!hi"):
        await message.channel.send("Hello 👋😃")

    if message.content.lower().startswith("!hello"):
        await message.channel.send(
            "https://media.giphy.com/media/v1"
            ".Y2lkPTc5MGI3NjExdXA3eXB5djZiczV"
            "jeHV6MGpqMXJ0OGM0OTdudTdwOTV5ZTN6eDMyZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Cmr1OMJ2FN0B2/giphy.gif")


# run bot using TOKEN from env
bot.run(os.environ['TOKEN'])
