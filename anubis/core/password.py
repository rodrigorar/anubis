from anubis.core.shared import Repository

class PasswordRepository(Repository):
    def get(self) -> str:
        ...

    def clear(self):
        ...

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
