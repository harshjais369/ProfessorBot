from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, mafiaversion
from pathlib import Path
import asyncio
import telethon.utils

MAFIA_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/e97d640332ce5eadb3f89.mp4"

os.system("pip install -U telethon")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting ProfessorBot...")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("ProfessorBot Startup Completed!")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print(f"""PROFESSOR BOT IS ON!!! PROFESSOR BOT VERSION:- {mafiaversion} YOUR ββππ½πΌπππβ πΉππ IS READY TO USE! TO CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping/.test) ENJOY YOUR BOT! Contact @harshjais369 (Telegram) for any kind of issues regarding ProfessorBot.""")
async def mafia_is_on():
    try:
        if Config.MAFIABOT_LOGGER != 0:
            await bot.send_file(
                Config.MAFIABOT_LOGGER,
                MAFIA_PIC,
                caption=f"ΰΌ π£πΏπΌπ³π²πππΌπΏ ππΌπ ΰΌ\n\n**ππ΄πππΈπΎπ½ βͺ** `{mafiaversion}`\n\nππ²π©π `.ping` or `.alive` π­π¨ ππ‘πππ€!\n\nπ²ππππππ @harshjais369 ππ ππππππ πππ’ πππ ππ πππ ππ πππ πππ’ ππππ ππ ππππππ πππππππππ πππ πππ.",
            )
    except Exception as e:
        LOGS.info(str(e))

bot.loop.create_task(mafia_is_on())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
