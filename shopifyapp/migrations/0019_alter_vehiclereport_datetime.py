from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('shopifyapp', '0018_delete_imagemodel_alter_vehiclereport_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='vehiclereport',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

