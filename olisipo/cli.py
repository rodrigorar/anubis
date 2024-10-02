import cmd
from getpass import getpass

from olisipo.data import repository_provider, Repository, Secret
from olisipo.encryption import EncryptionEngine
from olisipo.operations import Operations


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
            secret_value = self.operations.get_entry(secret_id=line)
            print(secret_value.value)
        except:
            print('Failed to fetch secret')

    def do_remove(self, line):
        'Remove entry with (remove <entry-name>)'

        try:
            self.operations.remove_entry(line)
        except:
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
