import os
from dotenv import load_dotenv


load_dotenv(".env")
pypi_token = os.getenv('PYPI_TOKEN')

cached_lines = []
with open("./rites/_version.py", "r") as f:
    cached_lines = f.readlines()
    f.close()


def increment_version():
    cloned_lines = cached_lines.copy()

    cached_version = cloned_lines[2].split('=')[1].strip().replace('\"', '')
    new_version = ''

    print(f"Env version: {os.getenv('RITES_PKG_VERSION')} - Cached version: {cached_version}")
    choice = input(f'''
    1. Increment patch version
    2. Increment minor version and set patch to 0
    3. Increment major version and set patch and minor to 0
    4. Don't increment version
    5. Custom
    >''')
    add_label = input(f'''Add Label? (y/n)
>''').lower()

    if add_label == 'y':
        label = input('Label: ')
    else:
        label = ''

    if choice == '1':
        new_version = cloned_lines[2].split('=')[1].strip().replace('\"', '').split('.')
        new_version[2] = str(int(new_version[2]) + 1)
        new_version = '.'.join(new_version) + label
        cloned_lines[2] = f'__version__ = "{new_version}"\n'

    elif choice == '2':
        new_version = cloned_lines[2].split('=')[1].strip().replace('\"', '').split('.')
        new_version[1] = str(int(new_version[1]) + 1)
        new_version[2] = '0'
        new_version = '.'.join(new_version) + label
        cloned_lines[2] = f'__version__ = "{new_version}"\n'

    elif choice == '3':
        new_version = cloned_lines[2].split('=')[1].strip().replace('\"', '').split('.')
        new_version[0] = str(int(new_version[0]) + 1)
        new_version[1] = '0'
        new_version[2] = '0'
        new_version = '.'.join(new_version) + label
        cloned_lines[2] = f'__version__ = "{new_version}"\n'

    elif choice == '4':
        new_version = cached_version + label
        cloned_lines[2] = f'__version__ = "{new_version}"\n'

    elif choice == '5':
        new_version = input('Version: ')
        cloned_lines[2] = f'__version__ = "{new_version}"\n'

    accept_changes = input(f'''Old version: {cached_version} - New version: {new_version}
Accept changes? (y/n)
>''').lower()
    if accept_changes == 'y':
        with open("./rites/_version.py", "w") as f:
            f.writelines(cloned_lines)
            f.close()

        clean_dist = input(f"Cleaning dist folder to not upload redundant versions.\nPress 'y' to accept\n>")
        if (clean_dist == 'y'):
            if os.name == 'nt':
                os.system('rmdir /S /Q dist')
                os.system('mkdir dist')
            else:
                os.system('rm -rf dist')
                os.system('mkdir dist')

        build_package(new_version)
        os.system(f'twine upload dist/* -u __token__ -p {pypi_token}')
    else:
        print('Aborted')


def build_package(pkgVersion):
    env_lines = []
    with open('.env', 'r') as f:
        env_lines = f.readlines()
        f.close()
    env_lines[1] = f'RITES_PKG_VERSION={pkgVersion}\n'
    with open('.env', 'w') as f:
        f.writelines(env_lines)
        f.close()

    load_dotenv(".env")

    print(f"Running setup.py for version {pkgVersion}")
    os.system(f"python setup.py --version={pkgVersion} sdist bdist_wheel")


increment_version()
