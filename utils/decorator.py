from django.db import connection
from django.shortcuts import render
from functools import wraps
from django_tenants.utils import schema_context
from rest_framework import status
from rest_framework.response import Response


def anonymous_required(view_func):
    @wraps(view_func)
    def wrapped_view(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'welcome.html')
        else:
            return view_func(self, request, *args, **kwargs)

    return wrapped_view


# def change_tenant(view_func):
#     def wrapper(self, request, *args, **kwargs):
#         print("Before function execution")
#         original_tenant = connection.get_tenant()
#         schema_name = None
#         if request.method == "GET":
#             schema_name = request.GET.get('schema_name', None)
#         elif request.method == "POST":
#             schema_name = request.POST.get('schema_name', None)
#         if schema_name:
#             connection.set_schema(schema_name=schema_name)
#             view_func(self, request, *args, **kwargs)
#         else:
#             return Response({'data': {'schema_name': 'Wrong schema name'}, 'status': status.HTTP_400_BAD_REQUEST})
#         print("After function execution")
#         connection.set_tenant(original_tenant)
#     return wrapper
