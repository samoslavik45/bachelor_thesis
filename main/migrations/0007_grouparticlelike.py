# Generated by Django 5.0.2 on 2024-03-31 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_group_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupArticleLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_likes', to='main.article')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_articles', to='main.group')),
            ],
            options={
                'unique_together': {('article', 'group')},
            },
        ),
    ]
