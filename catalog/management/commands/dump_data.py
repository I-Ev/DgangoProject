from django.core import serializers
from django.core.management import BaseCommand

import blog.models
import catalog.models
import mailing.models

from django.db.models import Model
Model.defer = False

class Command(BaseCommand):
    def handle(self, *args, **options):
        models = [
            blog.models.BlogEntry,
            catalog.models.Product,
            catalog.models.Category,
            catalog.models.Version,
            mailing.models.Email,
            mailing.models.MailingSetting,
            mailing.models.SendingTry,
            mailing.models.Client
        ]

        data = serializers.serialize('json', models, indent=2, use_natural_foreign_keys=True, ensure_ascii=False,
                                     use_natural_primary_keys=True)

        with open('data.json', 'w', encoding='utf-16') as f:
            f.write(data)
