# Generated by Django 3.2.25 on 2024-07-10 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0011_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('mechanic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.mechanic')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost_per_hour', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_spent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.service')),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.servicetype')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='service_types',
            field=models.ManyToManyField(through='vehicle.ServiceEntry', to='vehicle.ServiceType'),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.service')),
            ],
        ),
    ]
