import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

CONTACT_USERNAME = "naywww01"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Start နှိပ်တာနဲ့ ဇာတ်ကား ၁ ကား (The Flash) ပေါ်လာမည်
    keyboard = [
        [InlineKeyboardButton("🎬 The Flash (2014) season 1 to 9", callback_data="m1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "✨ *ကြိုဆိုပါတယ်ခင်ဗျာ!*\nအောက်ပါဇာတ်ကားကို နှိပ်၍ အပိုင်းများကို ရွေးချယ်နိုင်ပါသည် -",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    try:
        if data == "m1":
            # ဇာတ်ကား ၁ ကားကို နှိပ်လိုက်ရင် အပိုင်း ၆ ပိုင်း ကျလာမည်
            # (ကိုယ့်ရဲ့ ဗီဒီယို File ID များကို BQAC... နေရာတွင် ထည့်ပေးပါ)
            videos_m1 = [
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - အပိုင်း (၁)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - အပိုင်း (၂)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - အပိုင်း (၃)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - အပိုင်း (၄)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - အပိုင်း (၅)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - အပိုင်း (၆)"),
            ]

            for vid, cap in videos_m1:
                await context.bot.send_video(
                    chat_id=query.message.chat_id, 
                    video=vid, 
                    caption=cap
                )

            # အပိုင်း ၇ နှင့်အထက်အတွက် မန်ဘာဝင်ရန် ဆက်သွယ်ရန် (၂၀၀၀ ကျပ်)
            keyboard = [
                [InlineKeyboardButton("💬 မန်ဘာဝင်ရန် ဆက်သွယ်ရန် (၂၀၀၀ ကျပ်)", url=f"https://t.me/{CONTACT_USERNAME}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text=(
                    "🔒 *အပိုင်း ၇ နှင့်အထက် ကြည့်ရှုရန်*\n\n"
                    "⚠️ အပိုင်း ၇ နှင့်အထက် ဆက်လက်ကြည့်ရှုလိုပါက VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။\n"
                    "💰 မန်ဘာကြေး - *၂,၀၀၀ ကျပ်* ဖြစ်ပါသည်။\n\n"
                    "မန်ဘာဝင်လိုပါက အောက်ပါခလုတ်ကို နှိပ်၍ ဆက်သွယ်နိုင်ပါသည် -"
                ),
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )
            
    except Exception as e:
        await query.message.reply_text(f"⚠️ Error: {str(e)}")

if __name__ == '__main__':
    TOKEN = "8935742099:AAF8HZBWbZLu4fh10TufidZ83TlnBHygVbE"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    application.run_polling(drop_pending_updates=True)
    
