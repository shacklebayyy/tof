# Generated by Django 5.1.6 on 2025-02-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_student_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='current_grade',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='kcpe_marks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
