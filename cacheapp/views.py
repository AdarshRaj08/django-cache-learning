from django.shortcuts import render
from django.views.decorators.cache import cache_page

# cache is an information technology for the temporary storage of web documents, such as web pages,images and other types of web multipedia
# cache is one of those methods which a website implements to become faster.it saves cpu processing time.

# django comes with a robust cache system that lets you save dynamic pages so they don't have to be calculated for each reqeust.
# you can cache specific views

# options of caching 
    # 1. Database Caching
    # 2. File System caching
    # 3. Local memory caching

# how to implement caching
# 1. The per-site cache
# 2. The per-view cache
# 3. Template fragment caching


# ################# per-site cache ########################

# first add in middleware in settings.py

# steps (in database)
# 1. go in settings.py - do correction in middleware
# 2. caches in setting.py (backend and the location)
# 3. run the command python manage.py createcachetable

# steps (in local file system)
# 1. go in settings.py - do correction in middleware (same as database)
# 2. first create the directory in the main where manage.py or wherever then copy the path and give me locaiton 
# 3. caches in setting.py (backend and the location of the directory)

# MIDDLEWARE SETTINGS
# Full Website Caching: Requires both UpdateCacheMiddleware and FetchFromCacheMiddleware.
# View Caching: Does not require these middlewares; use the cache_page decorator.
# Template Fragment Caching: Does not require these middlewares; use the {% cache %} template tag.


# NOTE - > when you give me a time that for this time interval cache will active then after that expire of time period 
#           the current state will convert into cache for that time interval loop will continute see in the view cache you will understand more clearly


# Create your views here.
def home(request):
    return render(request,'cacheapp/course.html')



# ############################ per-view cache #########################################################

# django.views.decorators.cache defines a cache_page decorator that will automatically cache the view's response.
# if multiple URLs point at the same view, each URL will be cached separately.


# T=0s: First request to profile. Response is generated and cached for 60 seconds.
# T=30s: Second request to profile. Cached response is served.
# T=60s: Cache expires.
# T=61s: Third request to profile. Cache is expired, so the view is processed again, and a new response is cached for the next 60 seconds.


# @cache_page(60)
# def profile(request):
#     return render(request,'cacheapp/profile.html')

# ########### url-caching ##################

# let's say multiple url on one view function then we have to suppose do caching to a particular url 
# steps
#   1. remove caching from the views 
#   2. go to url and perform there caching
#   3. whre have to store choose from 3 methods and the procedure will same for all types of caching

def profile(request):
    return render(request,'cacheapp/profile.html')



# ############################ template-fragment cache #################################################

# steps
#   1. {% load cache %} add in your template
#   2. {% cache 45 course %}              # jis portion pe cache krna waha laga do yaha course cache ka name hai 45 - seconds hai 
#       <h1>LoveMeLikeYouDo❤️</h1>
#       <h1>LoveMeLikeYouDo❤️</h1>
#      {% endcache course %}
#   2. whre have to store choose from 3 methods and the procedure will same for all types of caching