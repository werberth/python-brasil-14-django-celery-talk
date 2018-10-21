from django.shortcuts import render

def bulk_create_users(request):
    return render(request, 'bulk-create-users.html')
