from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.decorator import anonymous_required


class Home(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return render(request, 'welcome.html')


class Login(APIView):
    permission_classes = [AllowAny]

    @anonymous_required
    def get(self, request):
        return render(request, 'login.html')

    @anonymous_required
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return redirect('login')

    def post(self, request):
        logout(request)
        return Response({'message': 'User logged out successfully.'})