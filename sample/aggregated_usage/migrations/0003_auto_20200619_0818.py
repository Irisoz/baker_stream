# Generated by Django 2.2.1 on 2020-06-19 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregated_usage', '0002_auto_20200618_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aggregateddatausage',
            old_name='total_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='aggregatedvoiceusage',
            old_name='total_price',
            new_name='price',
        ),
    ]
