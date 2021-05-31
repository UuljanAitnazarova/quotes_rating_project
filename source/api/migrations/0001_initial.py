# Generated by Django 3.2.3 on 2021-05-28 10:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('author', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('is_moderated', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(1)])),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_rating', to='api.quote')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='users',
            field=models.ManyToManyField(through='api.Rating', to=settings.AUTH_USER_MODEL),
        ),
    ]
