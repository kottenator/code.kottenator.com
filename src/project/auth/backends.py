from django.contrib.auth import get_user_model

from project.auth.models import AccessKey


class AccessKeyBackend:
    def authenticate(self, request, access_key=None):
        try:
            access_key_record = AccessKey.objects.get(key=access_key)
            return access_key_record.user
        except AccessKey.DoesNotExist:
            pass

    def get_user(self, user_id):
        User = get_user_model()

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
