import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler

TOKEN = os.environ['TOKEN']
GROUP_CHAT_ID = int(os.environ['GROUP_CHAT_ID'])

NAME, EMAIL, ADDRESS, DESC, FEE, PHONE, DATE, TIME_VAL, TEAM = range(9)

async def newjob(update, context):
    context.user_data.clear()
    await update.message.reply_text('What is the customer name?')
    return NAME

async def get_name(update, context):
    context.user_data['name'] = update.message.text
    await update.message.reply_text('What is the email address?')
    return EMAIL

async def get_email(update, context):
    context.user_data['email'] = update.message.text
    await update.message.reply_text('What is the address?')
    return ADDRESS

async def get_address(update, context):
    context.user_data['address'] = update.message.text
    await update.message.reply_text('What is the job description?')
    return DESC

async def get_desc(update, context):
    context.user_data['desc'] = update.message.text
    await update.message.reply_text('What is the fee?')
    return FEE

async def get_fee(update, context):
    context.user_data['fee'] = update.message.text
    await update.message.reply_text('What is the phone number?')
    return PHONE

async def get_phone(update, context):
    context.user_data['phone'] = update.message.text
    await update.message.reply_text('What is the date?')
    return DATE

async def get_date(update, context):
    context.user_data['date'] = update.message.text
    await update.message.reply_text('What is the time?')
    return TIME_VAL

async def get_time(update, context):
    context.user_data['time'] = update.message.text
    await update.message.reply_text('Which team?')
    return TEAM

async def get_team(update, context):
    d = context.user_data
    msg = (
        'Name: ' + d['name'] + '\n'
        'Email: ' + d['email'] + '\n'
        'Address: ' + d['address'] + '\n'
        'Job Description: ' + d['desc'] + '\n'
        'Fee: ' + d['fee'] + '\n'
        'Phone Number: ' + d['phone'] + '\n'
        'Date: ' + d['date'] + '\n'
        'Time: ' + d['time'] + '\n'
        'Status: To be Booked\n'
        'Team: ' + update.message.text
    )
    print("SENDING TO CHAT ID:", GROUP_CHAT_ID)
    try:
        await context.bot.send_message(chat_id=GROUP_CHAT_ID, text=msg)
        print("SUCCESS")
    except Exception as e:
        print("FAILED:", e)
    await update.message.reply_text('Done! Job posted to the group.')
    return ConversationHandler.END

async def cancel(update, context):
    context.user_data.clear()
    await update.message.reply_text('Cancelled. Send /newjob to start again.')
    return ConversationHandler.END

app = ApplicationBuilder().token(TOKEN).build()

conv = ConversationHandler(
    entry_points=[CommandHandler('newjob', newjob)],
    states={
        NAME:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
        EMAIL:    [MessageHandler(filters.TEXT & ~filters.COMMAND, get_email)],
        ADDRESS:  [MessageHandler(filters.TEXT & ~filters.COMMAND, get_address)],
        DESC:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_desc)],
        FEE:      [MessageHandler(filters.TEXT & ~filters.COMMAND, get_fee)],
        PHONE:    [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
        DATE:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_date)],
        TIME_VAL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_time)],
        TEAM:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_team)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
    per_message=False,
    per_chat=True,
    per_user=True,
)

app.add_handler(conv)
app.run_polling(drop_pending_updates=True)
