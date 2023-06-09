# Generated by Django 4.2.1 on 2023-05-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0004_projet_delete_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='Img',
        ),
        migrations.RemoveField(
            model_name='service',
            name='created_at',
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='service',
            name='nom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('Design Graphique', 'Design Graphique'), ('Design Web', 'Design Web'), ('SC', 'Scénarisation')], max_length=20),
        ),
    ]
