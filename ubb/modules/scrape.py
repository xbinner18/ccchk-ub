import re
import asyncio
from telethon import events, types, errors
from ..func import http
from bs4 import BeautifulSoup as bs
from ubb import Ubot, DUMP_ID


@Ubot.on(events.NewMessage())  # pylint:disable=E0602
async def check_incoming_messages(event):
    me = await Ubot.get_me()
    if event.sender_id == me.id:
        return
    entities = event.message.entities
    prefixes = ['?', '/', '.', '!']
    m = event.message.message
    if m.startswith(tuple(prefixes)) or len(m) < 25 or event.is_private or len(m) > 600:
        return
    is_cc = False
    if entities:
        for entity in entities:
            if isinstance(entity, types.MessageEntityBankCard):
                is_cc = True
            if is_cc:
                try:
                    x = re.findall(r'\d+', m)
                    if len(x) > 10:
                        return
                    BIN = re.search(r'\d{15,16}', m)[0][:6]
                    r = await http.get(f'https://bins.ws/search?bins={BIN}')
                    soup = bs(r, features='html.parser')
                    k = soup.find("div", {"class": "page"})
                    MSG = f"""
{m}

{k.get_text()[62:]}
"""
                    await asyncio.sleep(3)
                    await Ubot.send_message(DUMP_ID, MSG)
                except errors.FloodWaitError as e:
                    print(f'flood wait: {e.seconds}')
                    await asyncio.sleep(e.seconds)
                    await Ubot.send_message(DUMP_ID, MSG)
