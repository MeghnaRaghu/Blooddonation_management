# Generated by Django 4.2.7 on 2023-11-19 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_patientsdatas_remove_patientsdata_user'),
        ('blood', '0005_alter_bloodrequest_request_by_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='request_by_patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patientsdatas'),
        ),
    ]
