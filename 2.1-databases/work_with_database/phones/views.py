from django.shortcuts import render, redirect
from django.http import HttpResponse
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)

def catalog(request):
    phones_objects = Phone.objects.all()
    phones = [f'{p.id}, {p.name}, {p.price}, {p.image}, {p.release_date}, {p.lte_exists}, {p.slug}' for p in phones_objects]
    return HttpResponse('<br>'.join(phones))
def create_phone(request):
    add_phone = Phone(id=332,
                     name='name2131asdad',
                     price=3445,
                     image='https://avatars.mds.yandex.net/get-mpic/397397/img_id6752445806321208103.jpeg/orig',
                     release_date='2017-01-20',
                     lte_exists=True,
                      slug='sdkmjhjfl')
    add_phone.save()
    return HttpResponse(f'{add_phone.id}{add_phone.name}')
