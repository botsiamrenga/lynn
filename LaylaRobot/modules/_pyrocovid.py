#Code Owner @RSR(don't remove creditðŸ˜ª)

from telegram import ParseMode, Update, Bot, Chat
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, BaseFilter, run_async
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from LaylaRobot import dispatcher

import requests

import json
from urllib.request import urlopen


def corona(update: Update, context: CallbackContext):
    bot = context.bot
    message = update.effective_message
    state = ''
    confirmed = 0
    deceased = 0
    recovered = 0
    state_input = ''.join([message.text.split(' ')[i] + ' ' for i in range(1, len(message.text.split(' ')))]).strip()
    if state_input:
        url_india = 'https://api.covid19india.org/data.json'
        json_url = urlopen(url_india)
        state_dict = json.loads(json_url.read())
        for sdict in state_dict['statewise']:
            if sdict['state'].lower() == state_input.lower():
                confirmed = sdict['confirmed']
                deceased = sdict['deaths']
                recovered = sdict['recovered']
                state = sdict['state']
                active = sdict['active']
                break
    
    if state:
        message.reply_text(
            '*Cases in %s:* %s\n\n*Confirmed:* %s\n*Active:* %s\n*Deceased:* %s\n*Recovered:* %s' % (state, confirmed, active, deceased, recovered),
            reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Source", url="covid19india.org")]]
    ),
            parse_mode = ParseMode.MARKDOWN,
            disable_web_page_preview = True
        )
    else:
        message.reply_text(
            'You need to specify a valid Indian state!',
            parse_mode = ParseMode.MARKDOWN,
            disable_web_page_preview = True
        )


CORONA_HANDLER = CommandHandler('corona', corona)

dispatcher.add_handler(CORONA_HANDLER)
