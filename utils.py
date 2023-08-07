

from django.contrib.auth.tokens import PasswordResetTokenGenerator
import json

NULLABLE = {'blank': True, 'null': True}


class TokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return json.dumps([
            user.pk,
            timestamp,
            user.is_active
        ])


account_activation_token = TokenGenerator()

