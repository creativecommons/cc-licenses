# Generated by Django 2.2.13 on 2020-11-11 17:56

# Third-party
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("licenses", "0010_auto_20201105_1404"),
    ]

    operations = [
        migrations.AlterField(
            model_name="legalcode",
            name="deed_url",
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name="legalcode",
            name="language_code",
            field=models.CharField(
                help_text="E.g. 'en', 'en-ca', 'sr-Latn', or 'x-i18n'."
                " Case-sensitive? This is the language code used by CC, which"
                " might be a little different from the Django language code.",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="legalcode",
            name="license_url",
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name="legalcode",
            name="plain_text_url",
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name="translationbranch",
            name="language_code",
            field=models.CharField(
                help_text="E.g. 'en', 'en-ca', 'sr-Latn', or 'x-i18n'."
                " Case-sensitive? This is a CC language code, which might"
                " differ from Django.",
                max_length=8,
            ),
        ),
    ]
