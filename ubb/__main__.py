import importlib
import sys
import asyncio

from ubb import Ubot
from ubb.modules import ALL_MODULES


for module_name in ALL_MODULES:
    imported_module = importlib.import_module("ubb.modules." + module_name)


async def main():
    async with Ubot:
        # Run the client until Ctrl+C is pressed, or the client disconnects
        print('Your bot is alive .alive to check\n'
              '.help to check command list\n'
              '(Press Ctrl+C to stop this)')
        await Ubot.run_until_disconnected()
 

if __name__ == '__main__':
    asyncio.run(main())
