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
        [InlineKeyboardButton("🎬 The Flash (2014) season 1 to 9", callback_data="m1")],
        [InlineKeyboardButton("🎬 Lucifer (2016) season 1 to 6", callback_data="m2")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_photo(
        photo="AgACAgUAAxkBAAEgueJqYFrWN-knIvOwmsOQ859SgDB3eQACUxVrG9u7CFdtu8B_Lb_nPQEAAwIAA3gAAz0E",
        caption=(
            "✨ **ကြိုဆိုပါတယ်ခင်ဗျာ!**\n"
            "အောက်ပါ ဇာတ်ကားများကို နှိပ်၍ အပိုင်းများကို ရွေးချယ်နိုင်ပါသည် -"
        ),
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    try:
        # ----------------- ဇာတ်ကား (၁) : The Flash -----------------
        if data == "m1":
            keyboard = [
                [InlineKeyboardButton("အပိုင်း (၁) - Free", callback_data="m1_ep1")],
                [InlineKeyboardButton("အပိုင်း (၂) - Free", callback_data="m1_ep2")],
                [InlineKeyboardButton("အပိုင်း (၃) - Free", callback_data="m1_ep3")],
                [InlineKeyboardButton("အပိုင်း (၄) - Free", callback_data="m1_ep4")],
                [InlineKeyboardButton("အပိုင်း (၅) - Free", callback_data="m1_ep5")],
                [InlineKeyboardButton("အပိုင်း (၆) - Free", callback_data="m1_ep6")],
                [InlineKeyboardButton("💬 မန်ဘာဝင်ရန် ဆက်သွယ်ရန်", url=f"https://t.me/{CONTACT_USERNAME.replace('@', '')}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.message.reply_photo(
                photo="AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3cAAz0E",
                caption=(
                    "📌 **The Flash (2014)**\n"
                    "• အပိုင်း (၁) မှ (၆) အထိ ကြည့်ရှုနိုင်ပါသည်။\n"
                    "• ပို့ပေးသော ဗီဒီယိုများသည် **(၆) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်။\n"
                    "• မန်ဘာကြေး - **တစ်ကားလျှင် ၂,၀၀၀ ကျပ်**\n\n"
                    "အောက်ပါ အပိုင်းများကို ရွေးချယ်ပါ -"
                ),
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )

        # ----------------- ဇာတ်ကား (၂) : Lucifer -----------------
        elif data == "m2":
            keyboard = [
                [InlineKeyboardButton("အပိုင်း (၁) - Free", callback_data="m2_ep1")],
                [InlineKeyboardButton("အပိုင်း (၂) - Free", callback_data="m2_ep2")],
                [InlineKeyboardButton("အပိုင်း (၃) - Free", callback_data="m2_ep3")],
                [InlineKeyboardButton("အပိုင်း (၄) - Free", callback_data="m2_ep4")],
                [InlineKeyboardButton("အပိုင်း (၅) - Free", callback_data="m2_ep5")],
                [InlineKeyboardButton("အပိုင်း (၆) - Free", callback_data="m2_ep6")],
                [InlineKeyboardButton("💬 မန်ဘာဝင်ရန် ဆက်သွယ်ရန်", url=f"https://t.me/{CONTACT_USERNAME.replace('@', '')}")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.message.reply_photo(
                photo="AgACAgUAAxkBAAEguktqYGtKcwc5Lz0a-uvM011zR6ouQQACrBJrG-62aFXF-kV2rfK7_gEAAwIAA3cAAz0E",
                caption=(
                    "📌 **Lucifer (2016)**\n"
                    "• အပိုင်း (၁) မှ (၆) အထိ ကြည့်ရှုနိုင်ပါသည်။\n"
                    "• ပို့ပေးသော ဗီဒီယိုများသည် **(၆) နာရီကြာပါက** အလိုအလျောက် ပျက်သွားပါမည်။\n"
                    "• မန်ဘာကြေး - **တစ်ကားလျှင် ၂,၀၀၀ ကျပ်**\n\n"
                    "အောက်ပါ အပိုင်းများကို ရွေးချယ်ပါ -"
                ),
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )

        # ----------------- ဇာတ်ကား (၁) : The Flash ဗီဒီယိုများ -----------------
        elif data == "m1_ep1":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="BAACAgUAAxkBAAEgubBqYFc8zCBAF0q4TGoZwX3xHLSX1AACJB4AAoXLgVRxAUNrR-eL_z0E",
                caption="🎬 The Flash (2014) - အပိုင်း (၁)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "m1_ep2":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="BAACAgUAAxkBAAEgullqYGxRVOwVCisP1T14wkwpTeDrAwACJR4AAoXLgVSvbOSV-SlXHD0E",
                caption="🎬 The Flash (2014) - အပိုင်း (၂)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "m1_ep3":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="BAACAgUAAxkBAAEguqtqYH1JKVaAc4r3m1D_TSEGpRLRrQACJh4AAoXLgVTZ9Tnit771Sz0E",
                caption="🎬 The Flash (2014) - အပိုင်း (၃)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "m1_ep4":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="BAACAgUAAxkBAAEguqxqYH1JCxkERguduVwRuf7HDAb2-gACKx4AAoXLgVRTok4Dly278z0E",
                caption="🎬 The Flash (2014) - အပိုင်း (၄)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "m1_ep5":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="BAACAgUAAxkBAAEguq1qYH1JMSEgt1ePqSHRuT58A0J94wAC1yMAAlnEeFT7fXUpjRcYMD0E",
                caption="🎬 The Flash (2014) - အပိုင်း (၅)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "m1_ep6":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="BAACAgUAAxkBAAEgulfqYGw4w2Z9_1g885Oau3MBQAZ5dgACGxkAAlnEgFQsmJuyY9nHzD0E",
                caption="🎬 The Flash (2014) - အပိုင်း (၆)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        # ----------------- ဇာတ်ကား (၂) : Lucifer ဗီဒီယိုများ -----------------
        elif data == "m2_ep1":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="BAACAgUAAxkBAAEgusVqYH9ML8Wz_1g885Oau3MBQAZ5dgACGxkAAlnEgFQsmJuyY9nHzD0E",
                caption="🎬 Lucifer (2016) - အပိုင်း (၁)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "m2_ep2":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="BAACAgUAAxkBAAEgusdqYH-Se21TwLwEDW3wExwMEhJP9gACBxoAAlnEgFSGD6a-ep3_wj0E",
                caption="🎬 Lucifer (2016) - အပိုင်း (၂)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "m2_ep3":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="BAACAgUAAxkBAAEgus1qYH_dvXVp2vP9ZAZ1WyIDxtFyHQACWhkAAlnEgFQxHsouPRWm1D0E",
                caption="🎬 Lucifer (2016) - အပိုင်း (၃)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "m2_ep4":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="BAACAgUAAxkBAAEgutNqYIAQ1YVOgrqS4AzuR1Pe54iYKgACZhkAAlnEgFRDkdzKuTv3xT0E",
                caption="🎬 Lucifer (2016) - အပိုင်း (၄)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "m2_ep5":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="BAACAgUAAxkBAAEgutVqYICU0yb2rG2-ux8vEEgAAeO5IrgAApYZAAJZxIBULyCSzraSoIM9BA",
                caption="🎬 Lucifer (2016) - အပိုင်း (၅)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)

        elif data == "m2_ep6":
            sent_msg = await context.bot.send_video(
                chat_id=query.message.chat_id,
                video="BAACAgUAAxkBAAEgutdqYIDNUzAzxQdGBqkH5AM0-gQIkAACnhkAAlnEgFSZ92iCDLoVuj0E",
                caption="🎬 Lucifer (2016) - အပိုင်း (၆)\n\n⚠️ ဤဗီဒီယိုသည် ၆ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။"
            )
            schedule_deletion(context, sent_msg)
            
    except Exception as e:
        await query.message.reply_text(f"⚠️ Error: {str(e)}")

def schedule_deletion(context, sent_msg):
    async def delete_msg():
        await asyncio.sleep(21600)  # 6 hours = 21600 seconds
        try:
            await context.bot.delete_message(chat_id=sent_msg.chat_id, message_id=sent_msg.message_id)
        except Exception:
            pass
    context.application.create_task(delete_msg())

if __name__ == '__main__':
    TOKEN = "8935742099:AAH9U84SCqLairPP7NEMoHGnILDtsJkS4EQ"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    application.run_polling(drop_pending_updates=True)
            
