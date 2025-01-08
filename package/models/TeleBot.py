import asyncio

from typing import Final
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, CallbackContext, Updater, filters


BOT_TOKEN: Final = "7568273101:AAH5h0BUJ_dKI-0TIF63HVAGAzITYp9-f1I"
BOT_USERNAME: Final = "@MiniVit_bot"

class TeleBot():

	def __init__(self):
		self.bot = Bot(token=BOT_TOKEN)
	
	async def speak(self, message, chatid):
		await self.bot.send_message(chat_id = chatid, text=message)
	
	async def save_chatid(self):
		update = await self.bot.getUpdates(-1, 1, 100)
		
		print(f'\n"{update[0].message.text}" was sent by ({update[0].message.chat_id})')
		
		return update[0].message.chat_id
		

