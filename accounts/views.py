from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserChangeForm
from .models import User



class AccountSignupAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class AccountProfileAPIView(APIView):
    def post(self, request, username):
        user = get_object_or_404(User, username=username, is_active=True)
        serializer = UserSerializer(data=request.data, instance=user, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        
# def profile(request):
#     if request.method == "POST":
#         pass
#     else:
#         form = UserChangeForm(instance=request.user)
#     context = {"form": form}
#     return render(request, "accounts/profile.html", context)