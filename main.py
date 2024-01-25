import wikipedia
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
wikipedia.set_lang('uz')

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
	foydalanuvchi=update.message.from_user
	await update.message.reply_html('<b>Assalomu alaykum \n<i>'+foydalanuvchi.first_name+'</i>\nXush kelibsiz\n Botdan foydalanish uchun shunchaki\n qidirayotgan ma`lumotingizni kriting</b>')

async def wiki(update:Update, context:ContextTypes.DEFAULT_TYPE):
	try:
		res=wikipedia.summary(update.message.text)
		await update.message.reply_text(res)
	except:
		await update.message.reply_text('Xato😔, Wikipediadan bunday ma`lumot topa olmadim. Uzur😭')

bot = Application.builder().token("6708071280:AAEXrTAcDJwoWEwau1cffsqoY-TLzO5Jmqk").build()
bot.add_handler(CommandHandler('start',start))
bot.add_handler(MessageHandler(filters.TEXT&~filters.COMMAND ,wiki))
bot.run_polling(allowed_updates=Update.ALL_TYPES)	