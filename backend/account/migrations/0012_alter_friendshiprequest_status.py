# Generated by Django 4.2.2 on 2023-07-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_friendshiprequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendshiprequest',
            name='status',
            field=models.CharField(choices=[('send', 'send'), ('rejected', 'rejected'), ('accepted', 'accepted')], default='send', max_length=20),
        ),
    ]
