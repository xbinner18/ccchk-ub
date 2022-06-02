from ..func import http
from telethon import events
from ubb import Ubot


@Ubot.on(events.NewMessage(pattern=r'\.bin'))
async def srbin(event):
    BIN = event.message.message[len('.bin '):]
    try:
      res = await http.get(f'http://binchk-api.vercel.app/{BIN}')
      result = res.json()
      msg = f'''
      BIN: {BIN}
      BRAND: {result['brand']}
      TYPE: {result['type']}
      LEVEL: {result['level']}
      BANK: {result['bank']}
      COUNTRY: {result['country']}
      '''
      await event.edit(msg)
    except Exception as e:
      err = f'Error: {e}'
      await event.edit(err)
