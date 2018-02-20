import sys
import yaml

from st2actions.runners.pythonrunner import Action

class ReadConfig(Action):
  def run(self, config_file, config_path):
    file_path = config_path + "/" + config_file
    try:
      file_handle =open(file_path)
    except IOError as err:
      return (False, err)

    try:
      yaml_dict = yaml.load(file_handle)
    except:
      return (False, "Failed to parse YAML, verify it is valid")
    finally:
      file_handle.close()
    #print yaml_dict
    return (True,yaml_dict)

