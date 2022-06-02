# Generated by Django 3.2.5 on 2022-04-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slope", "0006_auto_20220411_0851"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="materialmodel",
            name="color",
        ),
        migrations.AlterField(
            model_name="materialmodel",
            name="name",
            field=models.CharField(
                blank=True, default="Fill", max_length=50, null=True
            ),
        ),
    ]
