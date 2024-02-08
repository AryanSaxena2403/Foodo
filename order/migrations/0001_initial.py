# Generated by Django 4.2.3 on 2023-08-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order_pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_img', models.ImageField(upload_to='order_pizza/')),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]