# Generated by Django 5.1.6 on 2025-03-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_approval', '0002_alter_feedback_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
