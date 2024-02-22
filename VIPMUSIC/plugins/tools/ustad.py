from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VIPMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("owner")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/403d1431dd35d74d6fcad.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ OWNER 🗡️", url=f"https://t.me/SaqibADM")
                ],
                [InlineKeyboardButton(
                        "🗡️ UPDATES 🗡️", url=f"https://t.me/LineWord122")
            ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/403d1431dd35d74d6fcad.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ OWNER 🗡️", url=f"https://t.me/SaqibADM")
                ],
                [InlineKeyboardButton(
                        "🗡️ UPDATES 🗡️", url=f"https://t.me/LineWord122")
            ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/403d1431dd35d74d6fcad.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ UPDATES 🗡️", url=f"https://t.me/LineWord122")
                ],
                [InlineKeyboardButton(
                        "🗡️ OWNER 🗡️", url=f"https://t.me/SaqibADM")
            ]
            ]
        ),
    )
