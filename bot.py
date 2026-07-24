import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, MessageHandler, filters, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

MOVIES = {
    "1. The Flash (2014)": (
        "Season 1 to 9", 
        "AgACAgUAAxkBAAEguTZqYDpsIxym5LL1imj09cHLuhpPCQACoxJrG-62aFUXfew0CMQ-UQEAAwIAA3cAAz0E", 
        ("BAACAgUAAxkBAAEgubBqYFc8zCBAF0q4TGoZwX3xHLSX1AACJB4AAoXLgVRxAUNrR-eL_z0E", "BAACAgUAAxkBAAEgullqYGxRVOwVCisP1T14wkwpTeDrAwACJR4AAoXLgVSvbOSV-SlXHD0E", "BAACAgUAAxkBAAEguqtqYH1JKVaAc4r3m1D_TSEGpRLRrQACJh4AAoXLgVTZ9Tnit771Sz0E", "BAACAgUAAxkBAAEguqxqYH1JCxkERguduVwRuf7HDAb2-gACKx4AAoXLgVRTok4Dly278z0E", "BAACAgUAAxkBAAEguq1qYH1JMSEgt1ePqSHRuT58A0J94wAC1yMAAlnEeFT7fXUpjRcYMD0E", "BAACAgUAAxkBAAEgubBqYFc8zCBAF0q4TGoZwX3xHLSX1AACJB4AAoXLgVRxAUNrR-eL_z0E")
    ),
    "2. Lucifer (2016)": (
        "Season 1 to 6", 
        "AgACAgUAAxkBAAEgznxqYurUbcElqsCI4D7RH0Imw_k1jgACrBJrG-62aFXF-kV2rfK7_gEAAwIAA3cAAz0E", 
        ("BAACAgUAAxkBAAEgzn1qYurUnIeGXQW0NEr2bSNecEF09wACGxkAAlnEgFQsmJuyY9nHzD0E", "BAACAgUAAxkBAAEgzn5qYurUD2c7Tj-F_ssJuNzZZIcohwACBxoAAlnEgFSGD6a-ep3_wj0E", "BAACAgUAAxkBAAEgzn9qYurURBQLnJRSUJ9ZNOVe0aVfpgACWhkAAlnEgFQxHsouPRWm1D0E", "BAACAgUAAxkBAAEgzoFqYurUw23B27G5p-gQWsX1uNdmCQACZhkAAlnEgFRDkdzKuTv3xT0E", "BAACAgUAAxkBAAEgzoJqYurUwyH67X51PEHMAAF_kEOEhbYAApYZAAJZxIBULyCSzraSoIM9BA", "BAACAgUAAxkBAAEgzoNqYurUdYzNiHpUzucP9MSKAAFZcaAAAp4ZAAJZxIBUmfdoggy6Fbo9BA")
    ),
    "3. Arrow (2013)": (
        "Season 1 to 8", 
        "AgACAgUAAxkBAAEgzoVqYurUaB-0x0dqPv0KyFX7S5nhbgACChFrGxNCiFXQms3mMfLpvAEAAwIAA3kAAz0E", 
        ("BAACAgUAAxkBAAEgzoZqYurUgXMbNXYwweoezqQ6mt0VYgACNhoAAlnEgFSF9lco9BjWkz0E", "BAACAgUAAxkBAAEgzodqYurUpgYdXX77L_QKCWXbqFQHbgACZhoAAlnEgFRu8P5hhQvAWD0E", "BAACAgUAAxkBAAEgzohqYurUqfjjMqOnPkPh7xDxna3jhwACdRoAAlnEgFSX8mAaSTKHXT0E", "BAACAgUAAxkBAAEgzopqYurUSqb-HtMIcdIVwkiInoyKkwAClRoAAlnEgFQx0HQ1w-3r6D0E", "BAACAgUAAxkBAAEgzotqYurUr5qsT98ukzoe0YkV95o7xgACmBoAAlnEgFT9H2sq5kC-DD0E", "BAACAgUAAxkBAAEgzoxqYurUequMOmaV94XPpuZ2JTxjKQACmhoAAlnEgFQJnGxkomFDBT0E")
    ),
    "4. Agents of shield (2013)": (
        "Season 1 to 7", 
        "AgACAgUAAxkBAAEgzo1qYurUlF2seznfeVKtRnIdJ9JkaAACexFrG39ZoVW7JwbxO6Q2hQEAAwIAA3cAAz0E", 
        ("BAACAgUAAxkBAAEgzo5qYurUyZ3gRKMj1QN_7VuwcCusLwACqBoAAlnEgFQmgQ5XNYHljj0E", "BAACAgUAAxkBAAEgzpBqYurU_5suT8JKcFihGOkUnck0vAACqxoAAlnEgFSWgfecXrlkMj0E", "BAACAgUAAxkBAAEgzpFqYurU1qfSiHkz1X-RX05w3kpXbQACrRoAAlnEgFQlwkdQ_MCiEz0E", "BAACAgUAAxkBAAEgzpJqYurUgS48PQrWkeTarYTs1ZvQxwACrhoAAlnEgFQtEw6zm9chez0E", "BAACAgUAAxkBAAEgzpNqYurU0-4QVW9F8EJfNoAjjr9q_AACrxoAAlnEgFT68OA81yLNdz0E", "BAACAgUAAxkBAAEgzpVqYurUUJPpeDE5P6gPnsrkVl3dJgACsBoAAlnEgFQt-kql04BA6T0E")
    ),
    "5. Supernatural (2015)": (
        "Season 1 to 15", 
        "AgACAgUAAxkBAAEgzpZqYurU7LG2gHBWkhFUizoSOrD2PQACNw9rG-8-qVUYa58yxg1rYwEAAwIAA3cAAz0E", 
        ("BAACAgUAAxkBAAEgzpdqYurUdzTa5wKvyvYDLp8soBx0yQACvBoAAlnEgFQ-XEKPeel0zT0E", "BAACAgUAAxkBAAEgzplqYurU6XaExFZvlnAd3-ZmWqzAYwACvRoAAlnEgFR4I9vUXDq21j0E", "BAACAgUAAxkBAAEgzppqYurU7acIrD40p5JKh5CQj4V6xAACvhoAAlnEgFSHvJntW5uGUD0E", "BAACAgUAAxkBAAEgzptqYurUIYeYuJ6VKW5qCvs4Wdh95AACvxoAAlnEgFRZqlYTuJRRXD0E", "BAACAgUAAxkBAAEgzpxqYurURnLCkzSDXzaCcNEJ-QAB59YAAsAaAAJZxIBUUSdx9kt6Sk49BA", "BAACAgUAAxkBAAEgzp1qYurUVYUudxTdbjWSbZyehl7uhwACwRoAAlnEgFQiRo8bzbpxvz0E")
    ),
    "6. The Witcher (2019-2025)": (
        "Season 1 to 4", 
        "AgACAgUAAxkBAAEgzp5qYurUgyveUt6labXn0V4hFGOq2AACQA9rG-8-qVWquCCVRkfCYwEAAwIAA3cAAz0E", 
        ("BAACAgUAAxkBAAEgzp9qYurUicN_E61Jw3QbB31ZJ4MUnwAC1R0AAlnEiFRRgA4T-_NqQz0E", "BAACAgUAAxkBAAEgzqBqYurUIfU2reqYzbgSK1DLOk0wsgAC8x0AAlnEiFQyiiCe6xokfT0E", "BAACAgUAAxkBAAEgzqFqYurUgonhjKAgp0t1vsdAS4CU2AACYB4AAlnEiFQblTHiAAFCN9s9BA", "BAACAgUAAxkBAAEgzqJqYurUJPTCIVJ1ne6gIOJLD8R6XgACah4AAlnEiFS_bp1ig8qECz0E", "BAACAgUAAxkBAAEgzqRqYurU02rjYTQY_6P7WrN35EzdOAACdR4AAlnEiFSusL3wR7tpPD0E", "BAACAgUAAxkBAAEgzqVqYurUzJIq3_3MamJTQnUZlDrbjwACdx4AAlnEiFSogqtuAAGnIMQ9BA")
    ),
    "7. Game of thrones (2019)": (
        "Season 1 to 8", 
        "AgACAgUAAxkBAAEgzqZqYurUTr2z9rLiN2l3_8vPCakPUAACQw9rG-8-qVXh0YppdxaTNgEAAwIAA3cAAz0E", 
        ("BAACAgUAAxkBAAEgzqdqYurUS7oLqB6W1R9-PPJPW9BvNwAC7B4AAlnEiFTwVXGbtuy0Xz0E", "BAACAgUAAxkBAAEgzqhqYurUKZIFoOedUv7cMozsSANwmAAC_B4AAlnEiFSjh0xZf6SCbj0E", "BAACAgUAAxkBAAEgzqlqYurUVYgL8iMXrQ2FAAHc9ked9C0AAgQfAAJZxIhUUcVZBCPrZOM9BA", "BAACAgUAAxkBAAEgzqxqYurUuGagAu_jGGYeRC04umvJtwAC6BwAAg4JiFQvWTWqj0Aosz0E", "BAACAgUAAxkBAAEgzqpqYurUD8nACao12i7Xb0wCbmdVzQAC_BwAAg4JiFSyWa_ixYP3HD0E", "BAACAgUAAxkBAAEgzqtqYurUGkit4V7ucfS__jUtxg6_GgACWB4AAg4JkFSzmPCvMdRxVj0E")
    ),
    "8. The good doctor (2017)": (
        "Season 1 to 7", 
        "AgACAgUAAxkBAAEgzq1qYurUTVzg43BOjJ07DCxehR3nfQACXg5rG39ZqVUQPq8PmOnpPgEAAwIAA3cAAz0E", 
        ("BAACAgUAAxkBAAEgzq5qYurUf4BKSt7xLFoviW4PluPG8QACox4AAg4JkFQivwAB2Sw7gDY9BA", "BAACAgUAAxkBAAEgzq9qYurUpgWdxbXBFdjs4p7uculWuwACpB4AAg4JkFQdiN28xpyP3D0E", "BAACAgUAAxkBAAEgzrFqYurUlAwp7rRjC4YM03FuWMh3ggACpR4AAg4JkFSQWQfH0l61PD0E", "BAACAgUAAxkBAAEgzrJqYurUXK8l4LStDwABOOWb8aJ9KtYAAqYeAAIOCZBUdFDu41vEbxM9BA", "BAACAgUAAxkBAAEgzrNqYurUPVPy42cZVTLgks3N-O_OngACpx4AAg4JkFQ44SeOJhYGBj0E", "BAACAgUAAxkBAAEgzrRqYurU13J1fQ-rFG7eAgToAAHovokAAqgeAAIOCZBUDMzu_T62ncs9BA")
    ),
    "9. Mayor of kingstown (2021-2025)": (
        "Season 1 to 4", 
        "AgACAgUAAxkBAAEgzrVqYurUwNHgwJXmYgr9ZpCRKR8j4gACTw9rG-8-qVVYcrfupM1s1QEAAwIAA3kAAz0E", 
        ("BAACAgUAAxkBAAEgzrZqYurUXmttO17u19pPIBM93gpS4AACih8AAg4JkFQFu9oiFC3Pfj0E", "BAACAgUAAxkBAAEgzrdqYurUSQ3swVGKHaPCvKEaZw2LvQACrR8AAg4JkFQIjyBXINAJYT0E", "BAACAgUAAxkBAAEgzrhqYurUpeBlB45BeEixnYUlIPQY8QAC1B8AAg4JkFTX4RVJYz4qzj0E", "BAACAgUAAxkBAAEgzrlqYurUmnT_AAFB1eCDVx2eD4SdISAAAuQfAAIOCZBUHy6yzpjl2xU9BA", "BAACAgUAAxkBAAEgzrpqYurUbKFfPsBJe5t2ZFFpvOdMOwAC_B8AAg4JkFQ_ZvSEJGmmgT0E", "BAACAgUAAxkBAAEgzrtqYurUg_4OJyfxLv-v3DYEayCIWgAC7xwAAg4JmFTkwFynex7A3z0E")
    ),
    "10. Iron Man": (
        "Movie Collection", 
        "AgACAgUAAxkBAAEgzrVqYurUwNHgwJXmYgr9ZpCRKR8j4gACTw9rG-8-qVVYcrfupM1s1QEAAwIAA3kAAz0E", 
        ("BAACAgUAAxkBAAEgzrZqYurUXmttO17u19pPIBM93gpS4AACih8AAg4JkFQFu9oiFC3Pfj0E", "BAACAgUAAxkBAAEgzrdqYurUSQ3swVGKHaPCvKEaZw2LvQACrR8AAg4JkFQIjyBXINAJYT0E", "BAACAgUAAxkBAAEgzrhqYurUpeBlB45BeEixnYUlIPQY8QAC1B8AAg4JkFTX4RVJYz4qzj0E", "BAACAgUAAxkBAAEgzrlqYurUmnT_AAFB1eCDVx2eD4SdISAAAuQfAAIOCZBUHy6yzpjl2xU9BA", "BAACAgUAAxkBAAEgzrpqYurUbKFfPsBJe5t2ZFFpvOdMOwAC_B8AAg4JkFQ_ZvSEJGmmgT0E", "BAACAgUAAxkBAAEgzrtqYurUg_4OJyfxLv-v3DYEayCIWgAC7xwAAg4JmFTkwFynex7A3z0E")
    ),
}

