from django.test import TestCase
from .models import Meal, Category


class MealTestCase(TestCase):

    def setUp(self):
        new_category = Category.objects.create(name="Quick Meal", slug="Quick")
        new_meal = Meal.objects.create(
            name = 'Classic Burger',
            description = "Hamburger with chesse and tomato",
            celiac = False,
            vegan = False,
            delivery = True,
            price = 150
        )
        new_meal.category.add(new_category)

    def test_check_meal(self):
        category = Category.objects.get(name="Quick Meal")
        burger = Meal.objects.get(name="Classic Burger")
        self.assertIn(category.id, list(burger.category.values_list('id', flat=True)))
        self.assertFalse(burger.vegan)
        self.assertNotEqual(burger.price, 10000)
        self.assertIn