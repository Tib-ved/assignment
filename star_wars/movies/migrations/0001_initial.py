from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swapi_id', models.IntegerField()),
                ('title', models.CharField(max_length=150)),
                ('is_favourite', models.BooleanField(default=False)),
            ],
        ),
    ]
