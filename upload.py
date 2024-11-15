import os
from dotenv import load_dotenv
from setuptools import setup, find_packages

load_dotenv()
pypi_token = os.getenv('PYPI_TOKEN')

cached_lines = []
with open("./rites/_version.py", "r") as f:
    cached_lines = f.readlines()
    f.close()


def increment_version():
    cloned_lines = cached_lines.copy()

    cached_version = cloned_lines[2].split('=')[1].strip().replace('\"', '')
    new_version = ''

    print(f"Current version: {cached_version}")
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
        build_package(new_version)
        os.system(f'twine upload dist/* -u __token__ -p {pypi_token}')
    else:
        print('Aborted')


def build_package(pkgVersion):
    setup(
        name="rites",
        version=pkgVersion,
        description="Reclipse's Initial Try at Enhanced Simplicity or R.I.T.E.S. A simple and lightweight QoL module.",
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        author="Reclipse",
        maintainer="Reclipse",
        url="https://github.com/ReclipseTheOne/rites",
        packages=find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
        install_requires=[
            'colored>=2.2.4'
        ]
    )


increment_version()
