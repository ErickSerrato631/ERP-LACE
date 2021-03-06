from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

from django.contrib.auth import get_user_model
user = get_user_model()


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.signup_confirmation)
        )


account_activation_token = AccountActivationTokenGenerator()
