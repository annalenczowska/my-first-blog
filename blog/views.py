from django.shortcuts import render

# Create r views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})