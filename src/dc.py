import discord
import requests

discord_token = ""#discordのBOTのトークン

client = discord.Client()

@client.event
async def on_ready():
    print('Done')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.channel.id == '':#反応させたいチャンネルのID
        url = 'https://api.mcsrvstat.us/2/サーバーIP:19132'
        response = requests.get(url)
        jsonData = response.json()

        if jsonData["online"]==False:
            embed = discord.Embed(title="現在のサーバー稼働状況", description="オフライン", color=0xff0000)
            await message.channel.send(embed=embed)
            return
        plyrs=""

        try:
            for i in jsonData["players"]["list"]:
                plyrs=plyrs+i+"\n"
        except KeyError:
            plyrs="プレイヤーはいません。\n"

        embed = discord.Embed(title="現在のサーバー稼働状況", description="オンライン", color=0x00ff00)
        embed.set_author(name="最上部に表示させたいテキスト", icon_url="お好きなアイコン")
        embed.add_field(name="IP:PORT", value=jsonData['hostname']+":"+str(jsonData['port']))
        embed.add_field(name="サーバー内のプレーヤー数", value=str(jsonData['players']['online'])+"/"+str(jsonData["players"]["max"]))
        embed.add_field(name="サーバー内のプレーヤー", value=plyrs, inline=False)
        await message.channel.send(embed=embed)
        return


client.run(discord_token)
