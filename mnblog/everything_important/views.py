from http.client import HTTPException

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.templatetags.static import static

from everything_important.models import Post

TEMPLATE_PATH = 'everything_important/templates/'


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
    posts = Post.published.all()


    return render(
        request=request,
        template_name=TEMPLATE_PATH + 'index.html',
        context={
            'title': title,
            'images': images,
            'posts': posts,
        },
    )

def post_detail(request, id: int):
    try:
        post = get_object_or_404(
            klass=Post,
            id=id,
            status=Post.Status.PUBLISHED,
        )
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(
        request=request,
        template_name=TEMPLATE_PATH + 'post/post_detail.html',
        context={
            'post': post,
        }
    )


