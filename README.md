# django_testpr2
# based on https://pocoz.gitbooks.io/django-v-primerah/content/

***
**CHANGING SYS**
***
...gitrep\django_testpr2\venv\Lib\site-packages\haystack\backends\solr_backend.py 
_adding [0]_
app_label, model_name = raw_result[DJANGO_CT][0].split(".")
result = result_class(app_label, model_name, raw_result[DJANGO_ID][0], raw_result['score'], **additional_fields)

***
**FOLLOW THIS STEPS:**
***
django-admin startproject mysite
cd mysite
python ./manage.py migrate
python ./manage.py runserver
python ./manage.py startapp blog
models.py -> class Post (базовая модель для записей блога)
settings.py -> добавить blog в INSTALLED_APPS
python ./manage.py makemigrations blog
python ./manage.py migrate
python ./manage.py createsuperuser
http://127.0.0.1:8000/admin/
admin.py -> добавить from .models import Post -> class PostAdmin -> admin.site.register(Post, PostAdmin)
views.py -> def post_list
create urls.py in blog app -> add re_path
edit urls.py in mysite
create templates -> base.html, list.html, detail.html
add pagination -> views.py, pagination.html
email -> forms.py -> class EmailPostForm -> views.py -> def post_share -> urlpatterns -> share.html
set gmail account as mail-server:
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
Comments -> models.py (class Comment) -> makemigrations + migrate -> admin.py (class CommentAdmin)
-> forms.py (class CommentForm) -> views.py (comments) -> detail.html (comments)
Tags -> add taggit to  settings.py (INSTALLED_APPS) -> models.py (TaggableManager()) -> makemigrations+migrate
-> views.py (tag) -> urls.py (re_path tag) -> list.html (class="tags")
Similar posts -> views.py (similar_posts) -> detail.html (Similar posts)
blog/templatetags/ -> blog_tags.py -> base.html ({% load blog_tags %}) -- count posts, latest posts, most comment etc
Sitemap -> settings.py ('django.contrib.sites', 'django.contrib.sitemaps') -> sitemaps.py -> urlpatterns mysite (sitemap)
RSS feed -> feeds.py -> urls.py (urlpatterns for blog) -> base.html
Search with Solr & Haystack -> install java, download and extract solr to /opt/solr/ 
-> opt/solr/bin/solr start -> opt/solr/bin/solr create -c blog
-> settings.py add haystack to INSTALLED_APPS and HAYSTACK_CONNECTIONS
-> create search_indexes.py in blog app -> post_text.txt -> python manage.py build_solr_schema
-> copy generated text to schema.xml
-> Reload core -> python manage.py rebuild_index 
-> check executing query http://127.0.0.1:8983/solr/#/blog/query
-> forms.py (class SearchForm) -> views.py (SearchQuerySet()) -> search.html
-> open http://127.0.0.1:8000/blog/search/
