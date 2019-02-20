from django.shortcuts import render, redirect

# Create your views here.
from predict_site import models
from predict_site.form import UserForm
from predict_site.models import Users, StuScore


def home(request):
    user_logged = Users.objects.get(stu_no=request.session['user_stu_no'])
    return render(request, 'home.html',
                  {'user': user_logged, 'portrait': '/static/user_portrait/portrait' + user_logged.stu_no + '.png'})


def score(request):
    user_logged = Users.objects.get(stu_no=request.session['user_stu_no'])
    return render(request, 'score.html',
                  {'user': user_logged, 'portrait': '/static/user_portrait/portrait' + user_logged.stu_no + '.png'})


def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            stu_no = login_form.cleaned_data['stu_no']
            password = login_form.cleaned_data['password']
            try:
                user = Users.objects.get(stu_no=stu_no)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_name'] = user.name
                    request.session['user_stu_no'] = user.stu_no
                    return redirect('/home/')
                else:
                    message = "密码不正确!"
            except:
                message = "用户不存在!"
        return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())

def scorepredict(request):
    user_logged = Users.objects.get(stu_no=request.session['user_stu_no'])
    user_predictscore=StuScore.objects.get(stu_no=request.session['user_stu_no'])
    return render(request, 'scorepredict.html',
                  {'user': user_logged, 'portrait': '/static/user_portrait/portrait' + user_logged.stu_no + '.png','predictscore':user_predictscore})

