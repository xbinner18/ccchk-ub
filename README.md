# CC CHECKER USERBOT

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?)


**Requirements to run this userbot**
```
 • SESSION OF TELETHON (requires your tg ac auth)
 • API_ID & APIHASH (from 'my.telegram.org')
 • URL Var of env value should be https://<appnameofheroku>.herokuapp.com/?cc= to point php file
 • If you set it correct userbot will able to make http calls at correct url to get response.
```
If you got api id n hash then lets proceed for session.
```
fork this repo login to your heroku ac create new app.
connect fork of this repo to heroku and deploy
after deployment finish click on setting icon select console.
you will get bash interface run sessionmaker file by cmd
'python3 sessionmaker.py'
put api-id hit enter
put api-hash hit enter
put your phone number of tg ac hit enter(with country code)
if you have set 2factor auth put your pwd and finnally u will get string session
click on save session copy that session we gonna use that in env varable of STRING_SESSION
```
___
You can also use termux or replit to gen session
```
git clone https://github.com/Xbinner18/ccchk-ub.git
```
 ```
 pip install --upgrade pip && pip3 install -r requirements.txt && python3 sessionmaker.py
 ```
• rest steps are same as above just give what it ask
___

Why did i used php? cause many peoples arent familiar with py i mean they prefer
php over py for checker apis so they can understand and update by themselve thats why.

## Note 
Make sure to use Proxies in php file for better response.


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
[Xbinner](https://telegram.dog/Xbinner) [xbinner18](https://github.com/xbinner18)
- Thanks to [Lonami](https://github.com/Lonami) for telethon Library.
- Thanks to [tomchristie](https://github.com/tomchristie) for httpx Library.
