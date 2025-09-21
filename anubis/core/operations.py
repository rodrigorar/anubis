from cryptography.fernet import InvalidToken

from anubis.core.password import PasswordProvider
from anubis.core.secrets import Secret, Repository
from anubis.core.encryption import EncryptionEngine

class Operations:

    def __init__(
            self,
            repository: Repository,
            password_provider: PasswordProvider,
            encryption_engine: EncryptionEngine
    ):
        self.repository = repository
        self.password_provider = password_provider
        self.encryption_engine = encryption_engine

    def add_entry(self, secret: Secret) -> None:
        assert secret, "No secret value has been provided"

        encrypted_value = self.encryption_engine.encrypt(secret.value, self.password_provider.get_password())
        self.repository.save(Secret(name=secret.name, value=encrypted_value))

    def get_entry(self, secret_id: str) -> Secret | None:
        assert secret_id, "Not secret id has been provided"

        result = self.repository.get(secret_id)
        decrypted_value = None
        if result:
            try:
                decrypted_value = self.encryption_engine.decrypt(result.value, self.password_provider.get_password())
            except InvalidToken:
                self.password_provider.clear_password()
                return self.get_entry(secret_id)
        else:
            print("No value returned from the repository")
        return Secret(secret_id, decrypted_value)

    def list_entries(self):
        return self.repository.list()

    def remove_entry(self, secret_id: str) -> None:
        assert secret_id, "No secret id has been provided"

        secret = self.repository.get(secret_id)
        if secret:
            decrypted_value = self.encryption_engine.decrypt(secret.value, self.password_provider.get_password())
            self.repository.delete(secret_id)
