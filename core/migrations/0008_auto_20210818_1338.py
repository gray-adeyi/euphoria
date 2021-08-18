# Generated by Django 3.2.6 on 2021-08-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_service_resume'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resumedata',
            options={'verbose_name_plural': 'Resume Data'},
        ),
        migrations.AlterModelOptions(
            name='siteinfo',
            options={'verbose_name_plural': 'Site Info'},
        ),
        migrations.AddField(
            model_name='resumedata',
            name='awards',
            field=models.IntegerField(blank=True, default=24),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experience',
            name='timeframe',
            field=models.CharField(blank=True, help_text='Expected format is `2001 - 2003`', max_length=20),
        ),
    ]