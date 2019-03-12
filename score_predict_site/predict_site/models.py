from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(u"用户名", max_length=100)
    password = models.CharField(u"密码", max_length=100)
    stu_no = models.CharField(u"学号", max_length=100)
    name = models.CharField(u"姓名", max_length=100)
    gender = models.CharField(u"性别", max_length=100)
    major = models.CharField(u"专业", max_length=100)
    portrait = models.ImageField(upload_to="static/user_portrait")
    mail = models.CharField(u"邮箱", max_length=100)
    status = models.CharField(u"状态/个性签名", max_length=255, null=True)
    Uphy = models.FloatField(u"大学物理", max_length=100, null=True)
    Amath = models.FloatField(u"高等数学", max_length=100, null=True)
    Lalg = models.FloatField(u"线性代数", max_length=100, null=True)
    C = models.FloatField(u"C语言", max_length=100, null=True)
    Cpp = models.FloatField(u"C++", max_length=100, null=True)


class Courses(models.Model):
    name = models.CharField(u"课程名", max_length=100)
    intro = models.TextField(u"课程简介")
    # lesson_hours = models.FloatField(u"课时", null=True)
    course_id = models.IntegerField(u"课程名id", null=True)  # 课程名在图数据库中的id


class StuScore(models.Model):
    score_predict = models.FloatField(u"预测分数", null=True)
    score_actual = models.FloatField(u"实际分数", null=True)
    stu_no = models.CharField(u"学号", max_length=100)
    course_id = models.IntegerField(U"课程名id")
    predict_accuracy_rating = models.FloatField(u"预测准确度", null=True)
