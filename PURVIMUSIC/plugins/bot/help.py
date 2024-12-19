import re
from typing import Union
from pyrogram import Client, filters, types
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton, CallbackQuery
from PURVIMUSIC import app
from PURVIMUSIC.utils import help_pannel
from PURVIMUSIC.utils.database import get_lang 
from PURVIMUSIC.utils.decorators.language import LanguageStart, languageCB
from PURVIMUSIC.utils.inline.help import help_back_markup, private_help_panel
import config
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers
from PURVIMUSIC.utils.stuffs.buttons import BUTTONS
from PURVIMUSIC.utils.stuffs.helper import Helper

@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=keyboard)
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboard)
        
        
@app.on_callback_query(filters.regex("feature"))
async def feature_callback(client: Client, callback_query: CallbackQuery):
    keyboard = [
        [
            InlineKeyboardButton(
                text="⚜️ ᴋɪᴅɴᴀᴘ ᴍᴇ ɪɴ ɴᴇᴡ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ ⚜️",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="ᴍᴜsɪᴄ", callback_data="music"),
            InlineKeyboardButton(text="ᴍᴀɴᴀɢᴇᴍᴇɴᴛ", callback_data="management"),
        ],
        [
            InlineKeyboardButton(text="ᴛᴏᴏʟs", callback_data="tools"),
            InlineKeyboardButton(text="ᴀʟʟ", callback_data="settings_back_helper"),
        ],
        [InlineKeyboardButton(text="✯ ʜᴏᴍᴇ ✯", callback_data="go_to_start")],
    ]
    k = f"""**❖ ᴛʜɪs ɪs {app.mention} ! 

━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━━
❖ ᴛʜɪs ɪs ᴄʜᴀᴛ | ᴍᴀɴᴀɢᴇᴍᴇɴᴛ | ᴍυsɪᴄ ʙσᴛ
❖ ɴᴏ ʟᴧɢ | ᴧᴅs ᴍυsɪᴄ | ɴᴏ ᴘʀᴏᴍᴏ
❖ 24x7 ʀυɴ | ʙєsᴛ sᴏυɴᴅ ǫυᴧʟɪᴛʏ
━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━━
❖ ᴄʟɪᴄᴋ ᴏɴ ᴛʜє ʜєʟᴩ ʙυᴛᴛᴏɴ ᴛᴏ ɢєᴛ ɪɴғᴏ
    ᴧʙσυᴛ ᴍʏ ᴍᴏᴅυʟєs ᴧɴᴅ ᴄᴏᴍᴍᴧɴᴅs...!
━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━━**"""
    await callback_query.message.edit_text(
        text=k, reply_markup=InlineKeyboardMarkup(keyboard)
    )


@app.on_callback_query(filters.regex("music"))
async def music_callback(client: Client, callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Aᴅᴍɪɴ", callback_data="music_callback hb1"),
                InlineKeyboardButton(text="Aᴜᴛʜ", callback_data="music_callback hb2"),
                InlineKeyboardButton(
                    text="Bʀᴏᴀᴅᴄᴀsᴛ", callback_data="music_callback hb3"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Bʟ-Cʜᴀᴛ", callback_data="music_callback hb4"
                ),
                InlineKeyboardButton(
                    text="Bʟ-Usᴇʀ", callback_data="music_callback hb5"
                ),
                InlineKeyboardButton(text="C-Pʟᴀʏ", callback_data="music_callback hb6"),
            ],
            [
                InlineKeyboardButton(text="G-Bᴀɴ", callback_data="music_callback hb7"),
                InlineKeyboardButton(text="Lᴏᴏᴘ", callback_data="music_callback hb8"),
                InlineKeyboardButton(
                    text="Mᴀɪɴᴛᴇɴᴀɴᴄᴇ", callback_data="music_callback hb9"
                ),
            ],
            [
                InlineKeyboardButton(text="Pɪɴɢ", callback_data="music_callback hb10"),
                InlineKeyboardButton(text="Pʟᴀʏ", callback_data="music_callback hb11"),
                InlineKeyboardButton(
                    text="Sʜᴜғғʟᴇ", callback_data="music_callback hb12"
                ),
            ],
            [
                InlineKeyboardButton(text="Sᴇᴇᴋ", callback_data="music_callback hb13"),
                InlineKeyboardButton(text="Sᴏɴɢ", callback_data="music_callback hb14"),
                InlineKeyboardButton(text="Sᴘᴇᴇᴅ", callback_data="music_callback hb15"),
            ],
            [InlineKeyboardButton(text="✯ ʙᴀᴄᴋ ✯", callback_data=f"feature")],
        ]
    )

    await callback_query.message.edit(
        f"``**Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.](t.me/tg_friendsss)**\n\n**Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**``",
        reply_markup=keyboard,
    )


