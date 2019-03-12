from django.shortcuts import render, redirect

# Create your views here.
from predict_site import models
from predict_site.form import UserForm
from predict_site.models import Users, StuScore
from predict_site.form import UserForm
from predict_site.models import Users, Courses
from py2neo import Graph
graph = Graph('http://localhost:7474', username='neo4j', password='123456')



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
def Classpoint_lisan(request):
    user_logged = Users.objects.get(stu_no=request.session['user_stu_no'])
    return render(request, 'Classpoint_lisan.html',
                  {'user': user_logged, 'portrait': '/static/user_portrait/portrait' + user_logged.stu_no + '.png'})

# 以下两个函数是course_relevance查看关系所需,由course_relevance调用,无需写进urls.py中
def build_nodes(neo_query):
    data = []
    data_kcm1 = {
        "id": str(neo_query["kcm1"]["id"]),
        "name": str(neo_query["kcm1"]["name"]),
        "label": "课程名"
    }
    data.append({"data": data_kcm1})
    data_kcm2 = {
        "id": str(neo_query["kcm2"]["id"]),
        "name": str(neo_query["kcm2"]["name"]),
        "label": "课程名"
    }
    data.append({"data": data_kcm2})
    data_zj1 = {
        "id": str(neo_query["zj1"]["id"]),
        "name": str(neo_query["zj1"]["name"]),
        "label": "章节"
    }
    data.append({"data": data_zj1})
    data_zj2 = {
        "id": str(neo_query["zj2"]["id"]),
        "name": str(neo_query["zj2"]["name"]),
        "label": "章节"
    }
    data.append({"data": data_zj2})
    data_zsd1 = {
        "id": str(neo_query["zsd1"]["id"]),
        "name": str(neo_query["zsd1"]["name"]),
        "label": "知识点"
    }
    data.append({"data": data_zsd1})
    data_zsd2 = {
        "id": str(neo_query["zsd2"]["id"]),
        "name": str(neo_query["zsd2"]["name"]),
        "label": "知识点"
    }
    data.append({"data": data_zsd2})
    return data


def build_edges(neo_query):
    data = []
    data_zc1 = {
        "source": str(neo_query["zj1"]["id"]),
        "target": str(neo_query["kcm1"]["id"]),
        "relationship": "组成"
    }
    data.append({"data": data_zc1})
    data_zc2 = {
        "source": str(neo_query["zsd1"]["id"]),
        "target": str(neo_query["zj1"]["id"]),
        "relationship": "组成"
    }
    data.append({"data": data_zc2})
    data_xg = {
        "source": str(neo_query["zsd1"]["id"]),
        "target": str(neo_query["zsd2"]["id"]),
        "relationship": "相关"
    }
    data.append({"data": data_xg})
    data_zc3 = {
        "source": str(neo_query["zsd2"]["id"]),
        "target": str(neo_query["zj2"]["id"]),
        "relationship": "组成"
    }
    data.append({"data": data_zc3})
    data_zc4 = {
        "source": str(neo_query["zj2"]["id"]),
        "target": str(neo_query["kcm2"]["id"]),
        "relationship": "组成"
    }
    data.append({"data": data_zc4})
    return data


def course_relevance(request):
    user_logged = Users.objects.get(stu_no=request.session['user_stu_no'])
    course_list = Courses.objects.all()
    if request.method == "GET":
        return render(request, 'course_relevance.html',
                      {'user': user_logged, 'portrait': '/static/user_portrait/portrait' + user_logged.stu_no + '.png',
                       'courses_list': course_list, 'not_choose': True})
    if request.method == "POST":
        course1 = request.POST.get('course1')
        course2 = request.POST.get('course2')
        cypher_to_run = 'match p=(kcm1{description:"课程名"})-[:组成]-(zj1{description:"章节"})-[:组成]-(zsd1{description:"知识点"})-[:相关]-(zsd2{description:"知识点"})-[:组成]-(zj2{description:"章节"})-[:组成]-(kcm2{description:"课程名"}) where kcm1.name="'+course1+'" and kcm2.name="'+course2+'" return distinct p, kcm1, kcm2, zj1, zj2, zsd1, zsd2'
        relation_graph = graph.run(cypher_to_run).data()
        nodes = []
        edges = []
        for relation in relation_graph:
            nodes.extend(build_nodes(relation))
            edges.extend(build_edges(relation))
        # print(nodes)
        # print(edges)
        # print(relation_graph)
        return render(request, 'course_relevance.html', {'user': user_logged,
                                                         'portrait': '/static/user_portrait/portrait' + user_logged.stu_no + '.png',
                                                         'courses_list': course_list,
                                                         'nodes': nodes,
                                                         'edges': edges,
                                                         'course1': course1,
                                                         'course2': course2,
                                                         'not_choose': False  # 已选所要对比的课程
                                                         })
