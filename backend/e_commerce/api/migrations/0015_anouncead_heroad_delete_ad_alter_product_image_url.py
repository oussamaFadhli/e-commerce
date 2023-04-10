# Generated by Django 4.1.7 on 2023-04-09 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_ad_slug_anounce_remove_ad_slug_hero_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnounceAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='anounce_ads/')),
                ('url', models.URLField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='hero_ad/')),
                ('url', models.URLField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Ad',
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(upload_to='products_photo/'),
        ),
    ]
