import asyncio
from telethon import events, types, errors
from ubb import Ubot, DUMP_ID


@Ubot.on(events.NewMessage())  # pylint:disable=E0602
async def check_incoming_messages(event):
    entities = event.message.entities
    prefixes = ['?', '/', '.', '!']
    m = event.message.message
    if m.startswith(tuple(prefixes)) or len(m) < 23 or event.is_private:
        return
    is_cc = False
    if entities:
        for entity in entities:
            if isinstance(entity, types.MessageEntityBankCard):
                is_cc = True
            if is_cc:
                try:
                    await asyncio.sleep(3)
                    await Ubot.send_message(DUMP_ID, m)
                except errors.FloodWaitError as e:
                    print(f'flood wait: {e.seconds}')
                    await asyncio.sleep(e.seconds)
                    await Ubot.send_message(DUMP_ID, m)
