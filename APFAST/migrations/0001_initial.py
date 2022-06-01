# Generated by Django 4.0.4 on 2022-06-01 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announceTitle', models.CharField(max_length=100)),
                ('announceDescription', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studFirstName', models.CharField(max_length=50)),
                ('studLastName', models.CharField(max_length=50)),
                ('staffTp', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subName', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APFAST.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studFirstName', models.CharField(max_length=50)),
                ('studLastName', models.CharField(max_length=50)),
                ('tp', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='APFAST.course')),
            ],
        ),
        migrations.CreateModel(
            name='FacePattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studFacePat', models.CharField(max_length=1000, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APFAST.student')),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='APFAST.staff')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APFAST.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APFAST.classes')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APFAST.student')),
            ],
        ),
    ]