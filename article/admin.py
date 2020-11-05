from django.contrib import admin

# Register your models here.
from .models import Article #Oluşturmuş olduğumuz Modeli Admin panelinde göstermek için buraya import edip kaydetmemiz gerekiyor.

# admin.site.register(Article) # Oluşturmuş olduğumuz Modeli kayıt ediyoruz.ve artık bizim adnin panelimizde bu Articlemiz gözükecek.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title","author","created_date"] # istediğimiz yerlere link verebiliyoruz.
    search_fields = ["title"] # Admin panelimize arama bölümüde ekleyebiliriz. Title göre arama yapmak istiyoruz.
    list_filter = ["created_date"] # Admin panelimize filtrelme bölümüde ekleyebiliriz. Oluşturma Tarihine göre arama yapmak istiyoruz.

    class Meta :
        model = Article