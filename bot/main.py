from aiogram import Bot, Dispatcher, F, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

ADMIN_ID = 726130790
bot = Bot(token="8146852108:AAGIBIdz1rMr2wrdviLrglNM6_an3W25t30")
dp = Dispatcher()

confirm_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Yetkazib berildi ✅', callback_data='confirm_order')
        ]
    ]
)

@dp.message(F.text=='/start')
async def start(message: types.Message):
    await message.answer("Tarvuz market botiga xush kelibsiz")

async def send_message_to_admin(data):
    await bot.send_message(chat_id=ADMIN_ID, text=f"Yangi buyurtma {data}, qabul qilasizmi?", reply_markup=confirm_btn)
    print("adminga xabar yuborildi")

@dp.callback_query(F.data == 'confirm_order')
async def confirm(call: types.CallbackQuery):
    

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())