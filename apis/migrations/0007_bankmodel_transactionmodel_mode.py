# Generated by Django 4.0.2 on 2022-08-14 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_alter_notificationmodel_paid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankId', models.CharField(default='', max_length=10)),
                ('name', models.CharField(default='', max_length=300)),
                ('currBalance', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='mode',
            field=models.CharField(default='credit', max_length=10),
        ),
    ]
