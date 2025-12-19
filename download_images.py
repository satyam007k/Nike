import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nike.settings')
django.setup()

from nikeapp.models import Product
import urllib.request
from django.core.files.base import ContentFile

for product in Product.objects.all():
    if product.image and product.image.name.startswith('http'):
        try:
            with urllib.request.urlopen(product.image.name) as response:
                image_data = response.read()
            filename = f"{product.slug}.png"
            product.image.save(filename, ContentFile(image_data), save=True)
            print(f"Downloaded for {product.name}")
        except Exception as e:
            print(f"Failed for {product.name}: {e}")