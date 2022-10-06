# Generated by Django 4.1.1 on 2022-10-05 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0005_settings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoiceApp.invoice'),
        ),
    ]