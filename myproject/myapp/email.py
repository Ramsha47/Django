# myapp/email.py

from djoser.email import PasswordResetEmail as BasePasswordResetEmail, PasswordChangedConfirmationEmail as BasePasswordChangedConfirmationEmail

class PasswordResetEmail(BasePasswordResetEmail):
    template_name = "email/password_reset.html"

class PasswordChangedConfirmationEmail(BasePasswordChangedConfirmationEmail):
    template_name = "email/password_changed_confirmation.html"