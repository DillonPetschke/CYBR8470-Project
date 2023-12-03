from django.shortcuts import render

# Create your views here.
def JoinNow(request):
    return render(request, 'JoinNow.html', {})