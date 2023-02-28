import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
# from .exceptions import AllFieldsRequiredException, InvalidCredentialsException

def login_user(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        # if not username or not password:
        #     raise AllFieldsRequiredException('All fields are required')

        user = authenticate(request, username=username, password=password)
        # if user is None:
        #     raise InvalidLoginCredentialsException('Invalid login credentials')

        login(request, user)

        # token = generate_jwt_token(user)
        response_data = {
            'status': 'success',
            'message': 'Login successful',
            # 'token': token,
        }
        return JsonResponse(response_data)

    else:
        return JsonResponse({'status': 'error', 'message': 'Method not supported'}, status=405)