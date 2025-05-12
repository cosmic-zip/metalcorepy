from ninja import Schema

class LoginSchema(Schema):
    email: str
    password: str

class TokenSchema(Schema):
    access_token: str
    token_type: str = "bearer"