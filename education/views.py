from django.shortcuts import render, render_to_response

# Create your views here.
from django.views import View


class Index(View):
    def get(self, request):
        return render_to_response('hello.html')
