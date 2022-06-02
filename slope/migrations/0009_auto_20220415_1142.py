# Generated by Django 3.2.4 on 2022-04-15 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slope", "0008_materialmodel_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="materialmodel",
            name="color",
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name="materialmodel",
            name="name",
            field=models.CharField(blank=True, default="Fill", max_length=50),
        ),
        migrations.AlterField(
            model_name="slopemodel",
            name="angle",
            field=models.FloatField(default=45),
        ),
        migrations.AlterField(
            model_name="slopemodel",
            name="length",
            field=models.FloatField(default=1),
        ),
    ]
