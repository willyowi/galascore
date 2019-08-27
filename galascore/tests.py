from django.test import TestCase
from .models import Postee,Image,tags,Location,Category#importing models 

# Create your tests here.

class PosteeTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.willy= Postee(first_name = 'willy', last_name ='owi', email ='willyowi@gmail.com')


    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.willy,Postee))  


    # Testing Save Method
     # Testing Save Method
    def test_save_method(self):
        self.willy.save_postee()
        postee = Postee.objects.all()
        self.assertTrue(len(postees) > 0)   

     # Testing delete Method
    

class imageTestClass(TestCase):

    def setUp(self):
        # Creating a new postee and saving it
        self.willy= Postee(first_name = 'willy', last_name ='owi', email ='willyowi@gmail.com')
        self.willy.save_postee()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_image= image(title = 'Test image',post = 'This is a random test Post',postee = self.willyposteelf.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        image.objects.all().delete()

    def test_get_image_today(self):
        today-pics = image.today_pics()
        self.assertTrue(len(today-pics)>0)    
