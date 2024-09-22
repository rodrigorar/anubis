from dataclasses import dataclass
from typing import Any


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


def repository_provider() -> Repository:
    return InMemoryPasswordRepository()