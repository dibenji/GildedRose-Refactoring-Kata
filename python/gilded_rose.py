# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality_value > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality_value = item.quality_value - 1
            else:
                if item.quality_value < 50:
                    item.quality_value = item.quality_value + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_within_days < 11:
                            if item.quality_value < 50:
                                item.quality_value = item.quality_value + 1
                        if item.sell_within_days < 6:
                            if item.quality_value < 50:
                                item.quality_value = item.quality_value + 1

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_within_days = item.sell_within_days - 1
            if item.sell_within_days < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality_value > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality_value = item.quality_value - 1
                    else:
                        item.quality_value = item.quality_value - item.quality_value
                else:
                    if item.quality_value < 50:
                        item.quality_value = item.quality_value + 1


class Item:
    def __init__(self, name, sell_within_days, quality_value):
        self.name = name
        self.sell_within_days = sell_within_days
        self.quality_value = quality_value

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_within_days, self.quality_value)
