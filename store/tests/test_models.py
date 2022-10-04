from unicodedata import category
from django.test import TestCase
from store.models import Product,Category
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):
    
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')
    
    def test_category_model_entry(self):
        """
        Test Category model Data insertion/type/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')
        

class TestproductModel(TestCase):
    
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin', password='Testuser@123')
        self.data1 = Product.objects.create(category_id=1,created_by_id=1,title='django begineers',slug='django begineers', price='20.99', image='image')
        
    def test_product_model_entry(self):
        """
        Test product model data insertion/type/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django begineers')