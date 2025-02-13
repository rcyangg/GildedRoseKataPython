# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
# Abstract class for item behavior
class ItemBehavior(ABC):
    def __init__(self, item: Item):
        super().__init__()
        self.item = item

    @abstractmethod
    def update_quality(self):
        pass


# Concrete sub-class for different items
class NomalItem(ItemBehavior):
    def update_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1
        self.item.sell_in -= 1
        # Once the sell by date has passed, Quality degrades twice as fast
        if self.item.sell_in < 0 and self.item.quality > 0:
            self.item.quality -= 1

class AgedBrie(ItemBehavior):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1
        self.item.sell_in -= 1

class BackstagePasses(ItemBehavior):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1
            if self.item.sell_in < 11 and self.item.quality < 50:
                self.item.quality += 1
            if self.item.sell_in < 6 and self.item.quality < 50:
                self.item.quality += 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0

class Sulfuras(ItemBehavior):
    def update_quality(self):
        # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
        pass


class Conjured(ItemBehavior):
    def update_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 2
        self.item.sell_in -= 1
        if self.item.sell_in < 0 and self.item.quality > 0:
            self.item.quality -= 2

# Use the Factory Pattern mentioned in the class (Feb 12)
class ItemFactory:
    @staticmethod
    def create(item: Item):
        if item.name == "Aged Brie":
            return AgedBrie(item)
        elif item.name == "Backstage passes":
            return BackstagePasses(item)
        elif item.name == "Sulfuras":
            return Sulfuras(item)
        elif item.name == "Conjured":
            return Conjured(item)
        else:
            return NomalItem(item)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        self.item_behaviors = {item: ItemFactory.create(item) for item in items}

    def update_quality(self):
        for item in self.items:
            self.item_behaviors[item].update_quality()

    # List all the items exist
    def get_items(self):
        return [str(item.name) for item in self.items]
    
    # List all items which sell in less than 5
    def get_items_sell_in_less_than_5(self):
        return [str(item.name) for item in self.items if item.sell_in < 5]