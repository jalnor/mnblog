from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static

# Create your views here.
def index(request):
    title = "Everything Important"
    images = [
        static('images/bv-1.webp'),
        static('images/bv-2.webp'),
        static('images/bv-3.webp'),
        static('images/bv-4.webp'),
        static('images/bv-5.webp'),
        static('images/bv-6.webp'),
        static('images/bv-7.webp'),
        static('images/bv-8.webp'),
        static('images/bv-9.webp'),
        static('images/bv-10.webp'),
        static('images/bv-11.webp'),
        static('images/bv-12.webp'),
        static('images/bv-13.webp'),
        static('images/bv-14.webp'),
        static('images/bv-15.webp'),
    ]
    return render(
        request=request,
        template_name='everything_important/templates/index.html',
        context={
            'title': title,
            'images': images,
        },
    )


