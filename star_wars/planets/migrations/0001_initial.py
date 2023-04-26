from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swapi_id', models.IntegerField()),
                ('name', models.CharField(max_length=300)),
                ('is_favourite', models.BooleanField(default=False)),
            ],
        ),
    ]
