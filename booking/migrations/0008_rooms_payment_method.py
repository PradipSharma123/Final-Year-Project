# Generated by Django 4.0.4 on 2022-04-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_rename_harryguesthouse_rooms_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Checkout', 'Cash On Checkout'), ('Khalti', 'Khalti')], default='Cash On Checkout', max_length=20),
        ),
    ]