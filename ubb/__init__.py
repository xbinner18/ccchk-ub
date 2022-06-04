import os
import logging

from telethon import TelegramClient
from telethon.sessions import StringSession


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

ENV = bool(os.getenv('ENV', True))
API_ID = int(os.getenv('API_ID', None))
API_HASH = os.getenv('API_HASH', None)
URL = os.getenv('URL', None)
DUMP_ID = int(os.getenv('DUMP_ID', None))
STRING_SESSION = os.getenv('STRING_SESSION', None)

Ubot = TelegramClient(StringSession(STRING_SESSION),
                      API_ID,
                      API_HASH,
                      auto_reconnect=False,
                      lang_code='en')
