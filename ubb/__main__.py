import importlib
import asyncio

from ubb import Ubot, TOKEN
from ubb.modules import ALL_MODULES


for module_name in ALL_MODULES:
    imported_module = importlib.import_module("ubb.modules." + module_name)


async def main():
    await Ubot.start(bot_token=TOKEN)
    try:
        # Run the client until Ctrl+C is pressed, or the client disconnects
        print('(Press Ctrl+C to stop this)\n'
              '/help to check command list\n'
              'Your bot is alive /start to check')
        await Ubot.run_until_disconnected()
    finally:
        await Ubot.disconnect()
 

if __name__ == '__main__':
    asyncio.run(main())
