from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from ..exceptions import *


def register_user(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        username = data.get('username')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')  

        try:
            validate_all_fields_required(username, email, password1, password2)
            validate_username(username)
            validate_email(email)
            validate_password(password1, password2)         
            
        except(
            InvalidUsenameException, 
            UsernameAlreadyExistsException,
            InvalidEmailException, 
            EmailAlreadyExistsException,
            InvalidPasswordException, 
            PasswordsDoNotMatchException, 
            AllFieldsRequiredException,
        ) as e:
            
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        
        try:
            
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            
            return JsonResponse({'status': 'success', 'message': 'User successfully registered'})
        
        except Exception as e:
            return register_exception_handler(e)

    else:
        return JsonResponse({'status': 'error', 'message': 'Method not supported'}, status=405)