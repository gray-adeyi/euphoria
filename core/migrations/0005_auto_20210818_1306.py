# Generated by Django 3.2.6 on 2021-08-18 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_socialaccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialaccount',
            name='resume',
        ),
        migrations.CreateModel(
            name='SiteSocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_accounts', to='core.siteinfo')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeDataSocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_accounts', to='core.resumedata')),
            ],
        ),
    ]