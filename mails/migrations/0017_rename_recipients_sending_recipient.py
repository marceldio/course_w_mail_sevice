# Generated by Django 4.2.15 on 2024-09-13 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mails", "0016_event_owner"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sending",
            old_name="recipients",
            new_name="recipient",
        ),
    ]