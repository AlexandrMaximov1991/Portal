# Generated by Django 4.0.1 on 2022-02-05 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='authorRating',
            field=models.IntegerField(default=0, verbose_name='authorRating'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news_portal.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_portal.author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='PostAuthor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_portal.author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoryType',
            field=models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], max_length=2),
        ),
    ]
