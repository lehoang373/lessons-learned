# Generated by Django 2.2.10 on 2020-04-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_product_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='cleanup_time',
        ),
        migrations.RemoveField(
            model_name='service',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='service',
            name='location',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_category',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_charge',
        ),
        migrations.RemoveField(
            model_name='service',
            name='setup_time',
        ),
        migrations.RemoveField(
            model_name='service',
            name='updated_date',
        ),
        migrations.AddField(
            model_name='service',
            name='client',
            field=models.CharField(default='DEFAULT VALUE', max_length=30),
        ),
        migrations.AddField(
            model_name='service',
            name='discipline',
            field=models.CharField(default='DEFAULT VALUE', max_length=20),
        ),
        migrations.AddField(
            model_name='service',
            name='division',
            field=models.CharField(default='DEFAULT VALUE', max_length=20),
        ),
        migrations.AddField(
            model_name='service',
            name='link_file',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
        migrations.AddField(
            model_name='service',
            name='market_sector',
            field=models.CharField(default='DEFAULT VALUE', max_length=40),
        ),
        migrations.AddField(
            model_name='service',
            name='project_location',
            field=models.CharField(default='DEFAULT VALUE', max_length=100),
        ),
        migrations.AddField(
            model_name='service',
            name='project_name',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
        migrations.AddField(
            model_name='service',
            name='project_number',
            field=models.CharField(default='DEFAULT VALUE', max_length=10),
        ),
    ]