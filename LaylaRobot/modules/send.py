import asyncio

import os

import subprocess

import time

import psutil

from telegram.ext import run_async

from LaylaRobot import StartTime
from LaylaRobot import dispatcher
from LaylaRobot.utils import formatter
from LaylaRobot.modules.disable import DisableAbleCommandHandler
from LaylaRobot.modules.helper_funcs.alternate import send_message
from LaylaRobot.modules.helper_funcs.chat_status import user_admin


@run_async
@user_admin
def send(update, context):
    args = update.effective_message.text.split(None, 1)
    creply = args[1]
    send_message(update.effective_message, creply)


ADD_CCHAT_HANDLER = DisableAbleCommandHandler("snd", send)
dispatcher.add_handler(ADD_CCHAT_HANDLER)
__command_list__ = ["snd"]
__handlers__ = [ADD_CCHAT_HANDLER]


# Stats Module


async def bot_sys_stats():
    bot_uptime = int(time.time() - StartTime)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
{USERBOT_USERNAME}
------------------
UPTIME: {formatter.get_readable_time((bot_uptime))}
BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
"""
    return stats
