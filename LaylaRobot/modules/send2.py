from LaylaRobot import pbot as app

from LaylaRobot.modules.sysstats import bot_sys_stats

from pyrogram import filters

@app.on_callback_query(filters.regex("stats_callback"))

async def stats_callbacc(_, CallbackQuery):

    text = await bot_sys_stats()

    await app.answer_callback_query(

        CallbackQuery.id, text, show_alert=True

    )
