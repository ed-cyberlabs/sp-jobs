import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler

TOKEN = os.environ['8394541384:AAFCYsw-o9WQ0zLerkcOJA1F3GLa-wtE0CQ']
GROUP_CHAT_ID = int(os.environ['399547346'])

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
    await update.message.reply_text('What is the fee? (e.g. 130 or: To be Estimated)')
    return FEE

async def get_fee(update, context):
    context.user_data['fee'] = update.message.text
    await update.message.reply_text('What is the phone number?')
    return PHONE

async def get_phone(update, context):
    context.user_data['phone'] = update.message.text
    await update.message.reply_text('What is the date? (e.g. 14/04/2026)')
    return DATE

async def get_date(update, context):
    context.user_data['date'] = update.message.text
    await update.message.reply_text('What is the time? (e.g. 11:00 or 5-6pm)')
    return TIME_VAL

async def get_time(update, context):
    context.user_data['time'] = update.message.text
    await update.message.reply_text('Which tea