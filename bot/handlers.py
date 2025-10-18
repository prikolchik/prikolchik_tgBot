import asyncio
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
import keyboards as kb
router = Router()

@router.message(CommandStart())
async def hii(message: Message):
    await message.answer_sticker("CAACAgIAAxkBAAESDBpou-LtchRTLtA98TJsg4x8WvGkywACngADzuT1KMhbRzEZD34LNgQ", reply_markup=kb.main)
    
@router.message(Command("dice"))
async def ii(message: Message):
    a = await message.answer_dice(emoji="🎲")
    await asyncio.sleep(4)
    dice_value = a.dice.value 
    await message.answer(f"кубик показал {dice_value}", reply_to_message_id=a.message_id)
    
@router.message(Command("football"))
async def ss(message: Message):
    a = await message.answer_dice(emoji="⚽")
    await asyncio.sleep(4)
    football_value = a.dice.value 
    if football_value in (3, 4, 5):
        await message.answer(f"гол! ", reply_to_message_id=a.message_id)    
    elif football_value == 2:
        await message.answer(f"в штангу ", reply_to_message_id=a.message_id)
    else:
        await message.answer(f"промах ", reply_to_message_id=a.message_id)
    
@router.message(Command("basketball"))
async def dd(message: Message):
    a = await message.answer_dice(emoji="🏀")
    await asyncio.sleep(4)
    basketball_value = a.dice.value 
    if basketball_value in ( 4, 5):
        await message.answer(f"попадание ", reply_to_message_id=a.message_id)    
    elif basketball_value in (1, 2):
        await message.answer(f"промах", reply_to_message_id=a.message_id)
    else:
        await message.answer(f"мяч застрял ", reply_to_message_id=a.message_id)
        
@router.message(Command("darts"))
async def dd(message: Message):
    a = await message.answer_dice(emoji="🎯")
    await asyncio.sleep(4)
    darts_value = a.dice.value 
    if darts_value == 6:
        await message.answer(f"прямо в яблочко ", reply_to_message_id=a.message_id)    
    elif darts_value in (2, 3, 4, 5):
        await message.answer(f"вы попали", reply_to_message_id=a.message_id)
    else:
        await message.answer(f"не попали", reply_to_message_id=a.message_id)
        
@router.message(Command("bowling"))
async def dd(message: Message):
    a = await message.answer_dice(emoji="🎳")
    await asyncio.sleep(4)
    bowling_value = a.dice.value 
    if bowling_value == 6:
        await message.answer(f"страйк ", reply_to_message_id=a.message_id)    
    elif bowling_value in (2, 3, 4, 5):
        await message.answer(f"попадание", reply_to_message_id=a.message_id)
    else:
        await message.answer(f"мимо", reply_to_message_id=a.message_id)
        
@router.message(Command("slots"))
async def dd(message: Message):
    a = await message.answer_dice(emoji="🎰")
    await asyncio.sleep(4)
    slots_value = a.dice.value 
    
    await message.answer(f"ваши очки: {slots_value}", reply_to_message_id=a.message_id)
    
@router.message(F.text == "Помощь" )
async def hii(message: Message):
    await message.answer(''' Чтобы играть нажмите Игры
                             когда вы играете вам будут начислятся балы''')

@router.message(F.text == "Посхалка" )
async def hii(message: Message):
    photo = FSInputFile('C:\\Users\\USER\\Desktop\\python\\prikolchik_tgBot\\ascii-art.png')
    await message.answer_photo(photo=photo)
    
@router.message(F.text == "Игры" )
async def hii(message: Message):
    await message.answer("Выберите игру:", reply_markup=kb.game)
    
@router.callback_query(F.data == "football" )
async def hii(callback: CallbackQuery):
    await callback.answer("кидаем мяч", show_alert=False)
    a = await callback.message.answer_dice(emoji="⚽")
    await asyncio.sleep(4)
    football_value = a.dice.value 
    if football_value in (3, 4, 5):
        await callback.message.answer(f"гол! ", reply_to_message_id=a.message_id)    
    elif football_value == 2:
        await callback.message.answer(f"в штангу ", reply_to_message_id=a.message_id)
    else:
        await callback.message.answer(f"промах ", reply_to_message_id=a.message_id)
    
    
@router.callback_query(F.data == "basketball" )
async def hii(callback: CallbackQuery):
    await callback.answer("кидаем мяч", show_alert=False)
    a = await callback.message.answer_dice(emoji="🏀")
    await asyncio.sleep(4)
    basketball_value = a.dice.value 
    if basketball_value in ( 4, 5):
        await callback.message.answer(f"попадание ", reply_to_message_id=a.message_id)    
    elif basketball_value in (1, 2):
        await callback.message.answer(f"промах", reply_to_message_id=a.message_id)
    else:
        await callback.message.answer(f"мяч застрял ", reply_to_message_id=a.message_id)
        
@router.callback_query(F.data == "darts" )
async def hii(callback: CallbackQuery):
    await callback.answer("кидаем дротик", show_alert=False)
    a = await callback.message.answer_dice(emoji="🎯")
    await asyncio.sleep(4)
    darts_value = a.dice.value 
    if darts_value == 6:
        await callback.message.answer(f"прямо в яблочко ", reply_to_message_id=a.message_id)    
    elif darts_value in (2, 3, 4, 5):
        await callback.message.answer(f"вы попали", reply_to_message_id=a.message_id)
    else:
        await callback.message.answer(f"не попали", reply_to_message_id=a.message_id)
        
@router.callback_query(F.data == "bowling" )
async def hii(callback: CallbackQuery):
    await callback.answer("кидаем шар", show_alert=False)
    a = await callback.message.answer_dice(emoji="🎳")
    await asyncio.sleep(4)
    bowling_value = a.dice.value 
    if bowling_value == 6:
        await callback.message.answer(f"страйк ", reply_to_message_id=a.message_id)    
    elif bowling_value in (2, 3, 4, 5):
        await callback.message.answer(f"попадание", reply_to_message_id=a.message_id)
    else:
        await callback.message.answer(f"мимо", reply_to_message_id=a.message_id)
        
@router.callback_query(F.data == "slots" )
async def hii(callback: CallbackQuery):
    await callback.answer("делаем прокрут", show_alert=False)
    a = await callback.message.answer_dice(emoji="🎰")
    await asyncio.sleep(4)
    slots_value = a.dice.value 
    
    await callback.message.answer(f"ваши очки: {slots_value}", reply_to_message_id=a.message_id)
    
@router.callback_query(F.data == "dice" )
async def hii(callback: CallbackQuery):
    await callback.answer("кидаем кубик", show_alert=False)
    a = await callback.message.answer_dice(emoji="🎲")
    await asyncio.sleep(4)
    dice_value = a.dice.value 
    await callback.message.answer(f"кубик показал {dice_value}", reply_to_message_id=a.message_id)
    
    
        
    
