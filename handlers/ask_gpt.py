import logging
import openai

from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender

from main import config

openai.api_key = config['GPT_API']
openai.api_base = config['GPT_URL']
#print(openai.Model.list())
router = Router()


@router.message(F.text)
async def get_response(message: Message):
    async with ChatActionSender.typing(chat_id=message.chat.id):
        logging.info('[' + str(message.chat.id) + '] prompt: ' + message.text)
        response = openai.Completion.create(
            prompt=message.text,
            model=config['MODEL'],
            max_tokens=config['MAX_TOKENS'],
            temperature=config['TEMPERATURE']
        )
    try:
        if response and 'error' not in response:
            logging.debug(str(response))
            logging.info('[' + response['model'] + '] completion: ' + response.choices[0].text)
            await message.answer(response.choices[0].text)
    except Exception as e:
        logging.error(e)
