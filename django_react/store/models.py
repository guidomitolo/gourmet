from django.db import models
from users.models import Customer
from menu.models import Meal


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False, null=True, blank=False)
    transId = models.CharField(max_length=200, null=True)

    @property
    def total_order_price(self):
        return sum([order.total_price for order in self.ordermeal.all()])

    @property
    def total_order_quantity(self):
        return sum([order.quantity for order in self.ordenarproducto_set.all()])

    def __str__(self):
        return f"{self.customer}: Order n. {self.id}"


class OrderMeal(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.meal.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.meal.name}"


class Dispach(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    street = models.CharField(max_length=256, null=True)
    address = models.IntegerField(null=True)
    state = models.CharField(max_length=256, null=True)
    neighborhood = models.CharField(max_length=256, null=True)
    
    creationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order} - {self.address}"
    



