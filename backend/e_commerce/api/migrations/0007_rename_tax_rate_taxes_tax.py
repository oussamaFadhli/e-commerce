# Generated by Django 4.1.7 on 2023-04-07 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_taxes_created_at_remove_taxes_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxes',
            old_name='tax_rate',
            new_name='tax',
        ),
    ]