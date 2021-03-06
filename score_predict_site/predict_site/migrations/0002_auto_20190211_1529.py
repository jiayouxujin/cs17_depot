# Generated by Django 2.1.5 on 2019-02-11 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='课程名')),
                ('intro', models.TextField(verbose_name='课程简介')),
                ('lesson_hours', models.FloatField(null=True, verbose_name='课时')),
                ('course_id', models.IntegerField(null=True, verbose_name='课程名id')),
            ],
        ),
        migrations.CreateModel(
            name='StuScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_predict', models.FloatField(null=True, verbose_name='预测分数')),
                ('score_actual', models.FloatField(null=True, verbose_name='实际分数')),
                ('stu_no', models.CharField(max_length=100, verbose_name='学号')),
                ('course_id', models.IntegerField(verbose_name='课程名id')),
                ('predict_accuracy_rating', models.FloatField(null=True, verbose_name='预测准确度')),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='Amath',
            field=models.CharField(max_length=100, null=True, verbose_name='高等数学'),
        ),
        migrations.AddField(
            model_name='users',
            name='C',
            field=models.CharField(max_length=100, null=True, verbose_name='C语言'),
        ),
        migrations.AddField(
            model_name='users',
            name='Cpp',
            field=models.CharField(max_length=100, null=True, verbose_name='C++'),
        ),
        migrations.AddField(
            model_name='users',
            name='Lalg',
            field=models.CharField(max_length=100, null=True, verbose_name='线性代数'),
        ),
        migrations.AddField(
            model_name='users',
            name='Uphy',
            field=models.CharField(max_length=100, null=True, verbose_name='大学物理'),
        ),
    ]
