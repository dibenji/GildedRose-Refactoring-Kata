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
        elif 5 >= item.sell_in >= 0:
            cls.increase_quality(item)
            cls.increase_quality(item)
            cls.increase_quality(item)
        elif 0 > item.sell_in:
            item.quality = 0

    @classmethod
    def update_conjured_item(self, item):
        item.quality -= 2

    @classmethod
    def update_item(cls, item):
        if item.name.lower() == "aged brie":
            cls.update_aged_brie(item)
        elif "sulfuras" in item.name.lower():
            cls.update_sulfuras(item)
        elif "backstage pass" in item.name.lower():
            cls.update_backstage_pass(item)
        elif "conjured" in item.name.lower():
            cls.update_conjured_item(item)
        item.sell_in -= 1

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)
