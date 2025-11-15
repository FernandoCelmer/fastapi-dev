from pydantic import BaseModel, EmailStr, SecretStr


class SchemaSignup(BaseModel):
    email: EmailStr
    username: str | None = None
    password: SecretStr
