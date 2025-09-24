from enum import Enum

from jproperties import Properties

from anubis.core.errors import InvalidArgumentException


class ExecutionMode(Enum):
    GUI = "GUI"
    CLI = "CLI"

    @staticmethod
    def from_value(value: str):
        if value in ('gui', 'GUI'):
            result = ExecutionMode.GUI
        elif value in('cli', 'CLI'):
            result = ExecutionMode.CLI
        else:
            raise InvalidArgumentException(f'Unknown Execution Mode ${value}')

        return result

class AnubisConfigs:

    def __new__(cls):
        if not hasattr(cls, '__instance__'):
            cls.__instance__ = super(AnubisConfigs, cls).__new__(cls)
        return cls.__instance__

    def __init__(self):
        self.configs = Properties()
        with open('app-config.properties', 'rb') as config_file:
            self.configs.load(config_file)

    def get_json_database_location(self):
        result = self.configs.get("json_database_location")
        return result[0] if result else ""

    def get_execution_mode(self):
        result = self.configs.get("execution_mode")
        return ExecutionMode.from_value(result[0])
