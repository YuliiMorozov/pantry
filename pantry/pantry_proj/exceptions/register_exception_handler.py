from django.http import JsonResponse
from django.contrib.auth.models import User
import re


class CustomException(Exception):
    def __init__(self, message):
        super().__init__(self._get_message(message))

    def _get_message(self, message):
        return message


class InvalidUsenameException(CustomException):
    pass

class UsernameAlreadyExistsException(CustomException):
    pass

class InvalidEmailException(CustomException):
    pass

class EmailAlreadyExistsException(CustomException):
    pass

class InvalidPasswordException(CustomException):
    pass

class PasswordsDoNotMatchException(CustomException):
    pass

class AllFieldsRequiredException(CustomException):
    pass


def validate_username(username):
    if not re.match(r'^[a-zA-Z]{5,10}$', username):
        raise InvalidUsenameException('Username should be between 5 and 10 characters long and contain only Latin letters')
    
    if User.objects.filter(username=username).exists():
        raise UsernameAlreadyExistsException('Username already exists')
    

def validate_email(email):

    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise InvalidEmailException('Invalid email format')
    
    if User.objects.filter(email=email).exists():
        raise EmailAlreadyExistsException('Email already exists')


def validate_password(password1, password2):

    if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+])[a-zA-Z0-9!@#$%^&*()_+]{8,}$', password1):
        raise InvalidPasswordException('Password should be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character (!@#$%^&*()_+)')
    
    if password1 != password2:
            raise PasswordsDoNotMatchException('Passwords do not match')
    
    
def validate_all_fields_required(username, email, password1, password2):
    if not username or not email or not password1 or not password2:
            raise AllFieldsRequiredException('All fields are required')


def register_exception_handler(exception):    
    # return JsonResponse({'status': 'error', 'message': 'An unexpected error occurred'}, status=500)
    return JsonResponse({'status': 'error', 'message': str(exception)}, status=400)