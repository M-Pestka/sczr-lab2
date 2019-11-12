import os
from argparse import ArgumentParser
import re
import pandas as pd

def get_folder_data(folder_name):
    files_in_folder = os.listdir(folder_name)
    if('server.txt' not in files_in_folder):
        raise Exception('No server file in folder {}', folder_name)

    concatenated = None

    for client_file in [f for f in files_in_folder if f.startswith('cli_')]:
        tmp_data = pd.read_csv(os.path.join(folder_name, client_file), header = None)
        tmp_data['file_name'] = client_file

        if(concatenated is None):
            concatenated = tmp_data
        else:
            concatenated = concatenated.append(tmp_data)

    return concatenated


parser = ArgumentParser()
parser.add_argument('--output', type = str, help = 'name of output files', required = True)
args = parser.parse_args()

folders = os.listdir()
folders = [f for f in folders if re.match('^folder_[0-9]+_[0-9]+$', f) is not None]
print('Analizawanie danych z folderów: \n {}'.format(folders))

concatenated = None
for folder in folders:
    folder_data = get_folder_data(folder)
    folder_data['folder'] = folder
    if(concatenated is None):
        concatenated = folder_data
    else:
        concatenated = concatenated.append(folder_data)

concatenated.to_csv(args.output, index = False)
