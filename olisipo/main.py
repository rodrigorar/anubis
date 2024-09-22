import cmd
from dataclasses import dataclass
from typing import Any


@dataclass
class Password:

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

    def save(self, entity: Password):
        self.database[entity.name] = entity

    def get(self, entity_id: str) -> Password:
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
        self.repository.save(Password(split_input[0], split_input[1]))

    def do_edit(self, line):
        split_input = line.split()
        self.repository.save(Password(split_input[0], split_input[1]))

    def do_get(self, line):
        result = self.repository.get(line)
        print(result.value)

    def do_remove(self, line):
        self.repository.delete(line)

    def do_quit(self, line):
        print("Exiting")
        return True


if __name__ == "__main__":
    CLI(InMemoryPasswordRepository()).cmdloop()
