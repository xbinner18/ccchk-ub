import re

from ..func import http
from telethon import events
from ubb import Ubot


@Ubot.on(events.NewMessage(pattern=r'\.bin'))
async def srbin(event):
    BIN = event.message.message[len('.bin '):]
    reply_msg = await event.get_reply_message()
    if reply_msg:
        BIN = reply_msg.message
    try:
        _BIN = re.sub(r'[^0-9]', '', BIN)
        _res = await http.get(f'http://binchk-api.vercel.app/bin={_BIN}')
        res = _res.json()
        msg = f'''
BIN: `{_BIN}`
Brand⇢ **{res["brand"]}**
Type⇢ **{res["type"]}**
Level⇢ **{res["level"]}**
Bank⇢ **{res["bank"]}**
Phone⇢ **{res["phone"]}**
Flag⇢ **{res["flag"]}**
Currency⇢ **{res["currency"]}**
Country⇢ **{res["country"]}({res["code"]})**
'''
        await event.edit(msg)
    except:
        await event.edit('Failed to parse bin data from api')
