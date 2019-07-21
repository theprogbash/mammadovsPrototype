from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.http import Http404, HttpResponseRedirect
from django.views.generic import View
from django.core.mail import send_mail
from .forms import ContactForm


def index(request):
    context = {
        'category_list': Category.objects.all(),  # navbarda gostermek uchun
        'articles': Article.objects.all(),
    }
    return render(request, 'articles.html', context)


def article(request, article_slug, article_category):
    try:
        context = {
            'article': Article.objects.get(slug=article_slug),
            'category_list': Category.objects.all(),  # navbarda gostermek uchun
            'category': Category.objects.filter(name=article_category),  # url-de category name gostermek uchun
        }
    except Article.DoesNotExist:
        raise Http404("Such article could not be found")
    return render(request, 'article.html', context)


def error_404_view(request, exception):
    data = {'category_list': Category.objects.all(), }
    return render(request, 'error_404.html', data)


def error_500_view(request):
    data = {'category_list': Category.objects.all(), }
    return render(request, 'error_404.html', data)


def list_of_post(request, category_name):
    category_list = Category.objects.all()
    articles = Article.objects.all()
    if category_name:
        category = get_object_or_404(Category, name=category_name)
        articles = Article.objects.filter(category=category)
    context = {'category_list': category_list, 'articles': articles, 'category': category}
    return render(request, 'articles.html', context)


def contact(request):
    category_list = Category.objects.all()  # navbarda gostermek uchun
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = "User Name: {0}\n\nUser Email: {1}\n\nMessage: {2}".format(name, email, form.cleaned_data['message'])
            send_mail('New Message', message, email, ['wearemammadovs@gmail.com'])
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    context = {'category_list': category_list, 'form': form}
    return render(request, 'contact.html', context)


def about(request):
    context = {
        'category_list': Category.objects.all(),  # navbarda gostermek uchun
        'articles': Article.objects.all(),
    }
    return render(request, 'about.html', context)