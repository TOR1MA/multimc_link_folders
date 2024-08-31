import os


def save_mkdir(path):
    try:
        os.mkdir(path)
        print(path, 'created')
    except FileExistsError:
        print(path, 'already exist')
        return False
    except OSError:
        print('Privilege error, run program with administrator privileges')


def save_rmdir(dir):
    try:
        os.rmdir(dir)
    except FileNotFoundError:
        pass
    except OSError:
        print(dir, 'is not empty')
        return False


def save_symlink(src, dst):
    try:
        os.symlink(src, dst)
        print(dst, "linked")
    except OSError:
        print('Privilage error, run program with a administrator privilages')
        return False
