# Generated by Django 3.0.7 on 2020-10-29 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appShelter', '0005_auto_20201022_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='animal',
            name='age',
        ),
        migrations.AddField(
            model_name='animal',
            name='age',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appShelter.Age', verbose_name='возраст'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='animal',
            name='breed',
        ),
        migrations.AddField(
            model_name='animal',
            name='breed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appShelter.Breed', verbose_name='порода'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='animal',
            name='gender',
        ),
        migrations.AddField(
            model_name='animal',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='animal_gender', to='appShelter.Gender', verbose_name='пол'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='animal',
            name='size',
        ),
        migrations.AddField(
            model_name='animal',
            name='size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appShelter.Size', verbose_name='размер'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='animal',
            name='temperament',
        ),
        migrations.AddField(
            model_name='animal',
            name='temperament',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appShelter.Temperament', verbose_name='темперамент'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='animal',
            name='type',
        ),
        migrations.AddField(
            model_name='animal',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appShelter.Type', verbose_name='вид'),
            preserve_default=False,
        ),
    ]
