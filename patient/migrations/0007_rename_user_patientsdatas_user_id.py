# Generated by Django 4.2.7 on 2023-11-19 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_delete_patientsdata_patientsdatas_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientsdatas',
            old_name='user',
            new_name='user_id',
        ),
    ]
