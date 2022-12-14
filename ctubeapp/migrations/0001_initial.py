# Generated by Django 4.1.1 on 2022-10-07 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_ID', models.IntegerField(choices=[(1, 'カテゴリー１'), (2, 'カテゴリー２'), (3, 'カテゴリー３'), (4, 'カテゴリー４')], unique=True)),
                ('category_info', models.CharField(max_length=200)),
                ('category_rank', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='user_expansions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, unique=True)),
                ('group_ID', models.IntegerField(choices=[(1, 'JA1'), (2, 'JA2'), (3, 'JA3'), (4, 'JA4')], unique=True)),
                ('is_active', models.BooleanField(default=True, help_text='アクティブならTrue')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_expansions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('video_info', models.CharField(max_length=200)),
                ('video_URL', models.URLField(null=True)),
                ('img_URL', models.URLField(null=True)),
                ('video_rank', models.IntegerField(default=1)),
                ('is_active', models.BooleanField(default=True, help_text='アクティブならTrue')),
                ('category_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ctubeapp.category', to_field='category_ID')),
                ('group_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ctubeapp.user_expansions', to_field='group_ID')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='group_ID',
            field=models.ForeignKey(db_column='group_ID', on_delete=django.db.models.deletion.CASCADE, to='ctubeapp.user_expansions', to_field='group_ID'),
        ),
    ]
