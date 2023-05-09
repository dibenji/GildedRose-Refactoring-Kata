# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

if __name__ == "__main__":
    print("OMGHAI!")
    items = [
        Item(name="+5 Dexterity Vest", sell_within_days=10, quality_value=20),
        Item(name="Aged Brie", sell_within_days=2, quality_value=0),
        Item(name="Elixir of the Mongoose", sell_within_days=5, quality_value=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_within_days=0, quality_value=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_within_days=-1, quality_value=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_within_days=15, quality_value=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_within_days=10, quality_value=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_within_days=5, quality_value=49),
        Item(name="Conjured Mana Cake", sell_within_days=3, quality_value=6),  # <-- :O
    ]

    days = 2
    import sys

    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
