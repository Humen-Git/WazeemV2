class script(object):
    START_TXT = """<i>๐งi {}, ๐ญ๐๐ผ๐พ ๐๐ ๐๐พ๐พ๐ ๐๐๐ ๐
 ๐จ'๐ ๐๐๐๐ ๐บ ๐๐๐๐๐๐พ ๐๐๐พ - ๐ฟ๐๐๐ผ๐๐๐๐๐พ๐ฝ ๐บ๐๐๐๐ฟ๐๐๐๐พ๐ ๐ป๐๐\n\n
 i๐๐ ๐พ๐บ๐๐ ๐๐ ๐๐๐พ ๐๐พ; ๐๐๐๐ ๐บ๐ฝ๐ฝ ๐๐พ ๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐บ๐ ๐บ๐ฝ๐๐n,๐จ ๐ถ๐๐๐ ๐ฌ๐บ๐๐บ๐๐พ ๐จ๐๐๐ ๐ณ๐๐พ ๐ฑ๐พ๐๐๐๐ฅ</i>"""
    HELP_TXT = """<b><i>๐ง๐พ๐๐๐ ๐ฌ๐. {} ๐จ๐'๐ ๐ฌ๐ ๐ง๐พ๐๐ ๐ฌ๐๐ฝ๐๐๐พ</b>"""
    ABOUT_TXT = """<b><i>โข ๐ฌ๐ ๐ญ๐บ๐๐พ: <a href=https://t.me/cvEva_Bot><b>Wแดแดขแดแดแด โก</b></a>
โข ๐ฌ๐ ๐ต๐พ๐๐๐๐๐ : v2.1
โข ๐ฃ๐พ๐๐๐๐พ๐๐พ๐ : <a href=https://t.me/humen_tg><b>Hแดแดแดษด โ</b></a>
โข ๐ซ๐บ๐๐๐๐บ๐๐พ : ๐ฏ๐๐๐๐๐๐บ๐
โข ๐ฅ๐๐บ๐๐พ๐ถ๐๐๐ : ๐ฏ๐๐๐๐๐ 3
โข ๐ง๐๐๐๐พ๐ฝ ๐ฎ๐ : ๐ง๐พ๐๐๐๐
โข ๐ฃ๐บ๐๐บ๐ก๐บ๐๐พ : ๐ฌ๐๐๐๐ ๐ฃ๐ก
๐ ๐ญ๐๐๐พ : เดเดฐเตเด เดชเตเดเดฟเดเตเดเตเดฃเตเด เดเดฒเตเดฒเดพเดตเตผเดเตเดเตเด เดเดชเดฏเตเดเดฟเดเตเดเดพเด</i>"""
    SOURCE_TXT = """<b>NOTE:</b>
- Unfortunately This Bot is an Closed source project. 
-   

<b>But Base Repo Open Source:</b>
- <a href=https://github.com/EvamariaTG/EvaMaria>Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    
    BUTTON_TXT = """Help: <b>Buttons</b>

- Wazeem Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Wazeem Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Cinemaveed)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<u>Cแดสสแดษดแด Dแดแดแดสแดsแด Sแดแดแดแดs</u>

๐ ๐ฅ๐๐๐พ๐ ๐ฒ๐บ๐๐พ๐ฝ: <code>{}</code>
๐ฉ๐ปโ๐ป ๐ด๐๐พ๐๐: <code>{}</code>
๐ฅ ๐ฆ๐๐๐๐๐: <code>{}</code>
๐๏ธ ๐ฎ๐ผ๐ผ๐๐๐๐ฝ: <code>{}</code> ๐ผ๐๐ฑ
๐ ๐ฅ๐๐พ๐พ ๐ฒ๐๐๐๐บ๐๐พ: <code>{}</code> ๐ผ๐๐ฑ
"""
    CPU_TXT = """<i><u>๐ฌ๐ ๐ฒ๐พ๐๐๐พ๐ ๐ฒ๐๐บ๐๐๐๐ก</u></i>
    
<b>โข ๐ข๐๐ ๐ด๐๐บ๐๐พ - [๐ข๐๐๐๐๐ ๐ฒ๐๐๐]๐</b>
<b>โข ๐ฑ๐บ๐ ๐ด๐๐บ๐๐พ - [๐ข๐๐๐๐๐ ๐ฒ๐๐๐]๐</b>
"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
