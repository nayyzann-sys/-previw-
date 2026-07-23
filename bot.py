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
    await update.message.reply_text(
        "✨ **ကြိုဆိုပါတယ်ခင်ဗျာ!**\nအောက်ပါ ဇာတ်ကားကို နှိပ်၍ အပိုင်းများကို ရွေးချယ်နိုင်ပါသည် -",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    try:
        if data == "m1":
            keyboard = [
                [InlineKeyboardButton("အပိုင်း (၁) - Free", callback_data="ep_1")],
                [InlineKeyboardButton("အပိုင်း (၂) - Free", callback_data="ep_2")],
                [InlineKeyboardButton("အပိုင်း (၃) - Free", callback_data="ep_3")],
                [InlineKeyboardButton("အပိုင်း (၄) - Free", callback_data="ep_4")],
                [InlineKeyboardButton("အပိုင်း (၅) - Free", callback_data="ep_5")],
                [InlineKeyboardButton("အပိုင်း (၆) - Free", callback_data="ep_6")],
                [InlineKeyboardButton("အပိုင်း (၇) နှင့်အထက် - VIP", callback_data="vip_locked")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.message.reply_text(
                "📌 **The Flash (2014)**\n"
                "• အပိုင်း (၁) မှ (၆) အထိ အလကား (Free) ကြည့်ရှုနိုင်ပါသည်။\n"
                "• ပို့ပေးသော ဗီဒီယိုများသည် **(၆) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်။\n"
                "• အပိုင်းအသစ်များနှင့် ကျန်အပိုင်းများကို ကြည့်ရှုလိုပါက VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။\n\n"
                "အောက်ပါ အပိုင်းများကို ရွေးချယ်ပါ -",
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )

        # အပိုင်း (၁) မှ (၆) အထိ File ID များကို ဤနေရာတွင် ထည့်ပါ 👇
        elif data == "ep_1":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="အပိုင်း ၁ ရဲ့ File ID ကို ဤနေရာတွင် ထည့်ပါ",
                caption="🎬 The Flash (2014) - အပိုင်း (၁)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "ep_2":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="အပိုင်း ၂ ရဲ့ File ID ကို ဤနေရာတွင် ထည့်ပါ",
                caption="🎬 The Flash (2014) - အပိုင်း (၂)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "ep_3":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="အပိုင်း ၃ ရဲ့ File ID ကို ဤနေရာတွင် ထည့်ပါ",
                caption="🎬 The Flash (2014) - အပိုင်း (၃)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "ep_4":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="အပိုင်း ၄ ရဲ့ File ID ကို ဤနေရာတွင် ထည့်ပါ",
                caption="🎬 The Flash (2014) - အပိုင်း (၄)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "ep_5":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="အပိုင်း ၅ ရဲ့ File ID ကို ဤနေရာတွင် ထည့်ပါ",
                caption="🎬 The Flash (2014) - အပိုင်း (၅)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "ep_6":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="အပိုင်း ၆ ရဲ့ File ID ကို ဤနေရာတွင် ထည့်ပါ",
                caption="🎬 The Flash (2014) - အပိုင်း (၆)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "vip_locked":
            keyboard = [
                [InlineKeyboardButton("💬 မန်ဘာဝင်ရန် ဆက်သွယ်ရန်", url=f"https://t.me/{CONTACT_USERNAME.replace('@', '')}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.message.reply_text(
                f"🔒 **VIP အပိုင်းများ (အပိုင်း ၇ နှင့်အထက်)**\n\n"
                f"⚠️ ဤ အပိုင်းများကို ကြည့်ရှုရန်အတွက် VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။\n"
                f"မန်ဘာဝင်လိုပါက အောက်ပါခလုတ်ကို နှိပ်၍ Owner ထံသို့ ဆက်သွယ်နိုင်ပါသည် -",
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )
            
    except Exception as e:
        await query.message.reply_text(f"⚠️ Error: {str(e)}")

# ၆ နာရီကြာရင် မက်ဆေ့ချ်ဖျက်ပေးမည့် ဖန်ရှင်
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
    
