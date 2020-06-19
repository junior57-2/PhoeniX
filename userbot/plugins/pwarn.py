from math import ceil
import asyncio
import json
import random
import re
from telethon import events, errors, custom
import io

if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Userbot"):
            rev_text = query[::-1]
            buttons = paginate_help("Remove Warn")
            result = builder.article(
                "You can not remove this warn",
                text="{}\n**You have been warned!**\nYou Have 1/3 warnings.\nThe latest warning was because: Off-Topic",
                buttons=buttons,
                link_preview=False
            )
        await event.answer([result] if result else None)
        
        
