import base64
import cmd
from dataclasses import dataclass
from getpass import getpass
from typing import Any

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from olisipo.encryption import encrypt_entry, decrypt_entry


@dataclass
class Secret:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

class Repository:
    def save(self, entity: Any) -> Any:
        ...

    def get(self, entity_id: str) -> Any:
        ...

    def delete(self, entity_id: str) -> None:
        ...


class InMemoryPasswordRepository(Repository):
    database = {}

    def save(self, entity: Secret):
        self.database[entity.name] = entity

    def get(self, entity_id: str) -> Secret:
        return self.database.get(entity_id)

    def delete(self, entity_id):
        self.database.pop(entity_id, None)


class CLI(cmd.Cmd):
    prompt = ">> "
    intro = "Hello, welcome to Olisipo"

    def __init__(self, repository: Repository):
        super().__init__()

        self.repository = repository

    def do_add(self, line):
        split_input = line.split()
        password = getpass("Password>> ")
        encrypted_value = encrypt_entry(split_input[1], password)
        self.repository.save(Secret(split_input[0], encrypted_value))

    def do_edit(self, line):
        split_input = line.split()
        self.repository.save(Secret(split_input[0], split_input[1]))

    def do_get(self, line):
        result = self.repository.get(line)
        password = getpass("Password>> ")
        decrypted_value = decrypt_entry(result.value, password)
        print(decrypted_value)

    def do_remove(self, line):
        self.repository.delete(line)

    def do_quit(self, line):
        print("Exiting")
        return True


if __name__ == "__main__":
    CLI(InMemoryPasswordRepository()).cmdloop()
