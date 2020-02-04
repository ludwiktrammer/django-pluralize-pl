===================
Django Pluralize PL
===================

Simple Django plugin providing `pluralize_pl` template filter that works similarly to Django's built-in `pluralize <https://docs.djangoproject.com/en/dev/ref/templates/builtins/#pluralize>`_  plugin but respects Polish grammar rules.

Quick start
-----------

1. Install the plugin from PyPi::

    pip install django-pluralize-pl

1. Add `pluralize_pl` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'pluralize_pl',
    ]

2. Load `pluralize_pl` in your templates::

    {% load pluralize_pl %}

3. Use the `pluralize_pl` filter when you need it::

    {{ comments | pluralize_pl:"komentarz,komentarzy,komentarze" }}


Overview
--------

``pluralize_pl`` is fully compatible with Django's `pluralize <https://docs.djangoproject.com/en/dev/ref/templates/builtins/#pluralize>`_ filter. It works the same as long as you are giving it up to 2 comma-separated arguments. The difference is, you can provide it with a third argument, which will be used as a second plural form and applied according to Polish grammar rules:

* If value is **0**, ``{{ value|pluralize_pl:"komentarz,komentarzy,komentarze" }}`` displays "komentarzy".
* If value is **1**, ``{{ value|pluralize_pl:"komentarz,komentarzy,komentarze" }}`` displays "komentarz".
* If value is **2**, ``{{ value|pluralize_pl:"komentarz,komentarzy,komentarze" }}`` displays "komentarze".
* If value is **5**, ``{{ value|pluralize_pl:"komentarz,komentarzy,komentarze" }}`` displays "komentarzy".

Note that using the filter only makes sense if you do not utilize Django's translation system, which already has `built-in support for pluralization <https://docs.djangoproject.com/en/2.0/topics/i18n/translation/#pluralization>`_ based on grammar rules of the target language.
