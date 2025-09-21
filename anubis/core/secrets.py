from dataclasses import dataclass

from anubis.core.shared import Repository


@dataclass
class Secret:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value


class SecretsRepository(Repository):
    ...
