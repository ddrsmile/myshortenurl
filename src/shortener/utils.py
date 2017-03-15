import string, random
from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_letters + string.digits + '-_'):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator()
    url_class = instance.__class__
    is_code_existing  = url_class.objects.filter(url=new_code).exists()
    if is_code_existing:
        return create_shortcode(size=size)
    else:
        return new_code
