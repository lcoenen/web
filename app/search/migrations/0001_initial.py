# Generated by Django 2.2.3 on 2019-11-15 05:34

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0062_hackathonevent_show_results'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('source_id', models.PositiveIntegerField()),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=500)),
                ('url', models.CharField(default='', max_length=500)),
                ('source_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('visible_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='search_results_visible', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]