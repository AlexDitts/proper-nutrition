from django.db.models import Manager, QuerySet


class RecipeManager(Manager):

    def exclude_products(self, *, products: list) -> QuerySet:
        q = self.get_queryset().exclude(ingredient__product__title__in=products)
        return q
