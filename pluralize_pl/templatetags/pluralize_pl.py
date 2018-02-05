from django import template

register = template.Library()

def pluralize_pl(value, arg=u's'):
    """
    pluralize_pl is fully compatible with Django's "pluralize" filter. Works
    exactly the same as long as you are giving it up to 2 comma-separated arguments.
    The difference is you can provide it with a third argument, which will
    be used as a second plural form and applied according to Polish grammar
    rules:
    
    * If value is 0, {{ value|pluralize:"komentarz,komentarzy,komentarze" }} displays "0 komentarzy".
    * If value is 1, {{ value|pluralize:"komentarz,komentarzy,komentarze" }} displays "1 komentarz".
    * If value is 2, {{ value|pluralize:"komentarz,komentarzy,komentarze" }} displays "2 komentarze".
    * If value is 5, {{ value|pluralize:"komentarz,komentarzy,komentarze" }} displays "5 komentarzy".           
    
    It also can be used with i18n:

	(the following examples assume "spam,spams" is translated into
	Polish in language files as "mielonka,mielonek,mielonki")


    * If value is 1 and current language is English, {{ value|pluralize:_("dog,dogs") }} displays "1 spam".    
    * If value is 4 and current language is English, {{ value|pluralize:_("dog,dogs") }} displays "4 spams".
    * If value is 5 and current language is English, {{ value|pluralize:_("dog,dogs") }} displays "5 spams".

    * If value is 1 and current language is Polish, {{ value|pluralize:_("dog,dogs") }} displays "1 mielonka".    
    * If value is 4 and current language is Polish, {{ value|pluralize:_("dog,dogs") }} displays "4 mielonki".
    * If value is 5 and current language is Polish, {{ value|pluralize:_("dog,dogs") }} displays "5 mielonek".        

    """
    if not u',' in arg:
        arg = u',' + arg
    bits = arg.split(u',')
    if len(bits) > 3:
        return u''
    elif len(bits) == 2:  
        bits.append(bits[1]) # If there is no second plural form given use the same for both.

    singular_suffix, plural_suffix, plural_suffix2 = bits[:3]

    try:
        n = int(value)
    except ValueError: # Invalid string that's not a number. Assume 1.
        n = 1
    except TypeError: # Value isn't a string or a number; maybe it's a list?
        try:
            n = len(value)
        except TypeError: # len() of unsized object. Assume 1.
            n = 1
            
    if n == 1 or n == -1:
        return singular_suffix
    elif str(n)[-1:] in ['2','3','4'] and str(n)[-2:-1] != '1':
        return plural_suffix2
    else:
        return plural_suffix
pluralize_pl.is_safe = False

register.filter(pluralize_pl)
