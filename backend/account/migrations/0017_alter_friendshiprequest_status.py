# Generated by Django 4.2.2 on 2023-07-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_alter_friendshiprequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendshiprequest',
            name='status',
            field=models.CharField(choices=[('rejected', 'rejected'), ('accepted', 'accepted'), ('send', 'send')], default='send', max_length=20),
        ),
    ]
