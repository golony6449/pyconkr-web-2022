# Generated by Django 4.0.2 on 2022-09-15 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0004_remove_sponsor_creator_remove_sponsor_manager_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='eng_desc',
            field=models.TextField(blank=True, help_text='후원사 영문설명입니다. 이 설명은 홈페이지에 게시됩니다.', null=True),
        ),
    ]
