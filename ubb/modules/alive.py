from ubb import Ubot
from telethon import version, events
from platform import python_version


@Ubot.on(events.NewMessage(pattern=r'[!/]start$'))
async def amialive(event):
    me = await Ubot.get_me()
    await event.reply(f'''
**{me.first_name} is Working Fine!**
**Telethon version:** `{version.__version__}`
**Python version:** `{python_version()}`
**Repo:** [GitHub](https://github.com/Xbinner18/ccchk-ub)
''') 
    
    
@Ubot.on(events.NewMessage(pattern=r'[!/]help$'))
async def helper(event):
    await event.reply(f'''
**Dont Fear help is here!**
• /start <chk ubot is up or not>.
• /st <cc|mm|yy|csc> to chk cards.
• /paste <to unpack openbullet/storm configs or paste codes> .
• /tr <translate replied msg> to eng ex reply .tr en
• /ip <chk ip fraud score>
• /bin <chk bininfo>
• /eval <py codes>
''')
