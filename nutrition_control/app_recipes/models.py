from django.db import models


class Recipe(models.Model):
    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    title = models.CharField(max_length=1000, verbose_name='название')
    image = models.ImageField(upload_to='recipes_img', verbose_name='изображение')
    proteins = models.FloatField(verbose_name='белки')
    fats = models.FloatField(verbose_name='жиры')
    carbohydrates = models.FloatField(verbose_name='углеводы')
    energy = models.FloatField(verbose_name='энергетическая ценность')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title


class Product(models.Model):
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    title = models.CharField(max_length=1000, verbose_name='название')
    proteins = models.FloatField(verbose_name='белки')
    fats = models.FloatField(verbose_name='жиры')
    carbohydrates = models.FloatField(verbose_name='углеводы')
    energy = models.FloatField(verbose_name='энергетическая ценность')

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'

    product = models.OneToOneField(
        'Product',
        related_name='ingredient',
        verbose_name='продукт',
        on_delete=models.CASCADE
    )
    weight = models.FloatField(verbose_name='масса')
    recipe = models.ForeignKey(
        'Recipe',
        related_name='ingredient',
        on_delete=models.CASCADE,
        verbose_name='рецепт'
    )

    def __str__(self):
        return self.product.title
