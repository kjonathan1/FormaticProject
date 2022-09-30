# Generated by Django 3.0.6 on 2021-10-30 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0002_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='client',
            name='clientLogo',
            field=models.ImageField(default='default_logo.jpg', upload_to='company_logos'),
        ),
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('R', 'ZAR'), ('$', 'USD')], default='R', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='uniqueId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]