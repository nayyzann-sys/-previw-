import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

CONTACT_USERNAME = "@naywww01"

# Start နှိပ်ရင် ပေါ်မည့် Channel Photo ၏ Telegram File ID ကို ဤနေရာတွင် ထည့်ပါ
CHANNEL_PHOTO_ID = "यहाँ_Channel_Photo_၏_File_ID_ထည့်ပါ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 The Flash (2014)", callback_data="m1")],
        [InlineKeyboardButton("🎬 ဇာတ်ကားအသစ် အမည်", callback_data="m2")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Start နှိပ်လျှင် Channel Photo နှင့်အတူ ကြိုဆိုစာသား ပို့ပေးမည်
    sent_msg = await update.message.reply_photo(
        photo=CHANNEL_PHOTO_ID,
        caption=(
            "✨ **ကြိုဆိုပါတယ်ခင်ဗျာ!**\n"
            "အောက်ပါ ဇာတ်ကားများကို နှိပ်၍ အပိုင်းများကို ရွေးချယ်နိုင်ပါသည် -\n\n"
            "⚠️ *မှတ်ချက် - ဤမက်ဆေ့ချ်သည် ၁၀ မိနစ်ကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။ လင့်ခ်ပျက်သွားပါက သို့မဟုတ် အချိန်မရွေး ကြည့်ချင်ပါက /start ဖြင့် အလွယ်တကူ ပြန်ယူနိုင်ပါသည်။*"
        ),
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
            movie_poster_1 = "यहाँ_The_Flash_ပိုစတာ_File_ID_ထည့်ပါ"
            
            await context.bot.send_photo(
                chat_id=query.message.chat_id,
                photo=movie_poster_1,
                caption=(
                    "📌 **The Flash (2014)**\n"
                    "📺 **Season 1 to 6**\n\n"
                    "• ပို့ပေးသော ဗီဒီယိုများသည် **(၁၂) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်။\n"
                    "• ဗီဒီယိုများ ပျက်သွားပါက သို့မဟုတ် အချိန်မရွေး ထပ်မံကြည့်ချင်ပါက **/start** ကို ပြန်နှိပ်ပြီး အသစ်ပြန်ယူ ကြည့်ရှုနိုင်ပါသည်။"
                ),
                parse_mode="Markdown"
            )

            videos_m1 = [
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - Season 1 to 6 | အပိုင်း (၁)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - Season 1 to 6 | အပိုင်း (၂)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - Season 1 to 6 | အပိုင်း (၃)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - Season 1 to 6 | အပိုင်း (၄)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - Season 1 to 6 | အပိုင်း (၅)"),
                ("BQACAgUAAxkBAAI...", "🎬 The Flash (2014) - Season 1 to 6 | အပိုင်း (၆)"),
            ]

            for vid, cap in videos_m1:
                msg = await context.bot.send_video(
                    chat_id=query.message.chat_id, 
                    video=vid, 
                    caption=f"{cap}\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက ပျက်သွားပါမည်။ (အချိန်မရွေး /start ပြန်နှိပ်ပြီး ကြည့်နိုင်သည်)"
                )
                schedule_deletion(context, msg)

            keyboard = [
                [InlineKeyboardButton("💬 မန်ဘာဝင်ရန် ဆက်သွယ်ရန် (၂၀၀၀ ကျပ်)", url=f"https://t.me/{CONTACT_USERNAME.replace('@', '')}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text=(
                    "🔒 **ကျန်အပိုင်းများ ကြည့်ရှုရန်**\n\n"
                    "⚠️ အပိုင်း ၇ နှင့်အထက် ကျန်ရှိသော အပိုင်းများကို ဆက်လက်ကြည့်ရှုလိုပါက VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။\n"
                    "💰 မန်ဘာကြေး - **၂,၀၀၀ ကျပ်** ဖြစ်ပါသည်။\n\n"
                    "မန်ဘာဝင်လိုပါက အောက်ပါခလုတ်ကို နှိပ်၍ ဆက်သွယ်နိုင်ပါသည် -"
                ),
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )

        elif data == "m2":
            movie_poster_2 = "यहाँ_ဇာတ်ကားအသစ်_ပိုစတာ_File_ID_ထည့်ပါ"
            
            await context.bot.send_photo(
                chat_id=query.message.chat_id,
                photo=movie_poster_2,
                caption=(
                    "📌 **ဇာတ်ကားအသစ် အမည်**\n"
                    "📺 **Season 1 to 9**\n\n"
                    "• ပို့ပေးသော ဗီဒီယိုများသည် **(၁၂) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်။\n"
                    "• ဗီဒီယိုများ ပျက်သွားပါက သို့မဟုတ် အချိန်မရွေး ထပ်မံကြည့်ချင်ပါက **/start** ကို ပြန်နှိပ်ပြီး အသစ်ပြန်ယူ ကြည့်ရှုနိုင်ပါသည်။"
                ),
                parse_mode="Markdown"
            )

            videos_m2 = [
                ("BQACAgUAAxkBAAI...", "🎬 ဇာတ်ကားအသစ် - Season 1 to 9 | အပိုင်း (၁)"),
                ("BQACAgUAAxkBAAI...", "🎬 ဇာတ်ကားအသစ် - Season 1 to 9 | အပိုင်း (၂)"),
                ("BQACAgUAAxkBAAI...", "🎬 ဇာတ်ကားအသစ် - Season 1 to 9 | အပိုင်း (၃)"),
                ("BQACAgUAAxkBAAI...", "🎬 ဇာတ်ကားအသစ် - Season 1 to 9 | အပိုင်း (၄)"),
                ("BQACAgUAAxkBAAI...", "🎬 ဇာတ်ကားအသစ် - Season 1 to 9 | အပိုင်း (၅)"),
                ("BQACAgUAAxkBAAI...", "🎬 ဇာတ်ကားအသစ် - Season 1 to 9 | အပိုင်း (၆)"),
            ]

            for vid, cap in videos_m2:
                msg = await context.bot.send_video(
                    chat_id=query.message.chat_id, 
                    video=vid, 
                    caption=f"{cap}\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက ပျက်သွားပါမည်။ (အချိန်မရွေး /start ပြန်နှိပ်ပြီး ကြည့်နိုင်သည်)"
                )
                schedule_deletion(context, msg)

            keyboard = [
                [InlineKeyboardButton("💬 မန်ဘာဝင်ရန် ဆက်သွယ်ရန် (၂၀၀၀ ကျပ်)", url=f"https://t.me/{CONTACT_USERNAME.replace('@', '')}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text=(
                    "🔒 **ကျန်အပိုင်းများ ကြည့်ရှုရန်**\n\n"
                    "⚠️ အပိုင်း ၇ နှင့်အထက် ကျန်ရှိသော အပိုင်းများကို ဆက်လက်ကြည့်ရှုလိုပါက VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။\n"
                    "💰 မန်ဘာကြေး - **၂,၀၀၀ ကျပ်** ဖြစ်ပါသည်။\n\n"
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
    print("Bot is running with Channel Photo...")
    application.run_polling(drop_pending_updates=True)
            
