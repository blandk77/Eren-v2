#(©) PythonBotz 

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""◇──◇──◇──◇──◇──◇──◇──◇
<blockquote>‣ Mʏ ᴜsᴇʀɴᴀᴍᴇ: <a href='https://t.me/ErenXJaegerbot'>𝙴𝚛𝚎𝚗 𝚈𝚎𝚊𝚐𝚎𝚛</a>\n\n‣ Cʜᴀɴɴᴇʟ I ᴡᴏʀᴋ ғᴏʀ: <a href="https://t.me/Animes_Guy">𝙰𝙶</a> , <a href="https://t.me/Ongoing_AnimeGuy">𝙾𝙰𝙶</a>, <a href="https://t.me/TNXAnimes">𝚃𝙽𝚇</a>\n\n‣ Cʀᴇᴀᴛᴏʀ ᴏғ ᴍᴇ: <a href='https://t.me/The_TGguy'>𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝙶𝚞𝚢!!</a>\n\n‣ Dᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/'>𝙼𝚘𝚗𝚐𝚘 𝙳𝙱</a>\n\n‣ Pʀᴏɢʀᴀᴍᴍᴇᴅ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/'>𝙿𝚢𝚝𝚑𝚘𝚗</a>\n\n‣ Hᴏsᴛᴇᴅ Oɴ: <a href='https://www.heroku.com/'>𝙷𝚎𝚛𝚘𝚔𝚞</a>"</blockquote>
◇──◇──◇──◇──◇──◇──◇──◇""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [ [ InlineKeyboardButton("𝑨𝒏𝒊𝒎𝒆𝒔 𝑮𝒖𝒚!!", url = "https://t.me/Animes_Guy"),
                  InlineKeyboardButton("𝑻𝑵𝑿𝑨𝑵𝑰𝑴𝑬𝑺" , url = "https://t.me/TNXAnimes")],
                 [InlineKeyboardButton("𝑶𝒏𝒈𝒐𝒊𝒏𝒈 𝑨𝒏𝒊𝒎𝒆𝒔 𝑮𝒖𝒚!!", url = "https://t.me/Ongoing_AnimeGuy")],
                    [
                        InlineKeyboardButton("🔙 ʙᴀᴄᴋ ", callback_data = "home"),
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
       

        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "main":
        await query.message.edit_text(
            text=f"<blockquote>ʜᴇʟʟᴏ ᴍʏ ᴜsᴇʀs ᴍʏ ᴜᴘᴅᴀᴛᴇ & ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.</blockquote>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("𝑻𝑵𝑿𝑨𝑵𝑰𝑴𝑬𝑺", url="https://t.me/TNXAnimes"),
                        InlineKeyboardButton("𝑨𝒏𝒊𝒎𝒆𝒔 𝑮𝒖𝒚!!",url = "https://t.me/Animes_Guy")
                    ],
                    [   InlineKeyboardButton("🔙 ʙᴀᴄᴋ ", callback_data = "home"), 
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    elif data == "home":
        await query.message.edit_text(
            text=f"<b><blockquote>ʜᴇʏ !! {query.from_user.mention}\n\nɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton("🤖 ᴀʙᴏᴜᴛ ᴍᴇ", callback_data = "about")
                ]
            ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    
    elif data == "me":
            await query.message.edit(
                text=f"<b>ᴛʜɪs sᴇᴄᴛɪᴏɴ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs & ᴅᴇᴠᴇʟᴏᴘᴇʀ</b>",
                disable_web_page_preview=True,
                reply_markup = InlineKeyboardMarkup(
                    [
                        [  InlineKeyboardButton("𝑨𝒏𝒊𝒎𝒆𝒔 𝑮𝒖𝒚!!",url= "https://t.me/Animes_Guy"),
                         InlineKeyboardButton("𝑻𝑵𝑿𝑨𝑵𝑰𝑴𝑬𝑺",url = "https://t.me/TNXAnimes")],
                        [ InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data = "home"),
                         InlineKeyboardButton( "🚫 ᴄʟᴏsᴇ", callback_data = "close")]
                    ]
                )
         )

    elif data == "source":
        await query.message.edit_text(
            text=f"<b><blockquote>ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ\nɪɴ ᴛᴡᴏ ᴡᴀʏs\n★ <a herf='https://publicearn.com/GitHub'>ɢɪᴛʜᴜʙ</a> \n★ <a herf='https://t.me/+Yy9O2e_eJwU3NjRl'>ᴢɪᴘ ғɪʟᴇ </a></blockquote></b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("𝑻𝑵𝑿𝑨𝑵𝑰𝑴𝑬𝑺",url="https://t.me/TNXAnimes")
                    ],
                    [   InlineKeyboardButton("🔙 ʙᴀᴄᴋ" , callback_data = "home"),
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
