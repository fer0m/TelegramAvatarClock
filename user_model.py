from pydantic import BaseModel


class UserConfig(BaseModel):
    api_id: str
    api_hash: str
    phone: str
    secret_tg_key: str = None

