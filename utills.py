import math, time

async def progress_for_pyrogram(current, total, udtype, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        progress = "[{0}{1}] \n**📊 Pʀᴏɢʀᴇss:** `{2}%`".format(
            ''.join(["▰" for i in range(math.floor(percentage / 5))]),
            ''.join(["▱" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))
        try: await message.edit(f"{udtype}\n\n{progress}")
        except: pass
