# Generated by Django 5.0.2 on 2024-03-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('genero', models.CharField(choices=[('Pop', 'pop'), ('Reggaeton', 'reggaeton'), ('Rap', 'rap')], max_length=30)),
                ('origen', models.CharField(max_length=30)),
                ('edad', models.CharField(max_length=30)),
            ],
        ),
    ]
