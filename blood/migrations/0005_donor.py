

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0004_bloodrequest_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('bloodgroup', models.CharField(max_length=3)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
    ]
