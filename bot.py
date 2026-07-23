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
        [InlineKeyboardButton("🎬 The Flash (2014)", callback_data="m1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Start နှိပ်လိုက်ရင် ပေါ်မယ့် မက်ဆေ့ချ် (၁၀ မိနစ်အတွင်း မနှိပ်ရင် ပျက်မယ်၊ ပျက်သွားရင် /start ပြန်နှိပ်ပြီး ယူလို့ရမယ်)
    sent_msg = await update.message.reply_text(
        "✨ **ကြိုဆိုပါတယ်ခင်ဗျာ!**\n"
        "အောက်ပါ ဇာတ်ကားကို နှိပ်၍ အပိုင်းများကို ရွေးချယ်နိုင်ပါသည် -\n\n"
        "⚠️ *မှတ်ချက် - ဤမက်ဆေ့ချ်သည် ၁၀ မိနစ်ကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။ လင့်ခ်ပျက်သွားပါက သို့မဟုတ် အချိန်မရွေး ကြည့်ချင်ပါက /start ဖြင့် အလွယ်တကူ ပြန်ယူနိုင်ပါသည်။*",
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
            # ဇာတ်ကား ခေါင်းစဉ်နှင့် အချက်အလက်စာသား ပို့မည်
            await query.message.reply_text(
                "📌 **The Flash (2014)**\n"
                "• အပိုင်း (၁) မှ (၆) အထိ အလကား (Free) ကြည့်ရှုနိုင်ပါသည်။\n"
                "• ပို့ပေးသော ဗီဒီယိုများသည် **(၆) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်။\n"
                "• ဗီဒီယိုများ ပျက်သွားပါက သို့မဟုတ် အချိန်မရွေး ထပ်မံကြည့်ရှုချင်ပါက **/start** ကို ပြန်နှိပ်ပြီး အသစ်ပြန်ယူ ကြည့်ရှုနိုင်ပါသည်။",
                parse_mode="Markdown"
            )

            # အပိုင်း (၁) မှ (၆) အထိ ဗီဒီယိုများကို တစ်ခါတည်း တန်းပြီး ပို့ပေးမည် (၆ နာရီကြာရင် ပျက်မယ်)
            msg1 = await context.bot.send_video(chat_id=query.message.chat_id, video="အပိုင်း ၁ ရဲ့ File ID ကို ဤနေရာတွင် ထည့်ပါ", caption="🎬 The Flash (2014) - အပိုင်း (၁)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက ပျက်သွားပါမည်။ (အချိန်မရွေး /start ပြန်နှိပ်ပြီး ကြည့်နိုင်သည်)")
            schedule_deletion(context, msg1)

            msg2 = await context.bot.send_video(chat_id=query.message.chat_id, video="အပိုင်း ၂ ရဲ့ File ID ကို ဤနေရာတွင် ထည့်ပါ", caption="🎬 The Flash (2014) - အပိုင်း (၂)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက ပျက်သွားပါမည်။ (အချိန်မရွေး /start ပြန်နှိပ်ပြီး ကြည့်နိုင်သည်)")
            schedule_deletion(context, msg2)

            msg3 = await context.bot.send_video(chat_id=query.message.chat_id, video="အပိုင်း ၃ ရဲ့ File ID ကို ဤနေရာတွင် ထည့်ပါ", caption="🎬 The Flash (2014) - အပိုင်း (၃)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက ပျက်သွားပါမည်။ (အချိန်မရွေး /start ပြန်နှိပ်ပြီး ကြည့်နိုင်သည်)")
            schedule_deletion(context, msg3)

            msg4 = await context.bot.send_video(chat_id=query.message.chat_id, video="အပိုင်း ၄ ရဲ့ File ID ကို ဤနေရာတွင် ထည့်ပါ", caption="🎬 The Flash (2014) - အပိုင်း (၄)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက ပျက်သွားပါမည်။ (အချိန်မရွေး /start ပြန်နှိပ်ပြီး ကြည့်နိုင်သည်)")
            schedule_deletion(context, msg4)

            msg5 = await context.bot.send_video(chat_id=query.message.chat_id, video="အပိုင်း ၅ ရဲ့ File ID ကို ဤနေရာတွင် ထည့်ပါ", caption="🎬 The Flash (2014) - အပိုင်း (၅)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက ပျက်သွားပါမည်။ (အချိန်မရွေး /start ပြန်နှိပ်ပြီး ကြည့်နိုင်သည်)")
            schedule_deletion(context, msg5)

            msg6 = await context.bot.send_video(chat_id=query.message.chat_id, video="အပိုင်း ၆ ရဲ့ File ID ကို ဤနေရာတွင် ထည့်ပါ", caption="🎬 The Flash (2014) - အပိုင်း (၆)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက ပျက်သွားပါမည်။ (အချိန်မရွေး /start ပြန်နှိပ်ပြီး ကြည့်နိုင်သည်)")
            schedule_deletion(context, msg6)

            # အပိုင်း (၇) နှင့်အထက် အတွက် မန်ဘာဝင်ရန် ဆက်သွယ်ရန် ခလုတ်
            keyboard = [
                [InlineKeyboardButton("💬 မန်ဘာဝင်ရန် ဆက်သွယ်ရန် (၂၀၀၀ ကျပ်)", url=f"https://t.me/{CONTACT_USERNAME.replace('@', '')}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await context.bot.send_message(
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
            
    except Exception as e:
        await query.message.reply_text(f"⚠️ Error: {str(e)}")

# ၁၀ မိနစ်ကြာရင် start မက်ဆေ့ချ်ကို ဖျက်မည့် ဖန်ရှင်
def schedule_start_deletion(context, sent_msg):
    async def delete_start_msg():
        await asyncio.sleep(600)  # 10 minutes = 600 seconds
        try:
            await context.bot.delete_message(chat_id=sent_msg.chat_id, message_id=sent_msg.message_id)
        except Exception:
            pass
    context.application.create_task(delete_start_msg())

# ၆ နာရီကြာရင် ဗီဒီယိုဖျက်ပေးမည့် ဖန်ရှင်
def schedule_deletion(context, sent_msg):
    async def delete_msg():
        await asyncio.sleep(21600)  # 6 hours = 21600 seconds
        try:
            await context.bot.delete_message(chat_id=sent_msg.chat_id, message_id=sent_msg.message_id)
        except Exception:
            pass
    context.application.create_task(delete_msg())

if __name__ == '__main__':
    TOKEN = "8954957485:AAHkVsWNBZDzfxEg1y0u62Vo2hCPYg51RR4"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    application.run_polling(drop_pending_updates=True)
    
