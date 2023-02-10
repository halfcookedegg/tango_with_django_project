from rango.models import Category, Page

def populate():
    python_cat = add_cat('Python',128,64)

    django_cat = add_cat("Django", 64, 32)

    framework_cat = add_cat("Other Frameworks", 32, 16)

   

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c
def get_category_list(current_category=None):
     return {'categories': Category.objects.all(),'current_category': current_category}


def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p
populate()
python_cat = add_cat("Python", 128, 64)
django_cat = add_cat("Django", 64, 32)
other_cat = add_cat("Other Frameworks", 32, 16)

add_page(python_cat, "Official Python Tutorial", "http://docs.python.org/2/tutorial/")
add_page(python_cat, "How to Think like a Computer Scientist", "http://greenteapress.com/thinkpython/", 100)
add_page(python_cat, "Learn Python in 10 Minutes", "http://www.korokithakis.net/tutorials/python/", 200)


print("Population script complete!")

