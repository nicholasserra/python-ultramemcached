#Overview
A drop in replacement for python-memcached to use [ultramemcache](https://github.com/esnme/ultramemcache) as an interface instead of python sockets. Requires ultramemcache. Usage is the same as [python-memcached](http://www.tummy.com/Community/software/python-memcached/) .

#Usage
```python
import ultramemcache
mc = ultramemcache.Client(['127.0.0.1:11211'], debug=0)

mc.set("some_key", "Some value")
value = mc.get("some_key")

mc.set("another_key", 3)
mc.delete("another_key")

mc.set("key", "1")   # note that the key used for incr/decr must be a string.
mc.incr("key")
mc.decr("key")
````

#Usage with Django
To use this package with Django, implement your own subclass of Django's `BaseMemcachedCache` backend like this:

```python
from django.core.cache.backends.memcached import BaseMemcachedCache

class UltraMemcachedCache(BaseMemcachedCache):
    "An implementation of a cache binding using python-ultramemcached"
    def __init__(self, server, params):
        import ultramemcache
        super(MemcachedCache, self).__init__(server, params,
                                             library=ultramemcache,
                                             value_not_found_exception=ValueError)
```
