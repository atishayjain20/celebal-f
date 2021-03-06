# Generated by Django 3.2.3 on 2021-05-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voter', '0002_auto_20210529_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.ImageField(default='ps.jpg', upload_to='pics')),
                ('name', models.CharField(max_length=40)),
                ('party', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=20)),
                ('ward', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='voter',
            old_name='image',
            new_name='profile',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='address',
        ),
        migrations.AddField(
            model_name='voter',
            name='city',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voter',
            name='ward',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
