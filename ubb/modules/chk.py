from ..func import http
from telethon import events
from datetime import datetime
from ubb import Ubot, URL


@Ubot.on(events.NewMessage(pattern=r'\.st'))
async def st_chk(event):
    CC = event.message.message[len('.st '):]
    VALID = ('37', '34', '4', '51', '52', '53', '54', '55', '65', '6011')
    if not CC.startswith(VALID):
        return await event.edit('**Invalid CC Type**')
    try:
        req = await http.get(URL+CC)
        await event.edit(f'''
CC-->`{CC}`
RESPONSE--> **{req.json()['res']}**
GATE--> **STRIPE .5$**
DATE&TIME--> **{datetime.now()}**
**USERBOTBY**--> @XBINNER
''')
    except Exception as e:
        await event.edit(f'Error: `{e}`')
