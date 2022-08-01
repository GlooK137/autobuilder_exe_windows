from email import message
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

from os import mkdir, path, remove
from random import randint
from zipfile import ZipFile

from builder import build


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(content_types=['document'])
async def echo_message(msg: types.Message):
    folder_name = str( randint( 0, 999999999 ) )
    mkdir(folder_name)
    destination = path.join(folder_name, msg.document.file_name)
    destination_file = await msg.document.download(destination)
    with ZipFile(destination) as zip_file:
        zip_file.extractall(folder_name)
    #remove(destination)
    await msg.answer_document( await build(folder_name))



if __name__ == '__main__':
    executor.start_polling(dp)