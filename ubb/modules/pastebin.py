import os
import io

from telethon import events
from ..func import http
from ubb import Ubot


@Ubot.on(events.NewMessage(pattern=r'\.paste'))
async def paste_bin(event):
    if not event.reply_to:
        return await event.edit('Reply .paste Message|File')
    r = await event.get_reply_message()
    
    if not r.media and not r.message:
        return await event.edit('Is replied msg is text or file?')

    
    if r.media != None:
        doc = await Ubot.download_media(r)
        content = io.open(doc, 'rb').read()
        os.remove(doc)
    elif r.message:
        content = str(r.message)
    try:
        res = await http.post('https://hastebin.skyra.pw/documents', pdata=content)
        msg = f'**Pasted**: https://hastebin.skyra.pw/raw/{res.json()["key"]}'
        await event.edit(msg)
    except Exception as e:
        msg = f"**Failed to paste**: `{e}`"
        await event.edit(msg)  
