# Generated by Django 3.0.3 on 2020-03-10 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_tracker', '0004_auto_20200301_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='inventory_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='storage_location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='storage_location_type',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='change_orders',
            name='job_number',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='job_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='extra_work_tickets',
            name='job_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incoming_wall_covering',
            name='job_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='inventory_type',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='orders',
            name='job_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='outgoing_wallcovering',
            name='job_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='packages',
            name='job_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='plans',
            name='job_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='subcontractors',
            name='job_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='submittal_items',
            name='job_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='submittals',
            name='job_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='wallcovering',
            name='job_number',
            field=models.CharField(max_length=10),
        ),
    ]
