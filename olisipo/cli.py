import cmd
from getpass import getpass

from olisipo.data import repository_provider, Repository, Secret
from olisipo.encryption import EncryptionEngine
from olisipo.operations import Operations


class CLI(cmd.Cmd):
    prompt = ">> "
    intro = "Hello, welcome to Olisipo"

    def __init__(self, operations: Operations):
        super().__init__()

        self.operations = operations

    def do_add(self, line):
        split_input = line.split()
        self.operations.add_entry(Secret(name=split_input[0], value=split_input[1]))

    def do_get(self, line):
        secret_value = self.operations.get_entry(secret_id=line)
        print(secret_value.value)

    def do_remove(self, line):
        self.operations.remove_entry(line)

    @staticmethod
    def do_q(line):
        return True


if __name__ == "__main__":
    CLI(Operations(
        repository=repository_provider(),
        password_provider=lambda: getpass("Password>> "),
        encryption_engine=EncryptionEngine()
    )).cmdloop()
