"""pytests for webscraping functions in get_card.py"""

import pytest

from card_py_bot.scrape import scrape_card


@pytest.mark.parametrize("card_url,expected_card_data", [

    (
            "http://gatherer.wizards.com/Pages/Card/Details."
            "aspx?multiverseid=74626",
            {
                "P/T": "5 / 4",
                "Types": "Legendary Creature  — Rat Ninja",
                "image_url": "http://gatherer.wizards.com/Handlers/Image."
                             "ashx?multiverseid=74626&type=card",
                "Rarity": "Rare",
                "Expansion": "Betrayers of Kamigawa",
                "Artist": "Wayne Reynolds",
                "Card Number": "71",
                "Card Name": "Ink-Eyes, Servant of Oni",
                "Converted Mana Cost": "6"
            }
    ),
    (
            "http://gatherer.wizards.com/Pages/Card/Details."
            "aspx?multiverseid=13821",
            {
                "Artist": "Jeff Laubenstein", "Card Number": "92",
                "Converted Mana Cost": "1",
                "image_url": "http://gatherer.wizards.com/Handlers/Image."
                             "ashx?multiverseid=13821&type=card",
                "Card Name": "Landslide", "Expansion": "Urza's Destiny",
                "Rarity": "Uncommon",
                "Types": "Sorcery",
                "Card Text": "Sacrifice any number of Mountains. Landslide "
                             "deals that much damage to target player.",
                "Flavor Text": "Sometimes the mountain takes.â€”Keldon saying"
            }

    )

])
def test_scrape_card(card_url, expected_card_data):
    card_data = scrape_card(card_url)
    for card_data_element in expected_card_data:
        assert card_data[card_data_element] == \
               expected_card_data[card_data_element]
