import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nike.settings')
django.setup()

from nikeapp.models import Category, Product
from django.contrib.auth.models import User

# Create categories
shoes, _ = Category.objects.get_or_create(name='Shoes', slug='shoes', defaults={'description': 'Athletic shoes'})
apparel, _ = Category.objects.get_or_create(name='Apparel', slug='apparel', defaults={'description': 'Clothing'})

# Create products with real images
Product.objects.update_or_create(name='Air Force 1', slug='air-force-1', defaults={'description': 'Classic basketball-inspired sneakers', 'price': 110.00, 'category': shoes, 'stock': 20, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/awjogtdnqxniqqk0wpgf/air-force-1-07-mens-shoes-jBrhbr.png'})
Product.objects.update_or_create(name='Air Jordan 1', slug='air-jordan-1', defaults={'description': 'Iconic high-top basketball shoes', 'price': 170.00, 'category': shoes, 'stock': 15, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/gsuon30rzp8gql4ddpvh/air-jordan-1-retro-high-og-mens-shoes-4V54Jl.png'})
Product.objects.update_or_create(name='Nike Air Max', slug='nike-air-max', defaults={'description': 'Revolutionary air cushioning technology', 'price': 150.00, 'category': shoes, 'stock': 10, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f37fca8-6bce-43e7-ad07-f57ae3c13142/air-max-270-mens-shoes-KkLcGR.png'})
Product.objects.update_or_create(name='Nike React Element', slug='nike-react-element', defaults={'description': 'Responsive foam for all-day comfort', 'price': 130.00, 'category': shoes, 'stock': 12, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/gsuon30rzp8gql4ddpvh/epic-react-2-mens-running-shoes-2S0Cn1.png'})
Product.objects.update_or_create(name='Nike Dunk Low', slug='nike-dunk-low', defaults={'description': 'Retro basketball shoes with modern twist', 'price': 100.00, 'category': shoes, 'stock': 18, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f37fca8-6bce-43e7-ad07-f57ae3c13142/dunk-low-mens-shoes-77MhDk.png'})
Product.objects.update_or_create(name='Nike Tech Fleece Hoodie', slug='nike-tech-fleece-hoodie', defaults={'description': 'Ultra-soft, lightweight hoodie', 'price': 120.00, 'category': apparel, 'stock': 25, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/awjogtdnqxniqqk0wpgf/tech-fleece-windrunner-mens-hoodie-5R8Q8W.png'})
Product.objects.update_or_create(name='Nike Sportswear Club Fleece', slug='nike-sportswear-club-fleece', defaults={'description': 'Comfortable crewneck sweatshirt', 'price': 65.00, 'category': apparel, 'stock': 30, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/gsuon30rzp8gql4ddpvh/sportswear-club-fleece-mens-crew-neck-sweatshirt-2HcpFm.png'})
Product.objects.update_or_create(name='Nike Dri-FIT T-Shirt', slug='nike-dri-fit-t-shirt', defaults={'description': 'Moisture-wicking performance tee', 'price': 25.00, 'category': apparel, 'stock': 40, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f37fca8-6bce-43e7-ad07-f57ae3c13142/dri-fit-mens-short-sleeve-running-top-7Z3p4q.png'})
Product.objects.update_or_create(name='Nike Joggers', slug='nike-joggers', defaults={'description': 'Tapered-leg joggers with elastic cuffs', 'price': 80.00, 'category': apparel, 'stock': 20, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/awjogtdnqxniqqk0wpgf/sportswear-club-fleece-mens-joggers-2N7Z5H.png'})
Product.objects.update_or_create(name='Nike Windrunner Jacket', slug='nike-windrunner-jacket', defaults={'description': 'Lightweight wind-resistant jacket', 'price': 100.00, 'category': apparel, 'stock': 15, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/gsuon30rzp8gql4ddpvh/windrunner-mens-jacket-3J4Q8W.png'})

# Add more Nike products with real images
Product.objects.update_or_create(name='Air Jordan 4', slug='air-jordan-4', defaults={'description': 'Legendary basketball shoes with visible Air unit', 'price': 190.00, 'category': shoes, 'stock': 8, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f37fca8-6bce-43e7-ad07-f57ae3c13142/air-jordan-4-retro-mens-shoes-4V54Jl.png'})
Product.objects.update_or_create(name='Nike Cortez', slug='nike-cortez', defaults={'description': 'Original running shoes with retro style', 'price': 75.00, 'category': shoes, 'stock': 22, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/awjogtdnqxniqqk0wpgf/cortez-mens-shoes-2P8Q8W.png'})
Product.objects.update_or_create(name='Nike Pegasus', slug='nike-pegasus', defaults={'description': 'Everyday training shoes for runners', 'price': 120.00, 'category': shoes, 'stock': 16, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/gsuon30rzp8gql4ddpvh/pegasus-40-mens-road-running-shoes-4V54Jl.png'})
Product.objects.update_or_create(name='Nike Blazer Mid', slug='nike-blazer-mid', defaults={'description': 'Classic mid-top sneakers', 'price': 85.00, 'category': shoes, 'stock': 14, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f37fca8-6bce-43e7-ad07-f57ae3c13142/blazer-mid-77-mens-shoes-2P8Q8W.png'})
Product.objects.update_or_create(name='Nike SB Dunk', slug='nike-sb-dunk', defaults={'description': 'Skateboarding-inspired sneakers', 'price': 95.00, 'category': shoes, 'stock': 12, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/awjogtdnqxniqqk0wpgf/sb-dunk-low-mens-shoes-3J4Q8W.png'})
Product.objects.update_or_create(name='Nike Therma Hoodie', slug='nike-therma-hoodie', defaults={'description': 'Warm, breathable training hoodie', 'price': 110.00, 'category': apparel, 'stock': 18, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/gsuon30rzp8gql4ddpvh/therma-mens-hoodie-5R8Q8W.png'})
Product.objects.update_or_create(name='Nike Pro Shorts', slug='nike-pro-shorts', defaults={'description': 'Compression shorts for workouts', 'price': 35.00, 'category': apparel, 'stock': 35, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f37fca8-6bce-43e7-ad07-f57ae3c13142/pro-mens-3-compression-shorts-2HcpFm.png'})
Product.objects.update_or_create(name='Nike Heritage Hip Pack', slug='nike-heritage-hip-pack', defaults={'description': 'Classic waist bag for essentials', 'price': 25.00, 'category': apparel, 'stock': 28, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/awjogtdnqxniqqk0wpgf/heritage-hip-pack-2N7Z5H.png'})
Product.objects.update_or_create(name='Nike Swoosh Cap', slug='nike-swoosh-cap', defaults={'description': 'Adjustable baseball cap with swoosh logo', 'price': 20.00, 'category': apparel, 'stock': 45, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/gsuon30rzp8gql4ddpvh/swoosh-cap-7Z3p4q.png'})
Product.objects.update_or_create(name='Nike Elite Socks', slug='nike-elite-socks', defaults={'description': 'Performance socks with cushioning', 'price': 15.00, 'category': apparel, 'stock': 50, 'image': 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f37fca8-6bce-43e7-ad07-f57ae3c13142/elite-mens-socks-2HcpFm.png'})

# Create a test user
User.objects.get_or_create(username='testuser', defaults={'password': 'password123'})
