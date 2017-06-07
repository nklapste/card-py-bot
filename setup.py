from setuptools import setup

setup(
    name="card-py-bot",
    author="Nathan Klapstein",
    author_email="nklapste@ualberta.ca",
    version="1.0",
    description="A Discord Bot for parsing magic card links",
    url="https://github.com/nklapste/card-py-bot",
    download_url="https://github.com/nklapste/card-py-bot/archive/master.zip",
    packages=["card_py_bot"],
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
            'card-py-bot = card_py_bot.__main__:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.5'
    ]
)