@app.on_callback_query(filters.regex("management"))
async def management_callback(client: Client, callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="єxᴛʀᴧ", callback_data="management_callback extra"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ʙᴧη", callback_data="management_callback hb1"
                ),
                InlineKeyboardButton(
                    text="ᴋɪᴄᴋs", callback_data="management_callback hb2"
                ),
                InlineKeyboardButton(
                    text="ϻυᴛє", callback_data="management_callback hb3"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴘɪη", callback_data="management_callback hb4"
                ),
                InlineKeyboardButton(
                    text="sᴛᴧғғ", callback_data="management_callback hb5"
                ),
                InlineKeyboardButton(
                    text="sєᴛ υᴘ", callback_data="management_callback hb6"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="zσϻʙɪє", callback_data="management_callback hb7"
                ),
                InlineKeyboardButton(
                    text="ɢᴧϻє", callback_data="management_callback hb8"
                ),
                InlineKeyboardButton(
                    text="ɪϻᴘσsᴛєʀ", callback_data="management_callback hb9"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="sᴧηɢ ϻᴧᴛᴧ", callback_data="management_callback hb10"
                ),
                InlineKeyboardButton(
                    text="ᴛʀᴧηsʟᴧᴛє", callback_data="management_callback hb11"
                ),
                InlineKeyboardButton(
                    text="ᴛ-ɢʀᴧᴘʜ", callback_data="management_callback hb12"
                ),
            ],
            [InlineKeyboardButton(text="✯ ʙᴀᴄᴋ ✯", callback_data=f"feature")],
        ]
    )

    await callback_query.message.edit(
        f"``**Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.](t.me/tg_friendsss)**\n\n**Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**``",
        reply_markup=keyboard,
    )


@app.on_callback_query(filters.regex("tools"))
async def tools_callback(client: Client, callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="ᴄʜᴧᴛɢᴘᴛ", callback_data="tools_callback ai")],
            [
                InlineKeyboardButton(text="ɢσσɢʟє", callback_data="tools_callback hb1"),
                InlineKeyboardButton(
                    text="ᴛᴛs-ᴠσɪᴄє", callback_data="tools_callback hb2"
                ),
                InlineKeyboardButton(text="ɪηꜰσ", callback_data="tools_callback hb3"),
            ],
            [
                InlineKeyboardButton(text="ғσηᴛ", callback_data="tools_callback hb4"),
                InlineKeyboardButton(text="ϻᴧᴛʜ", callback_data="tools_callback hb5"),
                InlineKeyboardButton(text="ᴛᴧɢᴧʟʟ", callback_data="tools_callback hb6"),
            ],
            [
                InlineKeyboardButton(text="ɪϻᴧɢє", callback_data="tools_callback hb7"),
                InlineKeyboardButton(text="ʜᴧsᴛᴧɢ", callback_data="tools_callback hb8"),
                InlineKeyboardButton(
                    text="sᴛɪᴄᴋєʀs", callback_data="tools_callback hb9"
                ),
            ],
            [
                InlineKeyboardButton(text="ғυη", callback_data="tools_callback hb10"),
                InlineKeyboardButton(
                    text="ǫυσᴛʟʏ", callback_data="tools_callback hb11"
                ),
                InlineKeyboardButton(
                    text="ᴛʀ - ᴅʜ", callback_data="tools_callback hb12"
                ),
            ],
            [InlineKeyboardButton(text="✯ ʙᴀᴄᴋ ✯", callback_data=f"feature")],
        ]
    )

    await callback_query.message.edit(
        f"``**Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.](t.me/tg_friendsss)**\n\n**Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**``",
        reply_markup=keyboard,
    )


# If the back button has different meanings in various panels, you can set different callbacks
@app.on_callback_query(filters.regex("support"))
async def back_button_callback(client: Client, callback_query: CallbackQuery):
    keyboard = [
        [
            InlineKeyboardButton(text="❍ᴡɴᴇꝛ", user_id=config.OWNER_ID[0]),
            InlineKeyboardButton(
                text="ɢɪᴛʜᴜʙ",
                url="https://t.me/APNA_SYSTEM",
            ),
        ],
        [
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=f"{config.SUPPORT_GROUP}"),
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=f"{config.SUPPORT_CHANNEL}"),
        ],
        [InlineKeyboardButton(text="✯ ʜᴏᴍᴇ ✯", callback_data="go_to_start")],
    ]

    await callback_query.message.edit_text(
        "**๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ**\n\n**ɪғ ʏᴏᴜ ғɪɴᴅ ᴀɴʏ ᴇʀʀᴏʀ ᴏʀ ʙᴜɢ ᴏɴ ʙᴏᴛ ᴏʀ ᴡᴀɴᴛ ᴛᴏ ɢɪᴠᴇ ᴀɴʏ ғᴇᴇᴅʙᴀᴄᴋ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ ᴛʜᴇɴ ʏᴏᴜ ᴀʀᴇ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ  (✿◠‿◠)**",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

