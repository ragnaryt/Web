
from django.shortcuts import render
from .models import UserInfo
from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect

class Login(View):
    def get(self, request):
        return render(request, 'pride/template/login.html')

    def post(selfself, request):
        id = request.POST.get('userId')
        pw = request.POST.get('userPw')
        msg = False
        infos = UserInfo.objects.all()
        for info in infos:
            if info.userid == id and info.userpw == pw:
                name = info.username
                msg = True
        msg = 'Welcome, ' + name

        context = {
            'msg': msg,
        }

        return render(request, 'pride/template/main.html', context)