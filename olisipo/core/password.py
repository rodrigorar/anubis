from getpass import getpass

from olisipo.core.shared import Repository


class PasswordRepository(Repository):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PasswordRepository, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.password = None

    def save(self, entity: str):
        if not self.password:
            self.password = entity

    def get(self) -> str:
        return self.password


class PasswordProvider:

    def __init__(self, password_repository: Repository):
        self.password_repository = password_repository

    def get_password(self) -> str:
        if not self.password_repository.get():
            self.password_repository.save(getpass("Password >>> "))
        return self.password_repository.get()

def password_repository_provider() -> Repository:
    return PasswordRepository()