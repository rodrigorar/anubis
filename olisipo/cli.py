#!/usr/bin/env python3

import cmd
from getpass import getpass

import clipboard

from olisipo.core.password import PasswordProvider, password_repository_provider
from olisipo.core.secrets import repository_provider, Secret
from olisipo.core.encryption import EncryptionEngine
from olisipo.core.operations import Operations


class CLI(cmd.Cmd):
    prompt = ">> "
    intro = "Hello, welcome to Olisipo, a local simple secrets manager"

    def __init__(self, operations: Operations):
        super().__init__()

        self.operations = operations

    def do_add(self, line):
        'Add new secret with (add <entry-name> <entry-secret>)'

        secret_name = line
        self.operations.add_entry(Secret(name=secret_name, value=getpass("Secret >>> ")))

    def do_get(self, line):
        'Get secret with (get <entry-name>)'

        try:
            secret_value: Secret = self.operations.get_entry(secret_id=line)
            clipboard.copy(secret_value.value)
            print("The secret has been copied to your clipboard!")
        except Exception as e:
            print(e)

    def do_list(self, line):
        'List all stored secret keys'

        entry_keys = self.operations.list_entries()
        [print(entry_key) for entry_key in entry_keys]

    def do_remove(self, line):
        'Remove entry with (remove <entry-name>)'

        try:
            self.operations.remove_entry(line)
        except Exception as e:
            print(e)

    @staticmethod
    def do_q(line):
        'Quit the application'

        return True


def main():
    CLI(Operations(
        repository=repository_provider(),
        password_provider=PasswordProvider(password_repository_provider(), lambda: getpass("Password >>> ")),
        encryption_engine=EncryptionEngine()
    )).cmdloop()


if __name__ == "__main__":
    main()
