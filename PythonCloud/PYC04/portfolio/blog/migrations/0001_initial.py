# Generated by Django 2.0.6 on 2019-02-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='博客标题', max_length=30)),
                ('date', models.DateField()),
                ('image', models.ImageField(default='default.png', upload_to='images/')),
                ('text', models.TextField(default='文章内容')),
            ],
        ),
    ]
