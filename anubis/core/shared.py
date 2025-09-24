from typing import Any

class Repository:
    def save(self, entity: Any) -> Any:
        raise NotImplementedError("Repository#save is not implemented")

    def get_by_id(self, entity_id: str) -> Any:
        raise NotImplementedError("Repository#get is not implemented")

    def list(self):
        raise NotImplementedError("Repository#list is not implemented")

    def delete(self, entity_id: str) -> None:
        raise NotImplementedError("Repository#delete is not implemented")
