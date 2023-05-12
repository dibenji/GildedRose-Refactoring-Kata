class GildedRose(object):
    @classmethod
    def decrease_quality(cls, item):
        if (item.quality - 1) < 0:
            pass
        else:
            if item.sell_in < 0:
                item.quality -= 2
            else:
                item.quality -= 1

    @classmethod
    def increase_quality(cls, item):
        if (item.quality + 1) > 50:
            pass
        else:
            item.quality += 1

    @classmethod
    def update_aged_brie(cls, item):
        cls.increase_quality(item)

    @classmethod
    def update_sulfuras(cls, item):
        pass

    @classmethod
    def update_backstage_pass(cls, item):
        if 11 > item.sell_in > 5:
            cls.increase_quality(item)
            cls.increase_quality(item)
        elif 5 >= item.sell_in > 0:
            cls.increase_quality(item)
            cls.increase_quality(item)
            cls.increase_quality(item)

    @classmethod
    def update_item(cls, item):
        if "aged brie" in item.name.lower():
            cls.update_aged_brie(item)
        elif "sulfuras" in item.name.lower():
            cls.update_sulfuras(item)
        elif "backstage pass" in item.name.lower():
            cls.update_backstage_pass(item)
        item.sell_in -= 1

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.name != "Sulfuras, Hand of Ragnaros":
                    GildedRose.decrease_quality(item)
            else:
                GildedRose.increase_quality(item)
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        GildedRose.increase_quality(item)
                    if item.sell_in < 6:
                        GildedRose.increase_quality(item)

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            GildedRose.decrease_quality(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    GildedRose.increase_quality(item)
