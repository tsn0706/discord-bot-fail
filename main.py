#導入 Discord.py 及 from discord.ext import commands
import discord
from discord.ext import commands
import json
import asyncio
import os
import asyncio

#讀取json檔
with open("D:\\Discord機器人\\discord-bot\\setting.json","r",encoding="utf8")as jfile:
    jdata = json.load(jfile)

#bot 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!咩",intents=intents)

@bot.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', bot.user)
    game = discord.Game('窩ㄞ咩咩')#暱稱欄位文字
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.online, activity=game)

async def main():
    for filename in  os.listdir("./cmds"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")
    await bot.start(setups["TOKEN"])
if __name__=="__main__":
    asyncio.run(main())
# async def load_extension(bot):
#     for FileName in os.listdir("D:\Discord機器人\discord-bot\cmds"):#相對路徑 也可用實際路徑
#         if FileName.endswith(".py"): 
#             bot.load_extension(f"cmds.{FileName[:-3]}")
#             print(FileName)

# if __name__ == "__main__":
#     #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
#     asyncio.run(load_extension(bot))
#     bot.run(jdata["TOKEN"]) 
