from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "7526489061:AAHehYvu9nJWIAec9xEr0W2EHEjZPAc3ZLs"

async def start(update: Update, context):
    await update.message.reply_text("Selam! Sana nasıl yardımcı olabilirim?")

async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot çalışıyor...")
app.run_polling()
