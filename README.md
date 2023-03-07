**The point of this is to link to resources like so:**

```
<link href="/static/css/index.css/">
```

instead of 

```
{% load static %}
<link href="{% static 'css/index.css' %}">


~$ python manage.py collectstatic
```

---

There are 3 url patterns:

```
static/css/<filename>/
static/js/<filename>/
static/images/<filename>/
```

To enable browser caching, CSS and JS files are hashed using [xxHash](https://cyan4973.github.io/xxHash/). Django handles the rest with the `etag` decorator. For images, the Cache-Control header is set to public

Static should be in the same directory as `manage.py`
This is experimental and has many limitations