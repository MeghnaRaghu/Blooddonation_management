# Generated by Django 4.2.7 on 2023-11-19 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0005_alter_bloodrequest_request_by_patient'),
        ('patient', '0002_patients_remove_patient_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.AddField(
            model_name='patients',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
