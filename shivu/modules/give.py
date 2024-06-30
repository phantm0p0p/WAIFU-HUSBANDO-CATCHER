# give.py
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
import random

from shivu import application, sudo_users, user_collection, collection

async def give_waifu(update: Update, context: CallbackContext) -> None:
    if str(update.effective_user.id) not in sudo_users:
        await update.message.reply_text('Ask My Owner...')
        return

    if not update.message.reply_to_message:
        await update.message.reply_text("You need to reply to a user's message to give waifus!")
        return

    receiver_id = update.message.reply_to_message.from_user.id
    try:
        count = int(context.args[0])
        if count < 1:
            await update.message.reply_text('Count must be a positive integer.')
            return
    except (IndexError, ValueError):
        await update.message.reply_text('Usage: /givewaifu {count}')
        return

    receiver = await user_collection.find_one({'id': receiver_id})
    if not receiver:
        receiver = {
            'id': receiver_id,
            'username': update.message.reply_to_message.from_user.username,
            'first_name': update.message.reply_to_message.from_user.first_name,
            'characters': []
        }

    # Fetch random characters from the collection
    waifus = []
    async for waifu in collection.aggregate([{ '$sample': { 'size': count } }]):
        waifus.append(waifu)

    if len(waifus) < count:
        await update.message.reply_text('Not enough waifus available in the database.')
        return

    # Add the characters to the user's collection
    receiver['characters'].extend(waifus)
    await user_collection.update_one({'id': receiver_id}, {'$set': receiver}, upsert=True)

    # Create mention text
    mention_text = f'[{update.message.reply_to_message.from_user.first_name}](tg://user?id={receiver_id})'
    
    # Notify the user
    await update.message.reply_text(f'Gave {count} waifus to {mention_text}.', parse_mode='Markdown')

# Add the command handler
GIVE_HANDLER = CommandHandler('givewaifu', give_waifu, block=False)
application.add_handler(GIVE_HANDLER)
