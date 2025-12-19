import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nike.settings')
django.setup()

from nikeapp.models import Product

bad_products = {
    'Running Shoes': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f37fca8-6bce-43e7-ad07-f57ae3c13142/nike-air-max-270-mens-shoes-KkLcGR.png',
    'Jacket': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/awjogtdnqxniqqk0wpgf/sportswear-club-fleece-mens-joggers-2N7Z5H.png',
    'Air Jordan 1': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f37fca8-6bce-43e7-ad07-f57ae3c13142/air-jordan-4-retro-mens-shoes-4V54Jl.png',
    'Nike React Element': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f37fca8-6bce-43e7-ad07-f57ae3c13142/nike-air-max-270-mens-shoes-KkLcGR.png',
    'Nike Sportswear Club Fleece': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/awjogtdnqxniqqk0wpgf/tech-fleece-windrunner-mens-hoodie-5R8Q8W.png',
    'Nike Windrunner Jacket': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/awjogtdnqxniqqk0wpgf/sportswear-club-fleece-mens-joggers-2N7Z5H.png',
    'Nike Pegasus': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f37fca8-6bce-43e7-ad07-f57ae3c13142/nike-air-max-270-mens-shoes-KkLcGR.png',
    'Nike Therma Hoodie': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/awjogtdnqxniqqk0wpgf/tech-fleece-windrunner-mens-hoodie-5R8Q8W.png',
    'Nike Swoosh Cap': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f37fca8-6bce-43e7-ad07-f57ae3c13142/nike-elite-mens-socks-2HcpFm.png'
}

for name, url in bad_products.items():
    p = Product.objects.get(name=name)
    p.image = url
    p.save()
    print(f'Updated {name}')