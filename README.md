These are repro instructions for https://github.com/matthewwithanm/django-imagekit/issues/369.

## S3 prep

First, create a new s3 bucket named `iktest-media`.  We'll need your access
keys available in your environment later, so go ahead and just export them
now:

```shell
$ export AWS_ACCESS_KEY_ID=...
$ export AWS_SECRET_ACCESS_KEY=...
```

Now clone the iktest repo:

```shell
$ git clone https://github.com/mgalgs/iktest.git
$ cd iktest
```

and upload the `IMG_20160609_183718.jpg` file from this repo to your new
bucket:

```shell
$ aws s3 cp IMG_20160609_183718.jpg s3://iktest-media/media/test_images/
```

Your bucket should now look like this:

```shell
aws s3 ls --recursive s3://iktest-media                                                                                  1 ↵ ~/sites/iktest2/iktest master 
2016-08-11 20:03:26      49093 media/test_images/IMG_20160609_183718.jpg
```


## Django prep

Install everything in a fresh virtualenv and bootstrap some data:

```shell
$ virtualenv env
$ . env/bin/activate
$ pip install Django==1.9 django-s3-storage Pillow git+git://github.com/matthewwithanm/django-imagekit.git@develop
$ python manage.py migrate
$ python manage.py testdata
```

## Running the app

You're now ready to run the dev server:

```shell
$ python manage runserver
```

Load [http://localhost:8000](http://localhost:8000) in your web browser.
You'll notice that the first time you load the page it will complain with:

```
Internal Server Error: /
Traceback (most recent call last):
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/core/handlers/base.py", line 149, in get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/core/handlers/base.py", line 147, in get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/mgalgs/sites/iktest2/iktest/testapp/views.py", line 10, in index_view
    'widgets': TestWidget.objects.all(),
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/shortcuts.py", line 67, in render
    template_name, context, request=request, using=using)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/template/loader.py", line 97, in render_to_string
    return template.render(context, request)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/template/backends/django.py", line 95, in render
    return self.template.render(context)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/template/base.py", line 206, in render
    return self._render(context)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/template/base.py", line 197, in _render
    return self.nodelist.render(context)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/template/base.py", line 988, in render
    bit = node.render_annotated(context)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/template/base.py", line 955, in render_annotated
    return self.render(context)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/template/defaulttags.py", line 220, in render
    nodelist.append(node.render_annotated(context))
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/template/base.py", line 955, in render_annotated
    return self.render(context)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/template/base.py", line 1039, in render
    output = self.filter_expression.resolve(context)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/template/base.py", line 705, in resolve
    obj = self.var.resolve(context)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/template/base.py", line 846, in resolve
    value = self._resolve_lookup(context)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/template/base.py", line 887, in _resolve_lookup
    current = getattr(current, bit)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/imagekit/cachefiles/__init__.py", line 84, in url
    return self._storage_attr('url')
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/imagekit/cachefiles/__init__.py", line 74, in _storage_attr
    existence_required.send(sender=self, file=self)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/dispatch/dispatcher.py", line 192, in send
    response = receiver(signal=self, sender=sender, **named)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/imagekit/registry.py", line 53, in existence_required_receiver
    self._receive(file, 'on_existence_required')
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/imagekit/registry.py", line 61, in _receive
    call_strategy_method(file, callback)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/imagekit/utils.py", line 148, in call_strategy_method
    fn(file)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/imagekit/cachefiles/strategies.py", line 15, in on_existence_required
    file.generate()
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/imagekit/cachefiles/__init__.py", line 93, in generate
    self.cachefile_backend.generate(self, force)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/imagekit/cachefiles/backends.py", line 108, in generate
    self.generate_now(file, force=force)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/imagekit/cachefiles/backends.py", line 95, in generate_now
    file._generate()
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/imagekit/cachefiles/__init__.py", line 97, in _generate
    content = generate(self.generator)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/imagekit/utils.py", line 134, in generate
    content = generator.generate()
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/imagekit/specs/__init__.py", line 153, in generate
    self.source.open()
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/db/models/fields/files.py", line 81, in open
    self.file.open(mode)
  File "/home/mgalgs/sites/iktest2/env/lib/python2.7/site-packages/django/core/files/base.py", line 141, in open
    raise ValueError("The file cannot be reopened.")
ValueError: The file cannot be reopened.
```

If you *reload* your page it will load(!).  However, the thumbnails that
got generated won't actually be valid.  Check the urls from your web
browser to:

```shell
$ aws s3 ls --recursive s3://iktest-media
```
