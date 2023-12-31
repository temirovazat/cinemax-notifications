# Generated by Django 4.1.7 on 2023-03-16 04:07

from typing import List

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies: List = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('text', models.TextField(blank=True, verbose_name='text')),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
                'db_table': 'notifications',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('delivery_method', models.CharField(choices=[('email', 'email'), ('sms', 'sms'), ('push', 'push'), ('none', 'none')], default='email', max_length=255, verbose_name='delivery_method')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('was_sent', models.BooleanField(default=False, verbose_name='was_sent')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifications.notification', verbose_name='notification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifications.user', verbose_name='user')),
            ],
            options={
                'verbose_name': 'user notifications',
                'verbose_name_plural': 'user notifications',
                'db_table': 'user_notifications',
            },
        ),
        migrations.AddField(
            model_name='notification',
            name='users',
            field=models.ManyToManyField(related_name='notifications', through='notifications.UserNotification', to='notifications.user'),
        ),
        migrations.AddConstraint(
            model_name='usernotification',
            constraint=models.UniqueConstraint(fields=('user', 'notification'), name='unique_user_notification'),
        ),
    ]
