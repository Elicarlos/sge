# Generated by Django 5.1.4 on 2024-12-30 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
        ('categories', '0002_rename_brand_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
                ('serie_number', models.CharField(blank=True, max_length=200, null=True)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='brands.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='categories.category')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
