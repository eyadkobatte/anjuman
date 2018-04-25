# Generated by Django 2.0.4 on 2018-04-25 15:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=50)),
                ('relationship', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Total Amount')),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Paid Amount')),
                ('due_amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Due Amount')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolFeeTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateField(default=datetime.date(2018, 4, 25))),
                ('school_fee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.SchoolFee')),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StudClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('present_standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Standard')),
            ],
        ),
        migrations.CreateModel(
            name='StudentParentRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.ManyToManyField(to='school.Parent')),
                ('stud_id', models.ManyToManyField(to='school.Student')),
            ],
        ),
        migrations.CreateModel(
            name='TransportFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Total Amount')),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Paid Amount')),
                ('due_amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Due Amount')),
            ],
        ),
        migrations.CreateModel(
            name='TransportFeeTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateField(default=datetime.date(2018, 4, 25))),
                ('transport_fee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.TransportFee')),
            ],
        ),
        migrations.AddField(
            model_name='studclass',
            name='stud_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Student'),
        ),
        migrations.AddField(
            model_name='parent',
            name='stud_id',
            field=models.ManyToManyField(to='school.Student'),
        ),
    ]
