# Generated by Django 2.2.10 on 2020-05-06 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ll', '0002_auto_20200506_0230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='p_project_name',
            new_name='project_name',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectname', to='ll.Project'),
        ),
    ]
