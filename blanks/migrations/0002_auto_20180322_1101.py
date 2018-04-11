# Generated by Django 2.0.1 on 2018-03-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blanks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blank',
            name='document',
        ),
        migrations.RemoveField(
            model_name='blank',
            name='number',
        ),
        migrations.AddField(
            model_name='blank',
            name='base',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='документ-основание'),
        ),
        migrations.AddField(
            model_name='blank',
            name='position',
            field=models.IntegerField(blank=True, null=True, verbose_name='приоритет отображения'),
        ),
        migrations.AlterField(
            model_name='blank',
            name='doc',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='ссылка на doc'),
        ),
        migrations.AlterField(
            model_name='blank',
            name='pdf',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='ссылка на pdf'),
        ),
        migrations.AlterField(
            model_name='blank',
            name='title',
            field=models.CharField(max_length=80, verbose_name='название бланка'),
        ),
    ]
