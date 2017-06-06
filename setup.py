from distutils.core import setup

setup(
    name="card-py-bot",
    author="Nathan Klapstein",
    author_email="nklapste@ualberta.ca",

    packages=["card-py-bot"],
    package_data={
        '': ['README.md'],
        'card-py-bot': ['mana_config.txt', 'MANA_ICONS/*.gif']
    },

    install_requires=[
        'beautifulsoup4',
        'discord.py'
    ],
    entry_points={
        'console_scripts': [
            'card-py-bot = card_py_bot.__main__:main',
        ],
    },
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],



)
