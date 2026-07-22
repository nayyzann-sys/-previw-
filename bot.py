import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

CONTACT_USERNAME = "naywww01"

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
    chat_id = query.message.chat_id

    try:
        # ----------------- ဇာတ်ကား (၁) : The Flash -----------------
        if data == "m1":
            video_list_m1 = [
                ("BAACAgUAAxkBAAEgubBqYFc8zCBAF0q4TGoZwX3xHLSX1AACJB4AAoXLgVRxAUNrR-eL_z0E", "🎬 The Flash (2014) - အပိုင်း (၁)"),
                ("BAACAgUAAxkBAAEgullqYGxRVOwVCisP1T14wkwpTeDrAwACJR4AAoXLgVSvbOSV-SlXHD0E", "🎬 The Flash (2014) - အပိုင်း (၂)"),
                ("BAACAgUAAxkBAAEguqtqYH1JKVaAc4r3m1D_TSEGpRLRrQACJh4AAoXLgVTZ9Tnit771Sz0E", "🎬 The Flash (2014) - အပိုင်း (၃)"),
                ("BAACAgUAAxkBAAEguqxqYH1JCxkERguduVwRuf7HDAb2-gACKx4AAoXLgVRTok4Dly278z0E", "🎬 The Flash (2014) - အပိုင်း (၄)"),
                ("BAACAgUAAxkBAAEguq1qYH1JMSEgt1ePqSHRuT58A0J94wAC1yMAAlnEeFT7fXUpjRcYMD0E", "🎬 The Flash (2014) - အပိုင်း (၅)"),
                ("BAACAgUAAxkBAAEgulfqYGw4w2Z9_1g885Oau3MBQAZ5dgACGxkAAlnEgFQsmJuyY9nHzD0E", "🎬 The Flash (2014) - အပိုင်း (၆)")
            ]

            for vid, cap in video_list_m1:
                sent_msg = await context.bot.send_video(
                    chat_id=chat_id,
                    video=vid,
                    caption=f"{cap}\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။",
                    protect_content=True
                )
                context.job_queue.run_once(
                    delete_message_job, 
                    when=43200, 
                    data={"chat_id": sent_msg.chat_id, "message_id": sent_msg.message_id}
                )

            keyboard = [[InlineKeyboardButton("VIP မန်ဘာဝင်ရန် (2000)ဆက်သွယ်ရန်", url=f"https://t.me/{CONTACT_USERNAME}")]]
            await context.bot.send_message(
                chat_id=chat_id,
                text="🔒 **အပိုင်း (၇) နှင့် အထက် ကျန်ရှိသော အပိုင်းများကို ကြည့်ရှုလိုပါက VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။**",
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode="Markdown",
                protect_content=True
            )

        # ----------------- ဇာတ်ကား (၂) : Lucifer -----------------
        elif data == "m2":
            video_list_m2 = [
                ("BAACAgUAAxkBAAEgusVqYH9ML8Wz_1g885Oau3MBQAZ5dgACGxkAAlnEgFQsmJuyY9nHzD0E", "🎬 Lucifer (2016) - အပိုင်း (၁)"),
                ("BAACAgUAAxkBAAEgusdqYH-Se21TwLwEDW3wExwMEhJP9gACBxoAAlnEgFSGD6a-ep3_wj0E", "🎬 Lucifer (2016) - အပိုင်း (၂)"),
                ("BAACAgUAAxkBAAEgus1qYH_dvXVp2vP9ZAZ1WyIDxtFyHQACWhkAAlnEgFQxHsouPRWm1D0E", "🎬 Lucifer (2016) - အပိုင်း (၃)"),
                ("BAACAgUAAxkBAAEgutNqYIAQ1YVOgrqS4AzuR1Pe54iYKgACZhkAAlnEgFRDkdzKuTv3xT0E", "🎬 Lucifer (2016) - အပိုင်း (၄)"),
                ("BAACAgUAAxkBAAEgutVqYICU0yb2rG2-ux8vEEgAAeO5IrgAApYZAAJZxIBULyCSzraSoIM9BA", "🎬 Lucifer (2016) - အပိုင်း (၅)"),
                ("BAACAgUAAxkBAAEgutdqYIDNUzAzxQdGBqkH5AM0-gQIkAACnhkAAlnEgFSZ92iCDLoVuj0E", "🎬 Lucifer (2016) - အပိုင်း (၆)")
            ]

            for vid, cap in video_list_m2:
                sent_msg = await context.bot.send_video(
                    chat_id=chat_id,
                    video=vid,
                    caption=f"{cap}\n\n⚠️ ဤဗီဒီယိုသည် ၁၂ နာရီကြာပါက အလိုအလျောက် ပျက်သွားပါမည်။",
                    protect_content=True
                )
                context.job_queue.run_once(
                    delete_message_job, 
                    when=43200, 
                    data={"chat_id": sent_msg.chat_id, "message_id": sent_msg.message_id}
                )

            keyboard = [[InlineKeyboardButton("VIP မန်ဘာဝင်ရန် (2000)ဆက်သွယ်ရန်", url=f"https://t.me/{CONTACT_USERNAME}")]]
            await context.bot.send_message(
                chat_id=chat_id,
                text="🔒 **အပိုင်း (၇) နှင့် အထက် ကျန်ရှိသော အပိုင်းများကို ကြည့်ရှုလိုပါက VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။**",
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode="Markdown",
                protect_content=True
            )

        # ----------------- VIP Locked -----------------
        elif data == "vip_locked":
            keyboard = [[InlineKeyboardButton("VIP မန်ဘာဝင်ရန် (2000)ဆက်သွယ်ရန်", url=f"https://t.me/{CONTACT_USERNAME}")]]
            await query.message.reply_text(
                "🔒 **VIP အပိုင်းများ (အပိုင်း ၇ နှင့်အထက်)**\n\n"
                "⚠️ ဤ အပိုင်းများကို ကြည့်ရှုရန်အတွက် VIP မန်ဘာဝင်ရန် လိုအပ်ပါသည်။\n"
                "💰 မန်ဘာကြေး - **တစ်ကားလျှင် ၂,၀၀၀ ကျပ်** ဖြစ်ပါသည်။\n\n"
                "မန်ဘာဝင်လိုပါက အောက်ပါခလုတ်ကို နှိပ်၍ ဆက်သွယ်နိုင်ပါသည် -",
                reply_markup=reply_markup,
                parse_mode="Markdown",
                protect_content=True
            )

    except Exception as e:
        logging.error(f"Error handling callback: {e}")

async def delete_message_job(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    try:
        await context.bot.delete_message(
            chat_id=job.data["chat_id"], 
            message_id=job.data["message_id"]
        )
    except Exception as e:
        logging.error(f"Error deleting message: {e}")

# ----------------- Main Execution -----------------
if __name__ == '__main__':
    TOKEN = os.getenv("BOT_TOKEN")
    
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("Bot is running...")
    application.run_polling(drop_pending_updates=True)
