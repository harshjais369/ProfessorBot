# Thanks to MafiaBot
# Re-engineered as ProfessorBot by @harshjais369

import asyncio
import random
from telethon import events, version
from userbot import mafiaversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from . import *
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "π£πΏπΌπ³π²πππΌπΏ ππΌπ"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

MAFIA_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/e97d640332ce5eadb3f89.mp4"
pm_caption = "  __**π₯β‘ πΏππΎπ΅π΄πππΎπ π±πΎπ πΈπ π°π»πΈππ΄ β‘π₯**__\n\n"

pm_caption += f"**ββββββββββββββββββββββ**\n\n"
pm_caption += (
    f"                 ππππππππ\n       **γπ[{DEFAULTUSER}](tg://user?id={mafia})πγ**\n\n"
)
pm_caption += f"ββββββββββββββββββββββ\n"
pm_caption += f"β£β’**β³ Telethon:** `{version.__version__}`\n"
pm_caption += f"β£β’**β³ Version:** `{mafiaversion}`\n"
pm_caption += f"β£β’**β³ Sudo:** `{sudou}`\n"
pm_caption += f"β£β’**β³ Creator:** Himanshu\n"
pm_caption += f"β£β’**β³ Re-engineered by:** Harsh Jaiswal\n"
pm_caption += f"β£β’**β³ Contact:** [α΄α΄α΄ Κα΄Κα΄ ππ»](https://t.me/harshjais369)\n"
pm_caption += f"ββββββββββββββββββββββ\n"
pm_caption += "   πΈ [Repository](https://github.com/harshjais369/ProfessorBot) πΈ [License](https://github.com/harshjais369/ProfessorBot/blob/main/LICENSE) πΈ"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, MAFIA_IMG,caption=pm_caption)

    
CmdHelp("alive").add_command(
  "alive", None, "To check am I alive."
).add()
