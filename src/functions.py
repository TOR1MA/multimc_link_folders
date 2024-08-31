import json
import os
import sys
from func_protection import save_rmdir, save_symlink


def open_cfg():
    with open('config.json') as f:
        return json.load(f)


def menu_return(input):
    if input.lower() in ("return", "r", "0"):
        return True
    elif input.lower() == 'exit':
        os.system('pause')
        sys.exit()


def create_selector(func_dict: dict[int | str, callable], selector_message: str):
    mreturn = False
    while not mreturn:
        user_input = input(selector_message)
        if user_input in func_dict:
            func_dict[user_input]()
        mreturn = menu_return(user_input)


def link(config):
    dir_dict = {}
    dir_list = [folder for folder in os.listdir(config['multimc_instances_folder'])
                if folder not in ['instgroups.json', '_LAUNCHER_TEMP']]
    for key, folder in enumerate(dir_list, 1):
        print(f'{key}: {folder}')
        dir_dict[key] = folder
    mreturn = False
    while not mreturn:
        user_input = input('Choose a minecraft instance:\n')
        mreturn = menu_return(user_input)
        try:
            instance = dir_dict[int(user_input)]
        except (ValueError, KeyError):
            if user_input in dir_dict.values():
                instance = user_input
            else:
                print('Enter a valid instance')
                continue
        folder = config['multimc_instances_folder'] + '/' + instance + '/.minecraft'
        subfolders = [f'{folder}/saves', f'{folder}/shaderpacks', f'{folder}/screenshots', f'{folder}/resourcepacks']
        minecraft_subfolders = [f'{config['root_folder']}/saves', f'{config['root_folder']}/shaderpacks',
                                f'{config['root_folder']}/screenshots', f'{config['root_folder']}/resourcepacks']
        for subfolder, minecraft_subfolder in zip(subfolders, minecraft_subfolders):
            if save_rmdir(subfolder) is False:
                continue
            save_symlink(minecraft_subfolder, subfolder)
