from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import serializers

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect(reverse('listar_veiculo'))
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})


class LoginAPI(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request': request
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id,
            'nome': user.first_name,
            'email': user.email,
            'token': token.key
        })
