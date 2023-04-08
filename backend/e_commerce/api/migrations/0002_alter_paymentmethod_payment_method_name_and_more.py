# Generated by Django 4.1.7 on 2023-04-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='payment_method_name',
            field=models.CharField(choices=[('CH', 'CASH'), ('MC', 'MASTERCARD'), ('VS', 'VISA'), ('D17', 'D17')], default='CH', max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='shippingmethod',
            name='shipping_method_name',
            field=models.CharField(choices=[('ST', 'STANDARD'), ('PR', 'PREMIUM')], default='ST', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]