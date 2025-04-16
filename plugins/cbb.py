#(©)Yugen_Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, HELP_MSG, OWNER
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        abt_msg = "<b><blockquote>◈sᴜᴘʀᴇᴀᴍ: <a href=https://t.me/Stelleron_Hunter>sᴛᴇʟʟᴇʀᴏɴ</a>\n◈ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Anime_Eternals>ᴇᴛᴇʀɴᴀʟs</a>\n◈ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢs : <a href=https://t.me/+VxWwaMA6g_JkNTA9>ᴏɴɢᴏɪɴɢ</a>\n◈ᴇᴄᴄʜɪ ᴅᴇx : <a href=https://t.me/Ecchi_Dex>ᴇᴄᴄʜɪ</a>\n◈ʜᴇʟᴘʟɪɴᴇ : <a href=https://t.me/EternalsHelplineBot>ʜᴇʟᴘʟɪɴᴇ</a></blockquote></b>"
        ABOUT_TXT = abt_msg.format(mention=query.from_user.mention)
        await query.message.edit_text(
            text = ABOUT_TXT,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    
                    [
                    InlineKeyboardButton("😔 ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "help":
        await query.message.edit_text(
            text = HELP_MSG,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("😔 ᴄʟᴏsᴇ", callback_data = "close")
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


