from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField()


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    create = models.DateTimeField(auto_now_add=True, null=True)
    amount = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(1000)
        ])
    discount = models.PositiveSmallIntegerField(default=0,
                                                validators=[
                                                    MaxValueValidator(100)
                                                ])
    sold = models.PositiveSmallIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.pk])

    def __str__(self):
        return self.name


class Employee(models.Model):
    JOB_CHOICES = (
        ('Custodian', 'Custodian'),
        ('Cashier', 'Cashier'),
        ('Manager', 'Manager'),
        ('Stock clerk', 'Stock clerk')
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(18)
        ])
    job = models.CharField(choices=JOB_CHOICES, max_length=20)


class Customer(models.Model):
    LEVEL_CHOICES = (
        ('N', 'Normal'),
        ('G', 'Golden'),
    )

    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=11)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=1)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    time = models.DateTimeField()
    price = models.PositiveIntegerField()
