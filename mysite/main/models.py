from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('category name', max_length=50)

    def __str__(self):
        return self.name

        


class Notebook(models.Model):

    COLOE_CHOISES = (
        ('Gray', 'gray'),
        ('Black', 'black'),
        ('Red', 'red')
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField('Notebook name', max_length=50)
    price = models.PositiveIntegerField('notebook price')
    img = models.ImageField('Notebook image', upload_to='media/nootebooks/')
    color = models.CharField(choices=COLOE_CHOISES, max_length=80)

    def __str__(self):
        return f'{self.name} - {self.price}'


