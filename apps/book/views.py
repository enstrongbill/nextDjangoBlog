from django.shortcuts import render
from django.views import View

# Create your views here.
class GetBook(View):
    def get(self, request):
        return render(request, 'book.html', {'message':'测试成功'})