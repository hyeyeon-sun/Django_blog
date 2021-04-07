from django.shortcuts import render
from django.utils import timezone
from .models import Post
'''동일한 디렉토리 내에 있기 때문에 .파일명을 붙이지 않아도 내용을 가져올 수 있다.'''

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})