import os
import discord

# get default set of intents then enable intent to receive message content
permissions = discord.Intents.default()
permissions.message_content = True

# represent bot
client = discord.Client(intents=permissions)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # send message to each server it belongs to
    for guild in client.guilds:
        channel = guild.system_channel
        await channel.send(f"{client.user} is online!")


@client.event
async def on_message(message):
    # check if the message is from the bot itself
    if message.author == client.user:
        return

    if message.content.lower().startswith("!hi"):
        await message.channel.send("Hello 👋😃")

    if message.content.lower().startswith("!hello"):
        await message.channel.send(
            "https://media.giphy.com/media/v1"
            ".Y2lkPTc5MGI3NjExdXA3eXB5djZiczV"
            "jeHV6MGpqMXJ0OGM0OTdudTdwOTV5ZTN6eDMyZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Cmr1OMJ2FN0B2/giphy.gif")


# Run bot using TOKEN from env
client.run(os.environ['TOKEN'])
