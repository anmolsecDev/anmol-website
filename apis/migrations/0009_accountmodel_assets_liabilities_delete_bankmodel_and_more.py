# Generated by Django 4.0.2 on 2022-08-15 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_chequemodel_remove_bankmodel_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountModel',
            fields=[
                ('accountId', models.CharField(default='', max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=300)),
                ('currBalance', models.IntegerField(default=0)),
                ('currLoan', models.IntegerField(default=0)),
                ('bankName', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cashBalance', models.IntegerField(default=0)),
                ('ptCash', models.IntegerField(default=0)),
                ('accountReceivable', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Liabilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shareCapitalArchana', models.IntegerField(default=0)),
                ('shareCapitalSangita', models.IntegerField(default=0)),
                ('borrowingLoanBank', models.IntegerField(default=0)),
                ('borrowingArchanaRimal', models.IntegerField(default=0)),
                ('borrowingSangeetaNeupane', models.IntegerField(default=0)),
                ('borrowingOthers', models.IntegerField(default=0)),
                ('socialSecurityTax', models.IntegerField(default=0)),
                ('salaryTax', models.IntegerField(default=0)),
                ('salaryPayable', models.IntegerField(default=0)),
                ('auditFeePayable', models.IntegerField(default=0)),
                ('otherPayable', models.IntegerField(default=0)),
                ('capitalReserveOrDeficit', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='BankModel',
        ),
        migrations.DeleteModel(
            name='ChequeModel',
        ),
        migrations.RemoveField(
            model_name='transactionmodel',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='transactionmodel',
            name='subType',
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='paidFrom',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='paidTo',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='mode',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='type',
            field=models.CharField(default='', max_length=20),
        ),
    ]
