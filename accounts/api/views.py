from rest_framework.decorators import api_view, permission_classes
from .serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(http_method_names=['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(
            data=request.data
        )
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration Successful!'
            data['username'] = account.username
            data['email'] = account.email

            # token = Token.objects.get(user=account).key
            # data['token'] = token

            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response(
                data=data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_404_NOT_FOUND
            )
    else:
        serializer = RegistrationSerializer()
        return Response(
            data=serializer.error_messages,
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(http_method_names=['POST'])
@permission_classes(permission_classes=[IsAuthenticated])
def logout_view(request):
    try:
        request.user.auth_token.delete()
        return Response(
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {"error": "An error occured while logging out."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
