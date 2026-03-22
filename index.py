import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ضع التوكن الخاص بك هنا
TOKEN = "7963817662:AAEzdlPpa78KtKOtEtYYQZ8s8eZwu8toH-I"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبًا بك في خدمة عملاء متجرنا!\n"
        "أنا بوت آلي لمساعدتك. استخدم /help لعرض الأوامر المتاحة."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "الأوامر المتاحة:\n"
        "/start - بدء التفاعل\n"
        "/help - عرض هذه المساعدة\n"
        "/order - متابعة طلب\n"
        "/faq - الأسئلة الشائعة\n"
        "/contact - التواصل مع الدعم البشري"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("البوت يعمل...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
