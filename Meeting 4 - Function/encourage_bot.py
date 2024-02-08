import os
import discord
import random

# create default set of intents then enable intent to receive message content
permissions = discord.Intents.default()
permissions.message_content = True

# create bot
bot = discord.Client(intents=permissions)

sad_words = ["sad", "depressed", "angry", "hurting", "stressed"]

encouragements_list = [
    "Cheer up! 🤗",
    "Hang in there 😉",
    "You are a great person!👍",
    "Come on! You can do it! 💪",
    "Stay strong 🥰"
]

happy_words = ["happy", "glad", "joyful", "satisfied", "blessed"]

congratulations_list = [
    "There you go! 👏",
    "Keep up the good work 👍",
    "Keep it up 🙌",
    "Good job 👍",
    "I’m so proud of you! 🥰"
]

songs_list = [
    "https://youtu.be/2fBxXBqRWSY",
    "https://youtu.be/L3wKzyIN1yk",
    "https://youtu.be/Slv3LFYYokQ"
]


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

    if any(word in message.content for word in sad_words):
        response = random.choice(encouragements_list)
        await message.channel.send(response)

    if any(word in message.content for word in happy_words):
        response = random.choice(congratulations_list)
        await message.channel.send(response)

    if message.content.lower().startswith("!random song"):
        response = random.choice(songs_list)
        await message.channel.send(response)


# run bot using TOKEN from env
bot.run(os.environ['TOKEN'])
