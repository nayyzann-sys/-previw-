import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

CONTACT_USERNAME = "@naywww01"

# Start နှိပ်ရင် ပေါ်မည့် Channel Photo ၏ Telegram File ID
CHANNEL_PHOTO_ID = "AgACAgUAAxkBAAEgueJqYFrWN-knIvOwmsOQ859SgDB3eQACUxVrG9u7CFdtu8B_Lb_nPQEAAwIAA3gAAz0E"

async def set_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "ဇာတ်ကားများ ကြည့်ရန် /start နှိပ်ပါ")
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 The Flash (2014) season 1 to 9", callback_data="m1")],
        [InlineKeyboardButton("🎬 Lucifer (2016) season 1 to 6", callback_data="m2")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
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
    except Exception as e:
        print(f"Start Error: {e}")

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
                caption=(
                    "📌 **The Flash (2014)**\n"
                    "📺 **Season 1 to 9**\n\n"
                    "• ပို့ပေးသော ဗီဒီယိုများသည် **(၁၂) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်။\n"
                    "• ဗီဒီယိုများ ပျက်သွားပါက သို့မဟုတ် အချိန်မရွေး ထပ်မံကြည့်ချင်ပါက **/start** ကို ပြန်နှိပ်ပြီး အသစ်ပြန်ယူ ကြည့်ရှုနိုင်ပါသည်။"
                ),
                parse_mode="Markdown"
            )

            videos_m1 = [
                ("BAACAgUAAxkBAAEgubBqYFc8zCBAF0q4TGoZwX3xHLSX1AACJB4AAoXLgVRxAUNrR-eL_z0E", "🎬 The Flash (2014) - Season 1 to 6 | အပိုင်း (၁)"),
                ("BAACAgUAAxkBAAEgullqYGxRVOwVCisP1T14wkwpTeDrAwACJR4AAoXLgVSvbOSV-SlXHD0E", "🎬 The Flash (2014) - Season 1 to 6 | အပိုင်း (၂)"),
                ("BAACAgUAAxkBAAEguqtqYH1JKVaAc4r3m1D_TSEGpRLRrQACJh4AAoXLgVTZ9Tnit771Sz0E", "🎬 The Flash (2014) - Season 1 to 6 | အပိုင်း (၃)"),
                ("BAACAgUAAxkBAAEguqxqYH1JCxkERguduVwRuf7HDAb2-gACKx4AAoXLgVRTok4Dly278z0E", "🎬 The Flash (2014) - Season 1 to 6 | အပိုင်း (၄)"),
                ("BAACAgUAAxkBAAEguq1qYH1JMSEgt1ePqSHRuT58A0J94wAC1yMAAlnEeFT7fXUpjRcYMD0E", "🎬 The Flash (2014) - Season 1 to 6 | အပိုင်း (၅)"),
                ("BAACAgUAAxkBAAEguq1qYH1JMSEgt1ePqSHRuT58A0J94wAC1yMAAlnEeFT7fXUpjRcYMD0E", "🎬 The Flash (2014) - Season 1 to 6 | အပိုင်း (၆)"),
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
            movie_poster_2 = "AgACAgUAAxkBAAEguktqYGtKcwc5Lz0a-uvM011zR6ouQQACrBJrG-62aFXF-kV2rfK7_gEAAwIAA3cAAz0E"
            
            await context.bot.send_photo(
                chat_id=query.message.chat_id,
                photo=movie_poster_2,
                caption=(
                    "📌 **Lucifer (2016)**\n"
                    "📺 **Season 1 to 6**\n\n"
                    "• ပို့ပေးသော ဗီဒီယိုများသည် **(၁၂) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်။\n"
                    "• ဗီဒီယိုများ ပျက်သွားပါက သို့မဟုတ် အချိန်မရွေး ထပ်မံကြည့်ချင်ပါက **/start** ကို ပြန်နှိပ်ပြီး အသစ်ပြန်ယူ ကြည့်ရှုနိုင်ပါသည်။"
                ),
                parse_mode="Markdown"
            )

            videos_m2 = [
                ("BAACAgUAAxkBAAEgusVqYH9ML8Wz_1g885Oau3MBQAZ5dgACGxkAAlnEgFQsmJuyY9nHzD0E", "🎬 Lucifer (2016) - Season 1 to 9 | အပိုင်း (၁)"),
                ("BAACAgUAAxkBAAEgusdqYH-Se21TwLwEDW3wExwMEhJP9gACBxoAAlnEgFSGD6a-ep3_wj0E", "🎬 Lucifer (2016) - Season 1 to 9 | အပိုင်း (၂)"),
                ("BAACAgUAAxkBAAEgus1qYH_dvXVp2vP9ZAZ1WyIDxtFyHQACWhkAAlnEgFQxHsouPRWm1D0E", "🎬 Lucifer (2016) - Season 1 to 9 | အပိုင်း (၃)"),
                ("BAACAgUAAxkBAAEgutNqYIAQ1YVOgrqS4AzuR1Pe54iYKgACZhkAAlnEgFRDkdzKuTv3xT0E", "🎬 Lucifer (2016) - Season 1 to 9 | အပိုင်း (၄)"),
                ("BAACAgUAAxkBAAEgutVqYICU0yb2rG2-ux8vEEgAAeO5IrgAApYZAAJZxIBULyCSzraSoIM9BA", "🎬 Lucifer (2016) - Season 1 to 9 | အပိုင်း (၅)"),
                ("BAACAgUAAxkBAAEgutdqYIDNUzAzxQdGBqkH5AM0-gQIkAACnhkAAlnEgFSZ92iCDLoVuj0E", "🎬 Lucifer (2016) - Season 1 to 9 | အပိုင်း (၆)"),
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
    
    async def post_init(app):
        await set_commands(app)
        print("Bot is ready and running smoothly!")

    application.post_init = post_init
    
    # ဤနေရာတွင် drop_pending_updates=False ကို သုံးထားပေးပါသည်
    application.run_polling(drop_pending_updates=False)
