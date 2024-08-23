token = "7292007991:AAHNqunMM86zMNMFDHBYL907imygtYdMOuQ"
import g4f
import os
import asyncio
import logging
import nest_asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

print("started...")

nest_asyncio.apply()

# Set event loop policy for Windows
if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Disable logging
g4f.debug.logging = False
g4f.check_versiona= False

# Configure Python logging to suppress lower severity messages
logging.basicConfig(level=logging.ERROR)

# Function to get a normal response with language preference
def gpt(user_input):
    try:
        # Custom response for specific queries
        if 'your name' in user_input.lower():
            return "My name is Dark."

        # if 'who made you' in user_input.lower():
        #     return "I am an AI chatbot named Dark, created entirely from scratch by Dhruv Kadam."

        if 'who is Dhruv Kadam' in user_input.lower():
            return ("Dhruv Kadam is a talented 17-year-old developer who created me, Dark, "
                    "the AI chatbot, entirely from scratch. He is an expert in AI and machine "
                    "learning development.")
        if 'who is dhruv kadam' in user_input.lower():
            return ("Dhruv Kadam is a talented 17-year-old developer who created me, Dark, "
                    "the AI chatbot, entirely from scratch. He is an expert in AI and machine "
                    "learning development.")
        if 'who is dhruv' in user_input.lower():
            return ("Dhruv Kadam is a talented 17-year-old developer who created me, Dark, "
                    "the AI chatbot, entirely from scratch. He is an expert in AI and machine "
                    "learning development.")
        if 'who is Dhruv' in user_input.lower():
            return ("Dhruv Kadam is a talented 17-year-old developer who created me, Dark, "
                    "the AI chatbot, entirely from scratch. He is an expert in AI and machine "
                    "learning development.")
        if 'dhruv kadam' in user_input.lower():
            return ("Dhruv Kadam is a talented 17-year-old developer who created me, Dark, "
                    "the AI chatbot, entirely from scratch. He is an expert in AI and machine "
                    "learning development.")

        if 'what can you do' in user_input.lower():
            return ("I can assist with various tasks, answer questions, and engage in conversations. "
                    "I'm constantly learning and evolving thanks to my creator, Dhruv Kadam.")

        # Specify language preference in the system message
        messages = [
            {"role": "system", "content": '''Your name is Dark, & Dhruv Kadam is a talented 17-year-old developer who created, Dark, "
                    "the AI chatbot, entirely from scratch. He is an expert in AI and machine. and dhruv kadam name is person name dhruv"
                    "learning development. , respond in english only'''},
            {"role": "user", "content": user_input}
        ]

        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ensure this model is supported by the provider
            messages=messages,
        )

        # Debugging: Print the entire response to check its structure
        # If the response is a string, return it directly
        if isinstance(response, str):
            return response
        else:
            # Extract the content from the response assuming it's a dictionary
            return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error during normal response: {e}")
        return f"Error during normal response: {e}"

# Define a command handler for the /start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! I am Dark.')

# Define a message handler to handle user messages
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    response = gpt(user_input)
    await update.message.reply_text(response)

def main():
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
