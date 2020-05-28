'''Config Parser example to simulate Dev and Prod environment'''
import configparser

class MyConfigParser:
    """Implement your own Config Parser methods"""
    def __init__(self, config_file_path):
        """Initialize config object with file name"""
        self.config_file_path = config_file_path
        self.config = configparser.ConfigParser()

    def print_all_config_contents(self):
        """print all contents of config file"""
        self.config.read(self.config_file_path)
        for section in self.config.sections():
            for key in self.config[section]:
                print("Section: {0} \t Key: {1} \t Value: {2}".\
                      format(section, key, self.config.get(section, key)))

    def write_config_contents(self, ini_contents):
        """Write the given config into ini file"""
        with open(self.config_file_path, 'w') as config_file_to_write:
            self.config.read_dict(ini_contents)
            self.config.write(config_file_to_write)

    def add_section_to_config_contents(self, section_dict):
        """Add a new section into the ini file"""
        self.config.read(self.config_file_path)
        for section in section_dict.keys():
            self.config.add_section(section)
            for key in section_dict[section].keys():
                self.config.set(section, key, section_dict[section].get(key))
        with open(self.config_file_path, 'w') as config_file_to_add_sec:
            self.config.write(config_file_to_add_sec)

    def update_key_vallue(self, section_name, key_name, new_value):
        """Update the existing key value into new one"""
        self.config.read(self.config_file_path)
        self.config.set(section_name, key_name, new_value)
        with open(self.config_file_path, 'w') as config_file_to_update_value:
            self.config.write(config_file_to_update_value)

if __name__ == "__main__":
    DICT_VALUE = {"DEFAULT": {"host":"localhost"}, \
                   "DEV":{"Telemetry":"dev", "DB":"devDB", "install":"local"},\
                   "PROD":{"Telemetry":"prod", "DB":"prodDB", "install":"deployment"},\
                   "TEST":{"Telemetry":"test", "DB":"testDB", "install":"test-srv"}\
                  }
    CONFIG_PARSER_OBJ = MyConfigParser("app.config")
    CONFIG_PARSER_OBJ.write_config_contents(DICT_VALUE)
    CONFIG_PARSER_OBJ.print_all_config_contents()
    CONFIG_PARSER_OBJ.update_key_vallue("TEST", "install", "test-env")
    CONFIG_PARSER_OBJ.print_all_config_contents()
    CONFIG_PARSER_OBJ.add_section_to_config_contents\
                        ({"PDT":{"Telemetry":"pdt", "DB":"pdtDB", "install":"pdt-env"}})
    CONFIG_PARSER_OBJ.print_all_config_contents()
