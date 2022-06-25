from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import OWNER_USERNAME

def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Gʀᴏᴜᴘ's Pʟᴀʏʟɪsᴛ",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Pʟᴀʏʟɪsᴛ",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Cʟᴏsᴇ Mᴇɴᴜ", callback_data="close")],
      [
          InlineKeyboardButton(
                text="🕊.⋆Kɪɴɢ⋆",
                url=f"https://t.me/{OWNER_USERNAME}",
            ),
        ],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Gʀᴏᴜᴘ's Pʟᴀʏʟɪsᴛ",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Pʟᴀʏʟɪsᴛ",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Cʟᴏsᴇ Mᴇɴᴜ", callback_data="close")],
      [
          InlineKeyboardButton(
                text="🕊.⋆Kɪɴɢ⋆",
                url=f"https://t.me/{OWNER_USERNAME}",
            ),
        ],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Bᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"play_playlist {user_id}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"Hᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"play_playlist {user_id}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Pᴀʀᴛʏ",
                callback_data=f"play_playlist {user_id}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"Lᴏғɪ",
                callback_data=f"play_playlist {user_id}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Sᴀᴅ",
                callback_data=f"play_playlist {user_id}|{type}|Sad",
            ),
            InlineKeyboardButton(
                text=f"Wᴇᴇʙ",
                callback_data=f"play_playlist {user_id}|{type}|Weeb",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Pᴜɴɪᴀʙɪ",
                callback_data=f"play_playlist {user_id}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"Oᴛʜᴇʀs",
                callback_data=f"play_playlist {user_id}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Bᴀᴄᴋ",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="🗑 Cʟᴏsᴇ Mᴇɴᴜ", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"✚ Wᴇᴇʙ",
                callback_data=f"add_playlist {videoid}|{type}|Weeb",
            ),
            InlineKeyboardButton(
                text=f"✚ Sᴀᴅ",
                callback_data=f"add_playlist {videoid}|{type}|Sad",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ Pᴀʀᴛʏ",
                callback_data=f"add_playlist {videoid}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"✚ Lᴏғɪ",
                callback_data=f"add_playlist {videoid}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ Bᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"add_playlist {videoid}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"✚ Hᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"add_playlist {videoid}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ Pᴜɴɪᴀʙɪ",
                callback_data=f"add_playlist {videoid}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"✚ Oᴛʜᴇʀs",
                callback_data=f"add_playlist {videoid}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Bᴀᴄᴋ", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 Cʟᴏsᴇ Mᴇɴᴜ", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Wᴇᴇʙ", callback_data=f"check_playlist {type}|Weeb"
            ),
            InlineKeyboardButton(
                text=f"Sᴀᴅ", callback_data=f"check_playlist {type}|Sad"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Pᴀʀᴛʏ", callback_data=f"check_playlist {type}|Party"
            ),
            InlineKeyboardButton(
                text=f"Lᴏғɪ", callback_data=f"check_playlist {type}|Lofi"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Bᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"check_playlist {type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"Hᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"check_playlist {type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Pᴜɴɪᴀʙɪ",
                callback_data=f"check_playlist {type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"Oᴛʜᴇʀs", callback_data=f"check_playlist {type}|Others"
            ),
        ],
        [InlineKeyboardButton(text="🗑 Cʟᴏsᴇ Mᴇɴᴜ", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Gʀᴏᴜᴘ's Pʟᴀʏʟɪsᴛ",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Pʟᴀʏʟɪsᴛ",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s Pʟᴀʏʟɪsᴛ",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Cʟᴏsᴇ", callback_data="close")],
      [
          InlineKeyboardButton(
                text="🕊.⋆Kɪɴɢ⋆",
                url=f"https://t.me/{OWNER_USERNAME}",
            ),
        ],
    ]
    return buttons
  


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data=f"pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data=f"skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="Cʜᴇᴄᴋᴏᴜᴛ Qᴜᴇᴜᴇᴅ Pʟᴀʏʟɪsᴛ", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Cʟᴏsᴇ Mᴇɴᴜ", callback_data=f"close")],
      
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="Cʜᴇᴄᴋᴏᴜᴛ Pʟᴀʏʟɪsᴛ", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Cʟᴏsᴇ Mᴇɴᴜ", callback_data=f"close")],
      [
          InlineKeyboardButton(
                text="🕊.⋆Kɪɴɢ⋆",
                url=f"https://t.me/{OWNER_USERNAME}",
            ),
        ],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Yes! Delete",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="No!", callback_data=f"close"),
        ],
      [
          InlineKeyboardButton(
                text="🕊.⋆Kɪɴɢ⋆",
                url=f"https://t.me/{OWNER_USERNAME}",
            ),
        ],
    ]
    return buttons
