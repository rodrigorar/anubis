import json
import os
from dataclasses import dataclass
from pathlib import Path

from anubis.core.shared import Repository


@dataclass
class Secret:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value



class JsonRepository(Repository):
    DATABASE_LOCATION = Path.home()/".anubis"
    DATABASE = DATABASE_LOCATION/"database.json"

    def __init__(self):
        if not os.path.exists(self.DATABASE_LOCATION):
            print("Anubis working doesn't exist, creating")
            os.mkdir(self.DATABASE_LOCATION)
        if not os.path.exists(self.DATABASE):
            print("File does not exist, creating")
            with open(self.DATABASE, 'w') as f:
                f.write("")

    def load_database(self, file):
        return json.loads(file.read()) if os.stat(self.DATABASE).st_size != 0 else {}

    def save(self, entity: Secret):
        with open(self.DATABASE, 'r+') as db:
            data = self.load_database(db)

            data[entity.name] = entity.value

            db.seek(0) # Rewrite the entire file
            db.truncate()

            json.dump(data, db)

    def get(self, entity_id: str) -> Secret:
        with open(self.DATABASE) as db:
            data = self.load_database(db)
            result = Secret(entity_id, data.get(entity_id, ""))
        return result

    def list(self):
        with open(self.DATABASE) as db:
            data = self.load_database(db)
            result = data.keys()
        return result

    def delete(self, entity_id):
        with open(self.DATABASE, 'r+') as db:
            data = self.load_database(db)

            if data.get(entity_id) is not None:
                del data[entity_id]

            db.seek(0)  # Rewrite the entire file
            db.truncate()

            json.dump(data, db if db is not None else {})




def repository_provider() -> Repository:
    return JsonRepository()


