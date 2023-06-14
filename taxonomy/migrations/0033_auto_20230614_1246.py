# Generated by Django 3.2.18 on 2023-06-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0032_auto_20230508_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='B2CJobAllowList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=256, verbose_name='External ID')),
            ],
            options={
                'verbose_name': 'B2C Job Allow List entry',
                'verbose_name_plural': 'B2C Job Allow List entries',
                'ordering': ('external_id',),
            },
        ),
        migrations.AlterField(
            model_name='courserunxblockskillstracker',
            name='course_run_key',
            field=models.CharField(help_text='Course run key of the course under which all xblocks were tagged.', max_length=255, unique=True),
        ),
    ]
