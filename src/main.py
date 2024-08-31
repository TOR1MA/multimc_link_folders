import os
import installation as inst
import functions as func


if __name__ == '__main__':
    try:
        config = func.open_cfg()
    except FileNotFoundError:
        inst.create_config()
        config = func.open_cfg()
    print('''In all subsequent menus, you can type “exit” to exit program and
“return” or "0" to return to previous menu.
''')

    if not os.path.isdir(config['multimc_instances_folder']):
        print('Cant find multimc folder')
        inst.multimc_folder_select(config)
    print(config)
    if not os.path.isdir(config['root_folder']):
        print('Cant find root folder')
        inst.root_folder_select(config)
    func.create_selector({'1': func.link, '3': inst.multimc_folder_select, '4': inst.root_folder_select},
                         '''1. Link folders;
2. Link CurseForge instances;
3. Change multimc folder;
4. Change root folder:
''')
