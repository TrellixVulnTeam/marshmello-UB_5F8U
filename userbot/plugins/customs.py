import heroku3
import asyncio
import os
import requests
import math
from userbot.utils import admin_cmd
from userbot import CMD_HELP
from userbot.thunderconfig import Config

@borg.on(admin_cmd(pattern=r"heya ?(.*)"))  # initially made by @NOOB_GUY_OP
async def hhi(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "😘"
    b = giveVar[7:8]
    if not b:
        b = "✨"
    await event.edit(
        f"{a}{b}{b}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{a}{a}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{a}{a}{a}\n☁☁☁☁☁☁☁☁"
    )


# later made by me
@borg.on(admin_cmd(pattern=r"gws?(.*)"))
async def gws(event):
    giveVar = event.text
    """m = giveVar[5:-1]
    if not m:"""
    m = " Get Well Soon ! "
    a = giveVar[-1:]
    if a == "s":
        a = "🌹"
    elif not a:
        a = "🌹"
    await event.edit(f"{a}{a}{a}{a}{a}{a}{a} \n{a} {m} {a}\n{a}{a}{a}{a}{a}{a}{a}")


@borg.on(admin_cmd(pattern=r"heyyy ?(.*)"))
async def hlo(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "🤙"
    b = giveVar[7:8]
    if not b:
        b = "✨"
    await event.edit(
        f"{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{a}{a}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{a}{a}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{a}{a}{a}{b}{a}{a}{a}{a}{b}"
    )


@borg.on(admin_cmd(pattern=r"bye ?(.*)"))
async def bye(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "✨"
    b = giveVar[7:8]
    if not b:
        b = "🌺"
    await event.edit(
        f"{a}{b}{b}{a}{a}{b}{a}{a}{a}{b}{a}{b}{b}{b}{a}\n{a}{b}{a}{b}{a}{a}{b}{a}{b}{a}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{a}{a}{a}{b}{a}{a}{a}{b}{b}{a}{a}\n{a}{b}{a}{b}{a}{a}{a}{b}{a}{a}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{a}{a}{a}{b}{a}{a}{a}{b}{b}{b}{a}"
    )


CMD_HELP.update(
    {
        "customs": "__**PLUGIN NAME :** Custom animations__\
    \n\n📌** CMD ★** `.hhi(emoji)(emoji)`\
    \n**USAGE   ★  **Try it yourself (put space ) \
    \n\n📌** CMD ★** `.hhi(emoji)(emoji)`\
    \n**USAGE   ★  **Try it yourself (put space )\
    \n\n📌** CMD ★** `.gws(emoji)`\
    \n**USAGE   ★  **Try it yourself (put space )\
    \n\n📌** CMD ★** `.hlo(emoji)(emoji)`\
    \n**USAGE   ★  **Try it yourself (put space )\
    \n\n📌** CMD ★** `.bye(emoji)(emoji)`\
    \n**USAGE   ★  **Try it yourself (put space )"
    }
)
