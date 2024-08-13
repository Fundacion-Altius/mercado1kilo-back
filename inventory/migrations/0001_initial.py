# Generated by Django 4.2.14 on 2024-08-13 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('lot_number', models.CharField(blank=True, max_length=50, null=True)),
                ('administrative_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.administrativeunit')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('warehouse', 'Warehouse'), ('storefront', 'Storefront')], default='warehouse', max_length=50)),
                ('administrative_unit', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.administrativeunit')),
            ],
        ),
        migrations.CreateModel(
            name='ReceptionBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiving_date', models.DateField()),
                ('total_quantity', models.PositiveIntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('receiptID', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(default='')),
                ('contact_person', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('tax_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StockMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_type', models.CharField(choices=[('in', 'In'), ('out', 'Out'), ('transfer', 'Transfer')], max_length=50)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('reason', models.CharField(max_length=100)),
                ('inventory_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventoryitem')),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.location')),
                ('reception_batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.receptionbatch')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='receptionbatch',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('manufacturer', models.CharField(max_length=255)),
                ('unit_of_measure', models.CharField(max_length=50)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.category')),
            ],
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='reception_batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.receptionbatch'),
        ),
    ]
