""" card-py-bot setup """

from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="card-py-bot",
    author="Nathan Klapstein",
    author_email="nklapste@ualberta.ca",
    description="A Discord Bot for parsing WOTC Magic card links",
    long_description=readme(),
    version="3.0.5", # new tag
    url="https://github.com/nklapste/card-py-bot",
    download_url="https://github.com/nklapste/card-py-bot/archive/1.4.tar.gz",
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(exclude=["tests"]),
    license="MIT",
    package_data={
        "": ["README.md"],
        "card_py_bot": ["mana_config.txt", "MANA_ICONS/*.gif"],
    },
    install_requires=[
        "beautifulsoup4",
        "html5lib",
        "discord.py"
    ],
    entry_points={
        "console_scripts": ["card-py-bot = card_py_bot.__main__:main"],
    },
)
