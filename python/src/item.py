class Item:
    def __init__(self, name, sell_within_days, quality_value):
        self.name = name
        self.sell_within_days = sell_within_days
        self.quality_value = quality_value

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_within_days, self.quality_value)
