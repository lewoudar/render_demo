import pathlib
from pydantic import BaseSettings


root_dir = pathlib.Path(__file__).parent.parent


class Settings(BaseSettings):
    database_url: str = str(root_dir / 'file.db')
    generate_schema: bool = False


settings = Settings()
