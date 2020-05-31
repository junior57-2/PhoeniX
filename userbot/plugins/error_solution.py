# Exclusive module for PhoeniX
# By @Techy05
# You should use this module without proper credits
# Syntax (.solution <error_name>)
from telethon import events
from userbot.utils import admin_cmd
import asyncio
from telethon.tl import functions, types
from sql.global_variables_sql import SYNTAX, MODULE_LIST, SOLUTION, ERROR_LIST


@borg.on(admin_cmd(pattern="solution ?(.*)"))
async def _(event):
        if event.fwd_from:
            return
        err = event.pattern_match.group(1)
        if err:
            if err in SOLUTION:
                await event.edit(SOLUTION[err])
            else:
                await event.edit("No information for this error yet!\n**Tip: Get a list of all errors using .errors**")
        else:
            await event.edit("Please specify an error.\n**Tip: Get a list of all errors using .errors**")
