# Generated by Django 4.2.6 on 2023-11-19 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_privacypolicy_termsandconditions'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='privacypolicy',
            options={'verbose_name': 'Privacy Policy', 'verbose_name_plural': 'Privacy Policy'},
        ),
        migrations.AlterModelOptions(
            name='termsandconditions',
            options={'verbose_name': 'Terms And Condition', 'verbose_name_plural': 'Terms And Conditions'},
        ),
    ]
