from product.models import ProductCategory

def navigation_categories_config(request):
    navigation_categories=ProductCategory.objects.filter(status=True)
    return {"navigation_categories":navigation_categories}