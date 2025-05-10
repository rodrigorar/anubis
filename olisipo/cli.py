#!/usr/bin/env python3

import cmd
from getpass import getpass

import clipboard

from olisipo.core.data import repository_provider, Secret
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

        split_input = line.split()
        self.operations.add_entry(Secret(name=split_input[0], value=split_input[1]))

    def do_get(self, line):
        'Get secret with (get <entry-name>)'

        try:
            secret_value: Secret = self.operations.get_entry(secret_id=line)
            clipboard.copy(secret_value.value)
        except Exception as e:
            print(e)
            print('Failed to fetch secret')

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
            print('No permissions to remove secret')

    @staticmethod
    def do_q(line):
        'Quit the application'

        return True


def main():
    CLI(Operations(
        repository=repository_provider(),
        password_provider=lambda: getpass("Password>> "),
        encryption_engine=EncryptionEngine()
    )).cmdloop()


if __name__ == "__main__":
    main()
