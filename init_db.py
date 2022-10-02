"""
This is a script to run one time to initialize the database.
Once you have your database set up on render, make sure to set the environment
variable DATABASE_URL with the external database url before running this script.
"""
import asyncio

from tortoise import Tortoise

from render_demo.config import settings


async def init():
    await Tortoise.init(
        db_url=settings.database_url,
        modules={'models': ['render_demo.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


asyncio.run(init())
