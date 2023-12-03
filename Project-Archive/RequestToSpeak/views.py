from django.shortcuts import render

# Create your views here.
def RequestToSpeak(request):
    return render(request, 'RequestToSpeak.html', {})