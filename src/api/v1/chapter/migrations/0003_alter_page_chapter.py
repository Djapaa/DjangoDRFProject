# Generated by Django 4.2.11 on 2024-03-24 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0002_chapter_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='chapter.chapter'),
        ),
    ]
