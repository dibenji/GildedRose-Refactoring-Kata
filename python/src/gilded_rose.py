class GildedRose(object):
    @classmethod
    def decrease_quality(cls, item):
        if (item.quality - 1) < 0:
            pass
        else:
            item.quality -= 1

    @classmethod
    def increase_quality(cls, item):
        if (item.quality + 1) > 50:
            pass
        else:
            item.quality += 1

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        GildedRose.decrease_quality(item)
            else:
                if item.quality < 50:
                    GildedRose.increase_quality(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                GildedRose.increase_quality(item)
                        if item.sell_in < 6:
                            if item.quality < 50:
                                GildedRose.increase_quality(item)

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                GildedRose.decrease_quality(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        GildedRose.increase_quality(item)
