from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

test_file = config["files"]["filename1"]


def get_filename():
    values = list(config['files'].values())
    print(values)
    filename = input("\nEnter the Filename to work with from mentioned above list => ")
    if filename in values:
        return filename
    else:
        raise ValueError("INVALID Filename")

