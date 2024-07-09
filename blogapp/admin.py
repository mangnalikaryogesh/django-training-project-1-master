from django.contrib import admin
from . models import Category,Tag,Post,Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','url']
    prepopulated_fields = {'url':('name',)}
class TagAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_at','published']
    prepopulated_fields = {'url':('title',)}
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','email','created_at','content','approved']
    list_editable =['approved']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)


