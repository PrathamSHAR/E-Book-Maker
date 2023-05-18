# Generated by Django 4.1.7 on 2023-05-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texteditor_upload', '0006_alter_books_avgrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('price', models.IntegerField()),
                ('genre', models.CharField(max_length=254)),
                ('quant', models.IntegerField()),
                ('totalpayable', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='readrate',
            old_name='fivestar',
            new_name='readrate',
        ),
        migrations.RemoveField(
            model_name='readrate',
            name='fourstar',
        ),
        migrations.RemoveField(
            model_name='readrate',
            name='hitrate',
        ),
        migrations.RemoveField(
            model_name='readrate',
            name='onestar',
        ),
        migrations.RemoveField(
            model_name='readrate',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='readrate',
            name='threestar',
        ),
        migrations.RemoveField(
            model_name='readrate',
            name='twostar',
        ),
        migrations.AddField(
            model_name='books',
            name='readrate',
            field=models.IntegerField(default=0),
        ),
    ]
