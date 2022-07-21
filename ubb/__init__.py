import os
import logging

from telethon import TelegramClient


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

ENV = bool(os.getenv('ENV', True))
API_ID = int(os.getenv('API_ID', None))
API_HASH = os.getenv('API_HASH', None)
DUMP_ID = int(os.getenv('DUMP_ID', None))
TOKEN = os.getenv('TOKEN', None)

Ubot = TelegramClient('bot',
                      API_ID,
                      API_HASH
                     )
