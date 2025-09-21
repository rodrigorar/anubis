from anubis.core.shared import Repository

# TODO: Refactor this to the infrastructure layer
class PasswordRepository(Repository):

    def __new__(cls):
        if not hasattr(cls, '__instance__'):
            cls.__instance__ = super(PasswordRepository, cls).__new__(cls)
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


class PasswordProvider:

    def __init__(self, password_repository: PasswordRepository, password_input):
        self.password_repository = password_repository
        self.password_input = password_input

    def get_password(self) -> str:
        if not self.password_repository.get():
            self.password_repository.save(self.password_input())
        return self.password_repository.get()

    def clear_password(self):
        self.password_repository.clear()

def password_repository_provider() -> Repository:
    return PasswordRepository()