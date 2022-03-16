import discord

client = discord.Client()
token = "봇 토큰"

@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

@client.event
async def on_message(message):
    if message.content == "안녕!":
        await message.channel.send("반가워!")

client.run(token)