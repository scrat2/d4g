# Generated by Django 3.1.3 on 2020-11-04 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0002_auto_20201104_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='communes',
            name='numdep',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accueil.departements'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departements',
            name='numreg',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accueil.regions'),
            preserve_default=False,
        ),
    ]
