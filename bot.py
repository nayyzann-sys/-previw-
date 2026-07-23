import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

CONTACT_USERNAME = "naywww01"
CHANNEL_PHOTO_ID = "AgACAgUAAxkBAAEgueJqYFrWN-knIvOwmsOQ859SgDB3eQACUxVrG9u7CFdtu8B_Lb_nPQEAAwIAA3gAAz0E"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 The Flash (2014) season 1 to 9", callback_data="m1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    sent_msg = await update.message.reply_photo(
        photo=CHANNEL_PHOTO_ID,
        caption="✨ *ကြိုဆိုပါတယ်ခင်ဗျာ!*\nအောက်ပါဇာတ်ကားကို နှိပ်၍ အပိုင်းများကို ရွေးချယ်နိုင်ပါသည် -",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
    schedule_start_deletion(context, sent_msg)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    try:
        if data == "m1":
            movie_poster_1 = "AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3cAAz0E"
            
            await context.bot.send_photo(
                chat_id=query.message.chat_id,
                photo=movie_poster_1,
                caption="📌 *The Flash (2014)*\n📺 *Season 1 to 9*\n\nဗီဒီယိုများကို အောက်တွင် ပို့ပေးလိုက်ပါပြီ -",
                parse_mode="Markdown"
            )

            # အပိုင်း ၆ ပိုင်းသာ ထည့်ထားသည်
            videos_m1 = [
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - အပိုင်း (၁)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - အပိုင်း (၂)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - အပိုင်း (၃)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - အပိုင်း (၄)"),
                ("BQACAgeUAAxkBAAI...", "🎬 The Flash (2014) - အပိုင်း (၅)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - အပိုင်း (၆)"),
            ]

            for vid, cap in videos_m1:
                msg = await context.bot.send_video(
                    chat_id=query.message.chat_id, 
                    video=vid, 
                    caption=f"{cap}\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
                )
                schedule_deletion(context, msg)

            # အပိုင်း ၇ နှင့်အထက်အတွက် မန်ဘာဝင်ရန် ခလုတ်
            keyboard = [
                [InlineKeyboardButton("💬 မန်ဘာဝင်ရန် ဆက်သွယ်ရန် (၂၀၀၀ ကျပ်)", url=f"https://t.me/{CONTACT_USERNAME}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text=(
                    "🔒 *အပိုင်း ၇ နှင့်အထက် ကြည့်ရှုရန်*\n\n"
                    "⚠️ အပိုင်း ၇ နှင့်အထက် ဆက်လက်ကြည့်ရှုလိုပါက VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။\n"
                    "💰 မန်ဘာကြေး - *၂,၀၀0 ကျပ်* ဖြစ်ပါသည်။\n\n"
                    "မန်ဘာဝင်လိုပါက အောက်ပါခလုတ်ကို နှိပ်၍ ဆက်သွယ်နိုင်ပါသည် -"
                ),
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )
            
    except Exception as e:
        await query.message.reply_text(f"⚠️ Error: {str(e)}")

def schedule_start_deletion(context, sent_msg):
    async def delete_start_msg():
        await asyncio.sleep(600)
        try:
            await context.bot.delete_message(chat_id=sent_msg.chat_id, message_id=sent_msg.message_id)
        except Exception:
            pass
    context.application.create_task(delete_start_msg())

def schedule_deletion(context, sent_msg):
    async def delete_msg():
        await asyncio.sleep(43200)
        try:
            await context.bot.delete_message(chat_id=sent_msg.chat_id, message_id=sent_msg.message_id)
        except Exception:
            pass
    context.application.create_task(delete_msg())

if __name__ == '__main__':
    TOKEN = "8935742099:AAF8HZBWbZLu4fh10TufidZ83TlnBHygVbE"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    application.run_polling(drop_pending_updates=True)
            