async def set_bot_commands(application):
    commands = [
        BotCommand("start", "ဇာတ်ကားများကြည့်ရန် ပင်မစာမျက်နှာသို့သွားရန်")
    ]
    await application.bot.set_my_commands(commands)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [[KeyboardButton("/start")]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    
    keyboard = []
    for title in MOVIES.keys():
        keyboard.append([InlineKeyboardButton(f"🎬 {title}", callback_data=f"movie_{title}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_poster = "AgACAgUAAxkBAAEgznRqYurUmUDnoIVz7fnSiFsAAUMwMUoAAvYaaxvLRRFXAeiFaImm8hIBAAMCAAN4AAM9BA"
    
    welcome_text = (
        "✨ **ကြိုဆိုပါတယ်ခင်ဗျာ!**\n\n"
        "အောက်ပါ ဇာတ်ကားများထဲမှ ကြည့်လိုသည်များကို ရွေးချယ်နိုင်ပါသည် -\n\n"
        "⚠️ **မှတ်ချက်:** လင့်ခ် သို့မဟုတ် မက်ဆေ့ချ် ပျောက်သွားပါက `/start` ကို ပြန်နှိပ်ပြီး ပြန်ကြည့်နိုင်ပါသည်။"
    )

    try:
        sent_msg = await update.message.reply_photo(
            photo=welcome_poster,
            caption=welcome_text,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    except Exception:
        sent_msg = await update.message.reply_text(
            text=welcome_text,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    
    context.job_queue.run_once(auto_delete_message, 600, data=sent_msg.chat_id)

async def auto_delete_message(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    try:
        await context.bot.delete_message(chat_id=job.data, message_id=job.message.message_id)
    except Exception:
        pass

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data.startswith("movie_"):
        movie_title = data.replace("movie_", "")
        movie_info = MOVIES.get(movie_title, ("Season 1", "https://i.imgur.com/Default.jpg", ("", "", "", "", "", "")))
        seasons = movie_info[0]
        poster_url = movie_info[1]
        ep_files = movie_info[2]
        
        caption_text = (
            f"📌 **{movie_title}**\n"
            f"📺 **Seasons:** {seasons}\n\n"
            f"✨ အပိုင်း (၁) မှ (၆) အထိ ဗီဒီယိုဖိုင်များ -\n"
            f"💡 *(လင့်ခ် သို့မဟုတ် မက်ဆေ့ချ် ပျောက်သွားပါက `/start` ကို ပြန်နှိပ်ပြီး ကြည့်ပါ)*"
        )
        
        sent_msg = None
        try:
            sent_msg = await context.bot.send_photo(
                chat_id=query.message.chat_id,
                photo=poster_url,
                caption=caption_text,
                parse_mode="Markdown"
            )
        except Exception:
            sent_msg = await context.bot.send_message(
                chat_id=query.message.chat_id,
                text=caption_text,
                parse_mode="Markdown",
                protect_content=True
            )
        
        for index, file_id in enumerate(ep_files, start=1):
            if file_id and file_id != "EP1_FILE_ID":
                try:
                    await context.bot.send_video(
                        chat_id=query.message.chat_id,
                        video=file_id,
                        caption=f"📺 **{movie_title} - အပိုင်း ({index})**",
                        parse_mode="Markdown",
                        protect_content=True
                    )
                except Exception as e:
                    logging.error(f"Error sending video ep {index}: {e}")
                    pass
        
        keyboard = [
            [InlineKeyboardButton("🔒 အပိုင်း (၇) မှ အဆုံးထိ ကြည့်ရန် (မန်ဘာဝင်ရန် ၂၀၀၀ ကျပ် ဆက်သွယ်ရန်)", url="https://t.me/naywww01")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        try:
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text="✨ ဆက်လက်ကြည့်ရှုလိုပါက မန်ဘာဝင်ရန် ဆက်သွယ်နိုင်ပါသည်ခင်ဗျာ 👇\n\n*(မက်ဆေ့ချ်များ ပျောက်သွားပါက `/start` ကို ပြန်နှိပ်ပါ)*",
                reply_markup=reply_markup,
                parse_mode="Markdown"
            )
        except Exception:
            pass
        
        if sent_msg:
            context.job_queue.run_once(auto_delete_message_by_obj, 43200, data=(sent_msg.chat_id, sent_msg.message_id))

async def auto_delete_message_by_obj(context: ContextTypes.DEFAULT_TYPE):
    chat_id, message_id = context.job.data
    try:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except Exception:
        pass

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "/start":
        await start(update, context)

if __name__ == '__main__':
    TOKEN = "8935742099:AAF8HZBWbZLu4fh10TufidZ83TlnBHygVbE"
    
    application = ApplicationBuilder().token(TOKEN).read_timeout(60).write_timeout(60).connect_timeout(60).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), text_handler))
    
    asyncio.get_event_loop().run_until_complete(set_bot_commands(application))
    
    print("Bot is running...")
    application.run_polling(drop_pending_updates=True)
