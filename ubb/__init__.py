import os
import logging
import yaml

from telethon import TelegramClient
from telethon.sessions import StringSession


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
API_ID = int(os.getenv('api_id', CONFIG['api_id']))
API_HASH = os.getenv('api_hash', CONFIG['api_hash'])
DUMP_ID = os.getenv('dump_id', CONFIG['dump_id'])
STRING_SESSION = os.getenv('string_session', CONFIG['string_session'])

Ubot = TelegramClient(StringSession(STRING_SESSION),
                      API_ID,
                      API_HASH,
                      auto_reconnect=False,
                      lang_code='en')
