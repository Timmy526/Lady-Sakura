import motor.motor_asyncio
from datetime import datetime
from modules import config

mongo_url = config.get("MONGO", "URL")

cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
birthdaydoc = cluster["sakura"]["birthday"]
#[database][collection]


async def setBirthday(member, date):
    await birthdaydoc.insert_one({
        "id": member.id,
        "date": datetime.strptime(date, "%m/%d/%Y")
    })
  
async def findBirthdays():
    return await birthdaydoc.find({}).to_list(None)

async def removeBirthday(member):
    await birthdaydoc.delete_many({
        "id": member.id
    })