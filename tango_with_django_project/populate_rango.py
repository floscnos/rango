import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
    {'title': 'Official Python Tutorial',
    'url':'http://docs.python.org/3/tutorial/', 'views': 10,},
    {'title':'How to Think like a Computer Scientist',
    'url':'http://www.greenteapress.com/thinkpython/', 'views': 20,},
    {'title':'Learn Python in 10 Minutes',
    'url':'http://www.korokithakis.net/tutorials/python/', 'views': 30,}
    ]

    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views': 40,},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/', 'views': 50,},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/', 'views': 60,}
    ]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/', 'views': 70,},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org', 'views': 70,}
    ]

    cats = {'Python': {'pages': python_pages, 'views': 10, 'likes': 0},
            'Django': {'pages': django_pages, 'views': 20, 'likes': 0},
            'Other Frameworks': {'pages': other_pages, 'views': 30, 'likes': 0},
            'Pascal': {'pages': [], 'views': 30, 'likes': 0},
            'Perl': {'pages': [], 'views': 30, 'likes': 0},
            'PHP': {'pages': [], 'views': 30, 'likes': 0},
            'Prolog': {'pages': [], 'views': 30, 'likes': 0},
            'Postscript': {'pages': [], 'views': 30, 'likes': 0},
            'Programming': {'pages': [], 'views': 30, 'likes': 0},
            }
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

if __name__=='__main__':
    print('Starting Rango population script...')
    populate()
