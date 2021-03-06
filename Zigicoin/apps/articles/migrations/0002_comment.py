# Generated by Django 3.0.5 on 2020-04-26 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='name')),
                ('comment_text', models.CharField(max_length=200, verbose_name='comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Post')),
            ],
        ),
    ]
