import importlib
import sys

from ubb import LOGS, Ubot
from ubb.modules import ALL_MODULES


Ubot.start()

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("ubb.modules." + module_name)

LOGS.info("Your Bot is alive! Test it by typing .alive on any chat."
          "if you need assistance, head to https://t.me/xbinner")
LOGS.info("Your Bot Version is 1.0")

if len(sys.argv) not in (1, 3, 4):
    Ubot.disconnect()
else:
    Ubot.run_until_disconnected()
