Overview
========

pluralize_pl is fully compatible with Django's "pluralize" filter. Works exactly the same as long as you are giving it up to 2 comma-separated arguments. The difference is you can provide it with a third argument, which will be used as a second plural form and applied according to Polish grammar rules:

* If value is **0**, `value|pluralize:"komentarz,komentarzy,komentarze"` displays "0 komentarzy".
* If value is **1**, `value|pluralize:"komentarz,komentarzy,komentarze"` displays "1 komentarz".
* If value is **2**, `value|pluralize:"komentarz,komentarzy,komentarze"` displays "2 komentarze".
* If value is **5**, `value|pluralize:"komentarz,komentarzy,komentarze"` displays "5 komentarzy".

It also can be used with i18n:

(the following examples assume "spam,spams" is translated into Polish in language files as "mielonka,mielonek,mielonki")

* If value is 1 and current language is English, `value|pluralize:_("spam,spams")` displays "1 spam".    
* If value is 4 and current language is English, `value|pluralize:_("spam,spams")` displays "4 spams".
* If value is 5 and current language is English, `value|pluralize:_("spam,spams")` displays "5 spams".

* If value is 1 and current language is Polish, `value|pluralize:_("spam,spams")` displays "1 mielonka".    
* If value is 4 and current language is Polish, `value|pluralize:_("spam,spams")` displays "4 mielonki".
* If value is 5 and current language is Polish, `value|pluralize:_("spam,spams")` displays "5 mielonek".

Installation and usage
======================
* Place the application folder somewhere on the PYTHONPATH
* Add the application to INSTALLED_APPS for your project
* Before you can start using it in your template you need to loud it:

      {% load pluralize_pl %}
