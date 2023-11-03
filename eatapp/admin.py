from django.contrib import admin
from .models import WebSiteSettings,SocialLink,About,Menu,News,Gallery

class WebSiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('home_title', 'home_desc', 'site_logo','home_page_img','address','phone','email')  # Fields to display in the list view
    # list_filter = ('field1', 'field2')  # Filters available in the right sidebar
    # search_fields = ('field1', 'field2')  # Add a search bar to search by these fields


admin.site.register(WebSiteSettings,WebSiteSettingsAdmin)
# Register your models here.
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('icon','social_link')

admin.site.register(SocialLink,SocialLinkAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display=('title','image','desc')
admin.site.register(About,AboutAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu_name','menu_image','menu_price','menu_desc')
admin.site.register(Menu,MenuAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display=('news_title','news_image','news_desc','created_at')
admin.site.register(News,NewsAdmin)
class GalleryAdmin(admin.ModelAdmin):
    list_display=('image',)
admin.site.register(Gallery,GalleryAdmin)