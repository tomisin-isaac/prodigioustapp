# Generated by Django 3.2.2 on 2021-05-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_testimonials_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='banner_text',
            field=models.CharField(default='what we do', max_length=200),
        ),
    ]
