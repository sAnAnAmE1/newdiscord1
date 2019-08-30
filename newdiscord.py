import discord
import os
from discord import message

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("&도움 을 입력해보세요")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("&넌 누구니"):
        await message.channel.send("전 사나봇입니다만")
    if message.content.startswith("&도움"):
        await message.channel.send("넌 누구니 (자기소개를 합니다)사나봇의 제작자는 (사나봇의 제작자소개를 합니다) 개발은 언제 해 (사나봇의 귀차니즘 테스트) 사진 사나.PNG 을(사나 사진을 보여줍니다) 들을 입력해보세요 (접두사는 &입니다)")
    if message.content.startswith("&사나봇의 제작자는"):
        await message.channel.send("가장 잘생기셨고 가장 아름다운 SANA님이십니다만")
    if message.content.startswith("&개발은 언제 해"):
        await message.channel.send("나중에나중에나중에나중에나중에")
    if message.content.startswith("&이스터에그"):
        await message.channel.send("어 이스터에그를 찾다니ㄷㄷ 아니 이건 사실 힌트입니다 tkskditkfkdgo")
    if message.content.startswith("&tkskditkfkdgo"):
        await message.channel.send("&DM 이스터에그 음 이스터에그를 찾다니... 디엠을 확인해보세요...                                                                                        사나는 존예 졸귀 뿌잉")
        author = message.guild.get_member(int(message.content[4:22]))
    if message.content.startswith("&사나야사랑해"):
        await message.channel.send("&사진 사나2.png")
    if message.content.startswith("&사진 사나2.PNG"):
        await message.channel.send("&이제 사나!라고 외치세요!")
    if message.content.startswith("&사나!"):
        await message.channel.send("&사진 축하합니당.png")
    if message.content.startswith("&사진 축하합니당.png"):
        await message.channel.send("이스터에그를 찾았네요! 축하드립니다ㅎㅎ(사진 보다가 우연히 찾으신 분은 선물 안드릴겁니다")

    if message.content.startswith("&채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("&사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("&사진2"):
        pic = message.content.split(" ")[2]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("&사진3"):
        pic = message.content.split(" ")[3]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("&사진4"):
        pic = message.content.split(" ")[4]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("&사진5"):
        pic = message.content.split(" ")[5]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("&사진6"):
        pic = message.content.split(" ")[6]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("&사진7"):
        pic = message.content.split(" ")[7]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("&사진8"):
        pic = message.content.split(" ")[8]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("&사진9"):
        pic = message.content.split(" ")[9]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("&DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("&DM 이스터에그"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)


    if message.content.startswith("&뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.add_roles(role)

    if message.content.startswith("&언뮤트"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)

         
access_token = os.environ["BOT TOKEN"]            
client.run(access_token)
