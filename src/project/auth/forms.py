from django import forms

from django.contrib.auth import authenticate


class AccessForm(forms.Form):
    access_key = forms.CharField(widget=forms.TextInput(attrs={'autofocus': ''}))

    error_messages = {
        'invalid_access_key': "Please enter a correct access key.",
        'inactive': "This access key is inactive."
    }

    def clean(self):
        access_key = self.cleaned_data.get('access_key')

        if access_key:
            self.user_cache = authenticate(self.request, access_key=access_key)

            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_access_key'],
                    code='invalid_access_key'
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def __init__(self, request=None, *args, **kwargs):
        """
        Copied from ``django.contrib.auth.forms.AuthenticationForm``.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def confirm_login_allowed(self, user):
        """
        Copied from ``django.contrib.auth.forms.AuthenticationForm``.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive'
            )

    def get_user_id(self):
        """
        Copied from ``django.contrib.auth.forms.AuthenticationForm``.
        """
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        """
        Copied from ``django.contrib.auth.forms.AuthenticationForm``.
        """
        return self.user_cache
