from django.contrib import admin
from .models import *

admin.site.register((Gender,
                    SubCategory,
                    Brands,
                    Product,
                    Seller,
                    Buyer,
                    Wishlist,
                    Checkout,
                    Subscribe,
                    Contact))
