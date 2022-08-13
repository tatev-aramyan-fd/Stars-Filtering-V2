from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

filename = config["files"]["filename1"]