import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

CONTACT_USERNAME = "@naywww01"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 The Flash (2014) season 1 to 9", callback_data="m1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # ပုံ့ File ID အမှန်ကို ထည့်သွင်းပြီးပါပြီ
    sent_msg = await context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo="AgACAgUAAxkBAAEgueJqYFrWN-knIvOwmsOQ859SgDB3eQACUxVrG9u7CFdtu8B_Lb_nPQEAAwIAA3gAAz0E",
        caption=(
            "✨ **ကြိုဆိုပါတယ်ခင်ဗျာ!**\n"
            "အောက်ပါ ဇာတ်ကားခလုတ်ကို နှိပ်၍ အပိုင်းများကို ရွေးချယ်နိုင်ပါသည် -\n\n"
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
            # 📌 ဇာတ်ကားပိုစတာနှင့် Season အချက်အလက်
            poster_msg = await context.bot.send_photo(
                chat_id=query.message.chat_id,
                photo="AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3cAAz0E",
                caption=(
                    "📌 **The Flash (2014)**\n"
                    "📺 **Season:** 1 to 9 (Season ၉ ခုထိ ရှိပါတယ်)\n\n"
                    "• အပိုင်း (၁) မှ (၆) အထိ အလကား (Free) ကြည့်ရှုနိုင်ပါသည်။\n"
                    "• ပို့ပေးသော ပုံများနှင့် ဗီဒီယိုများသည် **(၁၂) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်။\n"
                    "• ပျက်သွားပါက သို့မဟုတ် အချိန်မရွေး ထပ်မံကြည့်ရှုချင်ပါက **/start** ကို ပြန်နှိပ်ပြီး အသစ်ပြန်ယူ ကြည့်ရှုနိုင်ပါသည်။"
                ),
                parse_mode="Markdown"
            )
            schedule_deletion(context, poster_msg)

            # 🎬 ဗီဒီယို အပိုင်း (၁) မှ (၆) အထိ ဖိုင်အိုင်ဒီများ
            msg1 = await context.bot.send_video(chat_id=query.message.chat_id, video="BAACAgUAAxkBAAEgubBqYFc8zCBAF0q4TGoZwX3xHLSX1AACJB4AAoXLgVRxAUNrR-eL_z0E", caption="🎬 The Flash (2014) - အပိုင်း (၁)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက ပျက်သွားပါမည်။")
            msg2 = await context.bot.send_video(chat_id=query.message.chat_id, video="BAACAgUAAxkBAAEgullqYGxRVOwVCisP1T14wkwpTeDrAwACJR4AAoXLgVSvbOSV-SlXHD0E", caption="🎬 The Flash (2014) - အပိုင်း (၂)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက ပျက်သွားပါမည်။")
            msg3 = await context.bot.send_video(chat_id=query.message.chat_id, video="BAACAgUAAxkBAAEguqtqYH1JKVaAc4r3m1D_TSEGpRLRrQACJh4AAoXLgVTZ9Tnit771Sz0E", caption="🎬 The Flash (2014) - အပိုင်း (၃)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက ပျက်သွားပါမည်။")
            msg4 = await context.bot.send_video(chat_id=query.message.chat_id, video="BAACAgUAAxkBAAEguqxqYH1JCxkERguduVwRuf7HDAb2-gACKx4AAoXLgVRTok4Dly278z0E", caption="🎬 The Flash (2014) - အပိုင်း (၄)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက ပျက်သွားပါမည်။")
            msg5 = await context.bot.send_video(chat_id=query.message.chat_id, video="BAACAgUAAxkBAAEguq1qYH1JMSEgt1ePqSHRuT58A0J94wAC1yMAAlnEeFT7fXUpjRcYMD0E", caption="🎬 The Flash (2014) - အပိုင်း (၅)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက ပျက်သွားပါမည်။")
            msg6 = await context.bot.send_video(chat_id=query.message.chat_id, video="BAACAgUAAxkBAAEguq1qYH1JMSEgt1ePqSHRuT58A0J94wAC1yMAAlnEeFT7fXUpjRcYMD0E", caption="🎬 The Flash (2014) - အပိုင်း (၆)\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက ပျက်သွားပါမည်။")

            schedule_deletion(context, msg1)
            schedule_deletion(context, msg2)
            schedule_deletion(context, msg3)
            schedule_deletion(context, msg4)
            schedule_deletion(context, msg5)
            schedule_deletion(context, msg6)

            # 🔒 VIP မန်ဘာဝင်ရန် ဆက်သွယ်ရန် ခလုတ်
            keyboard = [
                [InlineKeyboardButton("💬 မန်ဘာဝင်ရန် ဆက်သွယ်ရန် (၂၀၀၀ ကျပ်)", url=f"https://t.me/{CONTACT_USERNAME.replace('@', '')}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            vip_msg = await context.bot.send_message(
                chat_id=query.message.chat_id,
                text=(
                    "🔒 **VIP အပိုင်းများ (အပိုင်း ၇ နှင့်အထက်)**\n\n"
                    "⚠️ ဤ အပိုင်းများကို ကြည့်ရှုရန်အတွက် VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။\n"
                    "💰 မန်ဘာကြေး - **၂,၀၀၀ ကျပ်** ဖြစ်ပါသည်။\n\n"
                    "မန်ဘာဝင်လိုပါက အောက်ပါခလုတ်ကို နှိပ်၍ Owner ထံသို့ ဆက်သွယ်နိုင်ပါသည် -"
                ),
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )
            schedule_deletion(context, vip_msg)
            
    except Exception as e:
        await query.message.reply_text(f"⚠️ Error: {str(e)}")

def schedule_start_deletion(context, sent_msg):
    async def delete_start_msg():
        await asyncio.sleep(600)  # 10 minutes
        try:
            await context.bot.delete_message(chat_id=sent_msg.chat_id, message_id=sent_msg.message_id)
        except Exception:
            pass
    context.application.create_task(delete_start_msg())

def schedule_deletion(context, sent_msg):
    async def delete_msg():
        await asyncio.sleep(43200)  # 12 hours
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
    
