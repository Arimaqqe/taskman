from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_db_name: str
    postgres_db_host: str
    postgres_db_port: int
    postgres_db_user: str
    postgres_db_pass: str

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.postgres_db_user}:{self.postgres_db_pass}@{self.postgres_db_host}:{self.postgres_db_port}/{self.postgres_db_name}"

    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.postgres_db_user}:{self.postgres_db_pass}@{self.postgres_db_host}:{self.postgres_db_port}/{self.postgres_db_name}"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
