from ..func import http
from telethon import events
from ubb import Ubot


@Ubot.on(events.NewMessage(pattern=r'\.tr'))
async def translate(event):
    if not event.reply_to:
        return await event.edit('Reply .tr {code}')
    r = await event.get_reply_message()
    co = event.message.message[len('.tr '):]
    try:
        res = await http.get(f'https://translate.google.com/'+
                             f'translate_a/'+
                             f't?client=dict-chrome-ex&sl=auto&'+
                             f'tl={co}&q={r.message}&tbb=1&ie=UTF-8&oe=UTF-8')
        result = res.text.strip('[""]')
        so = result[-2:]
        msg = f'''
**INPUT**: `{r.message}`
Translated from **{so}** to **{co}**
`{result[:-5]}`
'''
        await event.edit(msg)
    except Exception as e:
        await event.edit(f'Failed error: `{e}`')
