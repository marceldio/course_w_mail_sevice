# Generated by Django 4.2.15 on 2024-08-31 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mails", "0008_remove_sending_title_sending_letter_sending_topic_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sending",
            name="frequency",
            field=models.CharField(
                choices=[
                    ("daily", "Раз в день"),
                    ("weekly", "Раз в неделю"),
                    ("monthly", "Раз в месяц"),
                ],
                max_length=15,
                verbose_name="Периодичность",
            ),
        ),
        migrations.AlterField(
            model_name="sending",
            name="status",
            field=models.CharField(
                choices=[
                    ("created", "Создана"),
                    ("launched", "Запущена"),
                    ("completed", "Завершена"),
                ],
                max_length=15,
                verbose_name="Статус",
            ),
        ),
    ]