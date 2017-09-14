"""Emoji config string generator"""

import re
import json
from logging import getLogger

from card_py_bot import MANA_CONFIG_PATH


__log__ = getLogger(__name__)


mana_id_dict={":15m:": "15", ":13m:": "13", ":wbm:": "White or Black",
 ":Energy:": "Energy", ":10m:": "10", ":7m:": "7", ":Untap:": "Untap",
 ":brm:": "Black or Red", ":bpm:": "Phyrexian Black", ":rgm:": "Red or Green",
 ":9m:": "9", ":8m:": "8", ":1m:": "1", ":gum:": "Green or Blue",
 ":2wm:": "Two or White", ":wpm:": "Phyrexian White", ":4m:": "4",
 ":12m:": "12", ":rm:": "Red", ":bm:": "Black", ":wum:": "White or Blue",
 ":rwm:": "Red or White", ":2bm:": "Two or Blue", ":gpm:": "Phyrexian Green",
 ":gm:": "Green", ":14m:": "14", ":bgm:": "Black or Green", ":3m:": "3",
 ":5m:": "5", ":Tap:": "Tap", ":1000000m:": "1000000",
 ":upm:": "Phyrexian Blue", ":2gm:": "Two or Green", ":rpm:": "Phyrexian Red",
 ":2m:": "2", ":6m:": "6", ":2rm:": "Two or Red", ":gwm:": "Green or White",
 ":wm:": "White", ":um:": "Blue", ":16m:": "16", ":urm:": "Blue or Red",
 ":ubm:": "Blue or Black", ":11m:": "11"}



def print_ids():
    """Return a string of all the mana ids (in order) for config setup
    in discord"""
    config_string = "?save_setup\n"
    for short_emoji_id in mana_id_dict:
        config_string += ("\\\\{}\n".format(short_emoji_id))

    return config_string


def load_mana_config():
    """Load the emoji mana config into a mana dict"""
    with open(MANA_CONFIG_PATH, "r") as file:
        mana_config = json.load(file)
    mana_dict = dict()
    for short_emoji_id in mana_config:
        emoji = mana_config[short_emoji_id]
        if not emoji["discord_raw_id"]:
            mana_dict[emoji["web_id"]] = "ERROR: NO ID Configured " \
                                         "for {}".format(emoji["web_id"])
        else:
            mana_dict[emoji["web_id"]] = emoji["discord_raw_id"]

    __log__.debug("WOTC Magic mana to Discord emoji "
                  "dictionary constructed: {}".format(mana_dict))
    return mana_dict


MANA_DICT = load_mana_config()



def parse_raw_emoji_id(raw_emoji_id) -> str:
    """Parse a raw emoji id to short emoji id"""

    m = re.search(":[A-Za-z0-9]*:", raw_emoji_id)
    return m.group(0)

def save_mana_config(raw_emoji_ids):
    """Save the emoji mana config"""

    try:
        mana_config = json.load(MANA_CONFIG_PATH)
    except Exception as e:
        # if no mana config file is found initialize a new one
        mana_config = dict()

        for short_emoji_id in mana_id_dict:
            mana_config[short_emoji_id]={
                "web_id":mana_id_dict[short_emoji_id],
                "discord_raw_id": None
            }

    __log__.info("Saving emoji ids: {}".format(raw_emoji_ids))

    for raw_emoji_id in raw_emoji_ids:

        short_emoji_id = parse_raw_emoji_id(raw_emoji_id)

        if short_emoji_id not in mana_id_dict:
            raise KeyError("Short Discord emoji id is unknown: "
                           "{}".format(short_emoji_id))

        mana_config[short_emoji_id]={
                "web_id":mana_id_dict[short_emoji_id],
                "discord_raw_id": raw_emoji_id
            }

    with open(MANA_CONFIG_PATH, "w") as file:
        json.dump(mana_config, file, indent=4)

    # update MANA_DICT global
    global MANA_DICT
    MANA_DICT = load_mana_config()


# test
# save_mana_config(["<:2m:314222462655004674>"])
# # test
# # print(load_mana_config())
#
# print(MANA_DICT["5"], MANA_DICT["2"])
# save_mana_config(["<:5m:314222462655004674>"])
# print(MANA_DICT["5"], MANA_DICT["2"])