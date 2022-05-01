from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    buttons = [
            [InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about")],
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=client.invitelink4),
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=client.invitelink5),
            ],
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=client.invitelink6),
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]


def fsub_button(client, message):
    buttons = [
        [
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=client.invitelink3),
        ],
        [
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=client.invitelink4),
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=client.invitelink5),
        ],
        [
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=client.invitelink6),
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=client.invitelink2),
        ],
        [
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close"),
        ],
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text="ᴄᴏʙᴀ ʟᴀɢɪ",
                    url=f"https://t.me/{client.username}?start={message.command[1]}",
                )
            ]
        )
    except IndexError:
        pass