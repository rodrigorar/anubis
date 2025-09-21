from jproperties import Properties

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
