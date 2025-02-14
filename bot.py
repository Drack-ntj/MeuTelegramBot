import os
import random
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Configuração do logging
logging.basicConfig(level=logging.INFO)

# Pegando o token do bot nas variáveis de ambiente
TOKEN = os.getenv("TOKEN")

# Criando o bot e o dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Mensagens para os comandos
mensagens_chute = [
    "💥 BOOM! @{} levou um chutão na barriga! 🥋",
    "👟 @{} foi chutado tão forte que foi parar no espaço! 🚀",
    "⚽ @{} foi confundido com uma bola de futebol! Gol! 🥅",
    "🦵 @{} recebeu um chute épico digno de um filme de ação! 🎬",
]

mensagens_tapa = [
    "🤚 SMACK! @{} levou um tapa que até girou! 🔄",
    "👋 @{} sentiu o peso da mão na cara! 😵",
    "💨 @{} foi estapeado tão forte que deixou marca! 👀",
    "🎭 @{} levou um tapa de novela mexicana! 🎬",
]

# Comando /chute
@dp.message_handler(commands=['chute'])
async def chute(message: types.Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.username
    else:
        chat_members = await bot.get_chat_administrators(message.chat.id)
        user = random.choice(chat_members).user.username

    resposta = random.choice(mensagens_chute).format(user)
    await message.reply(resposta)

# Comando /tapa
@dp.message_handler(commands=['tapa'])
async def tapa(message: types.Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.username
    else:
        chat_members = await bot.get_chat_administrators(message.chat.id)
        user = random.choice(chat_members).user.username

    resposta = random.choice(mensagens_tapa).format(user)
    await message.reply(resposta)

# Iniciar o bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)