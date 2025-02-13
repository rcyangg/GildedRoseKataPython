# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(0, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(["Sulfuras"], all_items)

    # Test 1: (checks for logical errors)
    def test_sulfuras_should_not_decrease_sellin(self):
        items = [Item("Sulfuras", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(0, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # Test 2: (checks for logical errors)
    def test_backstage_passes_should_not_decrease_quality_when_sellin_positive(self):
        items = [Item("Backstage passes", 15, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        backstage_passes_item = items[0]
        self.assertEqual(26, backstage_passes_item.quality)
        self.assertEqual(14, backstage_passes_item.sell_in)
        self.assertEqual("Backstage passes", backstage_passes_item.name)
    
    # Test 3: (checks for logical errors)
    def test_conjured_items_should_degrade_twice_faster(self):
        items = [Item("Conjured", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        conjured_item = items[0]
        self.assertEqual(38, conjured_item.quality)
        self.assertEqual(9, conjured_item.sell_in)
        self.assertEqual("Conjured", conjured_item.name)
    
    # Test 4: (checks for logical errors)
    def test_backstage_passes_should_increase_2_quality_when_sellin_less_than_11(self):
        items = [Item("Backstage passes", 10, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        backstage_passes_item = items[0]
        self.assertEqual(27, backstage_passes_item.quality)
        self.assertEqual(9, backstage_passes_item.sell_in)
        self.assertEqual("Backstage passes", backstage_passes_item.name)
    
    # Test 5: (checks for logical errors)
    def test_backstage_passes_should_increase_3_quality_when_sellin_less_than_6(self):
        items = [Item("Backstage passes", 5, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        backstage_passes_item = items[0]
        self.assertEqual(28, backstage_passes_item.quality)
        self.assertEqual(4, backstage_passes_item.sell_in)
        self.assertEqual("Backstage passes", backstage_passes_item.name)

    # Test 6: (checks for syntax errors): use a function that not yet been created
    def test_gilded_rose_list_items_sell_in_less_than_5(self):
        items = [
            Item("Aged Brie", 3, 10),
            Item("Sulfuras", 10, 25),
            Item("Backstage passes", 2, 30),
        ]
        gilded_rose = GildedRose(items)
        expect_items = gilded_rose.get_items_sell_in_less_than_5()
        self.assertEqual(["Aged Brie", "Backstage passes"], expect_items)

if __name__ == '__main__':
    unittest.main()
