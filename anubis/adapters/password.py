from anubis.core.password import PasswordRepository


class InMemoryPasswordRepository(PasswordRepository):

    def __new__(cls):
        if not hasattr(cls, '__instance__'):
            cls.__instance__ = super(InMemoryPasswordRepository, cls).__new__(cls)
        return cls.__instance__

    def __init__(self):
        self.password = None

    def save(self, entity: str):
        if not self.password:
            self.password = entity

    def get(self) -> str:
        return self.password

    def clear(self):
        self.password = None

def password_repository_provider() -> PasswordRepository:
    return InMemoryPasswordRepository()
