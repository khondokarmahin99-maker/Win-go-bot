import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔮 Get Wingo Prediction", callback_data='predict')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 Welcome to Win Go Signal Bot!\n\nClick the button below to get the next prediction.",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'predict':
        colors = ['🔴 RED', '🟢 GREEN', '🟣 VIOLET']
        sizes = ['BIG', 'SMALL']
        
        predicted_color = random.choice(colors)
        predicted_size = random.choice(sizes)
        predicted_number = random.randint(0, 9)

        result_text = (
            "🎯 **WIN GO PREDICTION** 🎯\n\n"
            f"🎨 **Color:** {predicted_color}\n"
            f"📊 **Size:** {predicted_size}\n"
            f"🔢 **Number:** {predicted_number}\n\n"
            "⚠️ *Note: Predictions are generated automatically.*"
        )

        keyboard = [
            [InlineKeyboardButton("🔄 Next Prediction", callback_data='predict')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text=result_text, parse_mode='Markdown', reply_markup=reply_markup)

def main():
    if not TOKEN:
        print("Error: TOKEN is missing!")
        return
    
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
