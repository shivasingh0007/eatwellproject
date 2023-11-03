from django.db import models

class WebSiteSettings(models.Model):
    home_title=models.CharField(max_length=50)
    home_desc=models.TextField()
    site_logo=models.ImageField(upload_to='site/site-logo')
    home_page_img=models.ImageField(upload_to='site/site-page')
    address=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField()

    def __str__(self):
            return self.home_title
    
class SocialLink(models.Model):
    icon=models.ImageField(upload_to='site/social-icon')
    social_link=models.URLField()


class About(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='site/site-about')
    desc=models.TextField()


class Menu(models.Model):
    menu_name=models.CharField(max_length=50)
    menu_image=models.ImageField(upload_to='site/menu-image')
    menu_price=models.IntegerField()
    menu_desc=models.TextField()
    # menu_type=models.CharField(choices=('breakfast':'breakfast','lunch':'lunch','dinner':'dinner''))

class News(models.Model):
    news_title=models.CharField(max_length=50)
    news_image=models.ImageField(upload_to='site/site-news')
    news_desc=models.TextField()
    created_at=models.DateTimeField()

class Gallery(models.Model):
    image=models.ImageField(upload_to='site/site-gallery')
