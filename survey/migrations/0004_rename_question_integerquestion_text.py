# Generated by Django 4.2 on 2023-04-12 14:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0003_rename_question_radioquestion_text"),
    ]

    operations = [
        migrations.RenameField(
            model_name="integerquestion",
            old_name="question",
            new_name="text",
        ),
    ]
