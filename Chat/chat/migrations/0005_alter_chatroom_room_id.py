# Generated by Django 4.1 on 2023-02-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0004_chatroom_message_chatroom"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatroom",
            name="room_id",
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
