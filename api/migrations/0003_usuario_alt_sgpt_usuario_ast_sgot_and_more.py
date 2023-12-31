# Generated by Django 4.2.7 on 2023-12-05 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_usuario_altura'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ALT_SGPT',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='AST_SGOT',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='circunferencia_cintura',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='colesterol_HDL',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='colesterol_LDL',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='colesterol_total',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='creatinina_serica',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='gama_GTP',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='hemoglobina',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='hemoglobina_sangue',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='peso',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pressao_arterial_diastolica',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pressao_arterial_sistolica',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='triglicerideos',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='visao_olho_direito',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='visao_olho_esquerdo',
            field=models.IntegerField(default=0.0),
        ),
    ]
