from django.shortcuts import render
from django.core.cache import cache


# LOW-LEVEL CACHE API 

# the low-level cache API in Django provides flexibility and control, allowing you to cache 
# exactly what you need to optimize performance without the limitations or broadness of higher-level 
# caching mechanisms. It’s an essential tool for fine-tuning your application’s performance and ensuring efficient use of resources.


# NOTE -> here you can cache any python object like lists, dictionary, tuple

# When you need to cache data that’s not tied directly to views or templates.
# When caching entire views or templates is too broad and you need more specific caching.
# When you have dynamic data that changes based on user interactions or external factors.
# When you need to cache complex data structures or results of expensive computations.
# When you want to have custom logic for cache invalidation.


# def home(request):
#     mv = cache.get('movie','has_expired')
#     if mv == 'has_expired':
#         cache.set('movie','The Manjhi',10)
#         mv = cache.get('movie')
#     return render(request,'lowLevelCacheApi_App/api.html',{'fm':mv})

# def home(request):
#     mv = cache.get_or_set('fees',4000,30)        # here if fees not in key then it set fees as key and value 4000 for 30 seconds
#     return render(request,'lowLevelCacheApi_App/api.html',{'fm':mv})

# ############################ version ##########################

# we can give same key of different version in the cache
# Versioning helps control, test, and manage cached data more effectively by differentiating between multiple versions of the same cache key

# def home(request):
#     mv = cache.get_or_set('fees',4800,30,version=2)
#     return render(request,'lowLevelCacheApi_App/api.html',{'fm':mv})

# ############################ set_many,get_many ################################
# def home(request):
#     data = {'name':'Adarsh','roll':'005'}
#     cache.set_many(data,30)
#     sv = cache.get_many(data)
#     print(sv)
#     return render(request, 'lowLevelCacheApi_App/api.html',{'fm':sv})


# ########################## delete ##################################3333333

# def home(request):
#     cache.delete('fees',version=2)
#     return render(request,'lowLevelCacheApi_App/api.html')


# ########################## decrement/increment ###################################

# def home(request):
#     mv = cache.get_or_set('count',10,400)
#     print("----------------------")
#     print(mv)
#     mv = cache.incr('count',delta=2)
#     print("Increment value is ", mv)
#     mv = cache.decr('count',delta=2)
#     print("decrement value is ", mv)
#     return render(request,'lowLevelCacheApi_App/api.html')

# ############################# cache.clear() ##############################################

# this is not the correct way of clearing cache because we don't provide autority to clear cache to the user
# it's the responsibility of programmer to clear the cache on time 2 time

# clear cache by command
# steps
#   1. python manage.py shell
#   2. from django.core.cache import cache
#   3. cache.clear()
#   4. quit()

def home(request):
    cache.clear()
    return render(request,'lowLevelCacheApi_App/api.html')
