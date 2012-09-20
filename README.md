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