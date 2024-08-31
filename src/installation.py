import os
import json
from functions import menu_return
from func_protection import save_mkdir


def create_config():
    with open('config.json', 'x') as f:
        cfg = {
            "root_folder": "",
            "multimc_folder": "",
            "multimc_instances_folder": ""
            }
        f.write(json.dumps(cfg, indent=3))


def multimc_folder_select(config):
    mreturn = False
    while not mreturn:
        user_input = input('Enter a path to multimc root folder, like "/MultiMC":\n').replace('\\', '/')
        mreturn = menu_return(user_input)
        if not os.path.isdir(user_input) or not os.path.isdir(os.path.join(user_input, "instances")):
            print('Enter a valid path')
            continue
        else:
            config['multimc_folder'] = user_input
            config['multimc_instances_folder'] = user_input + '/instances'
            config_dump = json.dumps(config, indent=3)
            with open('config.json', 'w') as f:
                f.write(config_dump)
            print('Multimc folder selected')
            mreturn = True


def root_folder_select(config):
    def root_folder_selected(root_folder):
        config['root_folder'] = root_folder
        config_dump = json.dumps(config, indent=3)
        with open('config.json', 'w') as f:
            f.write(config_dump)
        print(root_selected)
        return True
    mreturn = False
    root_selected = 'Root folder selected'
    while not mreturn:
        user_input = input('''1. Enter a path to miecraft root folder;
2. Select default minecraft folder;
3. Create main folder in multimc:
''')
        match user_input.lower():
            case '1':
                localreturn = False
                while not localreturn:
                    user_input = input('Enter a minecraft folder, like "/.minecraft" or exit:\n').replace('\\', '/')
                    if not os.path.isdir(user_input):
                        print('Enter a valid path')
                        continue
                    localreturn = menu_return(user_input) or root_folder_selected(user_input)
            case '2':
                root_folder = os.environ['USERPROFILE'] + '/AppData/Roaming/.minecraft'
                mreturn = root_folder_selected(root_folder)
            case '3':
                instances_folders = ['instances_root_folder', 'instances_root_folder/saves',
                                     'instances_root_folder/shaderpacks', 'instances_root_folder/screenshots',
                                     'instances_root_folder/resourcepacks']
                for folder in instances_folders:
                    save_mkdir(os.path.join(config['multimc_folder']), folder)
                root_folder = config['multimc_folder'] + '/instances_root_folder'
                mreturn = root_folder_selected(root_folder)
        mreturn = menu_return(user_input)
