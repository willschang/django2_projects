# Generated by Django 2.0.6 on 2018-07-18 12:09

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180717_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ('created_at',), 'verbose_name': '轮播图', 'verbose_name_plural': '轮播图'},
        ),
        migrations.AlterField(
            model_name='banner',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='desc',
            field=DjangoUeditor.models.UEditorField(default='', help_text='内容描述', verbose_name='内容描述'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(default='', help_text='轮播图', upload_to='banner/%Y/%m', verbose_name='轮播图'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(help_text='标题', max_length=100, verbose_name='标题'),
        ),
    ]
