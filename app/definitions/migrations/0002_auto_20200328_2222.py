# Generated by Django 3.0.4 on 2020-03-28 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('definitions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaireitem',
            name='item_type',
            field=models.CharField(choices=[('group', 'group'), ('display', 'display'), ('string', 'string'), ('text', 'text'), ('boolean', 'boolean'), ('decimal', 'decimal'), ('integer', 'integer'), ('date', 'date'), ('dateTime', 'dateTime')], max_length=12),
        ),
        migrations.AlterField(
            model_name='questionnaireitem',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='definitions.Questionnaire'),
        ),
    ]