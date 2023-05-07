# CC CHECKER & SCRAPPER USERBOT

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?)


**Requirements to run this userbot**
```
 • SESSION OF TELETHON (requires your tg ac auth)
 • API_ID & APIHASH (from 'my.telegram.org')
 • DUMP_ID = CHANNEL ID WHERE U WANT TO SEND SCRAPPED CARDS.
```
If you got api id n hash then lets proceed for session.
```
fork this repo login to your heroku ac create new app.
connect fork of this repo to heroku and deploy
after deployment finish click on more option select run console.
you will get bash interface run sessionmaker file by cmd
'python3 sessionmaker.py'
put api-id hit enter
put api-hash hit enter
put your phone number of tg ac hit enter(with country code)
if you have set 2factor auth put your pwd and finnally u will get string session
click on save session copy that session we gonna use that in env varable of STRING_SESSION
```
___
## By Termux StringSession:
```
git clone https://github.com/Xbinner18/ccchk-ub.git (clone this repo)

1- pkg install openssl (optional if httpclient give errors)

2- pip install --upgrade pip (if pip not updated already)

3- pip3 install telethon

4- python3 ccchk-ub/sessionmaker.py
```
• rest steps are same as above just give what it ask
___

~~Why did i used php? cause many peoples arent familiar with py i mean they prefer
php over py for checker apis so they can understand and update by themselve thats why.~~

## Running Locally
```
git clone https://github.com/xbinner18/ccchk-ub.git && pip3 install -r ccchk-ub/requirements.txt && python3 -m ubb
```

## Note 
Make sure to use Proxies for sending post requests for better result.


```diff
- <#Disclaimer>
- Your Telegram account may get terminated by TG.
- I am not responsible for any inappropriate use of this userbot.
- I have created this for education purpose only.
- This project doesnt support any cybercrime its just for edu.
- This is an opensource project selling isnt allowed.
```


# Credits
•
[Xbinner](https://telegram.dog/Xbinner69) [xbinner18](https://github.com/xbinner18)
- Special thanks to [Paperplane](https://github.com/RaphielGang/Telegram-Paperplane) for structure
- Thanks to [Lonami](https://github.com/Lonami) for telethon Library.
- Thanks to [tomchristie](https://github.com/tomchristie) for httpx Library.
