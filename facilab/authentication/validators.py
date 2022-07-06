"""This module defines some validators"""
from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    """This class define a letter validator for the password"""
    def validate(self, password, user=None):
        """This method display a message if the password doesn't contain
         a letter"""
        if not any(char.isalpha() for char in password):
            raise ValidationError('Le mot de passe doit contenir une lettre',
                                  code='password_no_letters')

    def get_help_text(self):
        """This method display a help text for the user"""
        return 'Votre mot de passe doit contenir au moins une lettre en' \
               ' majuscule ou minuscule.'


class ContainsNumberValidator:
    """This class define a number validator for the password"""
    def validate(self, password, user=None):
        """This method display a message if the password doesn't contain
        a number"""
        if not any(char.isdigit() for char in password):
            raise ValidationError('Le mot de passe doit contenir un chiffre',
                                  code='password_no_number')

    def get_help_text(self):
        """This method display a help text for the user"""
        return 'Votre mot de passe doit contenir au moins un chiffre.'
