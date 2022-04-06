class script(object):
    START_TXT = """<b>Hey {} 👋😘
I'm <a href=https://t.me/{}>{}</a>, admin of <a href=https://t.me/pencemodesign>Pencemo Designs</a></b>"""
    HELP_TXT = """Hey 👋😘👋😘
Here is the help for my commands...
Click button billow to use 👇"""
    ABOUT_TXT = """<b>Something About Me ✌️

◉ My Name : {}
◉ My UserName : @viruzZbot
◉ MyDev : <a href=https://t.me/mnmsby>α̅η̲ɗɾo͚ȋɗ കുഞ്ഞപ്പൻ</a>
◉ Support : <a href=https://t.me/pencemodesign>Pencemo Design</a>
◉ Updates : <a href=https://t.me/pencemodesigns>Pencemo Designs</a>
◉ Server : <a href=https://herokuapp.com/>Heroku</a>
◉ Source Code : <a href=https://t.me/AdhavaaBiriyaniKittiyalo>Click here</a></b>"""
    
    SOURCE_TXT = """<b>Our Services 🌐

🗣 Telegram Groups:</b>
https://t.me/pencemodesign
https://t.me/free_graphics_download

<b>👥 Telegram Channels:</b>
https://t.me/pencemodesigns
https://t.me/pencemo_mockup
https://t.me/pencemo_tools
https://t.me/design_soft_app
https://t.me/vfx_temp
https://t.me/+XrXE3qJbZRM1MWJl

<b>🤖 Telegram Bots:</b>
https://t.me/Typopng_bot
https://t.me/Unicodepro_bot
https://t.me/FreeGfx_bot

<b>Follow Us :</b>

<b>Youtube:</b>
youtube.com/c/pencemodesigns

<b>Facebook:</b>
www.facebook.com/pencemodesigns

<b>Instagram :</b>
www.instagram.com/pencemo_designs"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

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
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /settings  -  <code>to change settings.</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """◉ Totel Files: <code>{}</code>
◉ Totel Users: <code>{}</code>
◉ Totel Chats: <code>{}</code>
◉ Used Storage: <code>{}</code> 𝙼𝚒𝙱
◉ Free Storage: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
