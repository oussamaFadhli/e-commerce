# Generated by Django 4.1.7 on 2023-04-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_taxes_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxes',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]