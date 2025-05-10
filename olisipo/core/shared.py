from typing import Any

class Repository:
    def save(self, entity: Any) -> Any:
        ...

    def get(self, entity_id: str) -> Any:
        ...

    def list(self):
        ...

    def delete(self, entity_id: str) -> None:
        ...
