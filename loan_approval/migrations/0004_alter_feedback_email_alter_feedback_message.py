# Generated by Django 5.1.6 on 2025-03-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_approval', '0003_alter_feedback_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
