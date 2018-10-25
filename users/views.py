import csv
from django.shortcuts import render
from .tasks import bulk_create_users_task

def bulk_create_users(request):
    context = {}
    if request.method == 'POST':
        csv_file = request.FILES.get('csv')
        csv_file = csv_file.read().decode('utf-8').splitlines()
        users = csv.DictReader(csv_file, delimiter=',')
        bulk_create_users_task.delay(list(users))
        succes_text = 'A sua solicitação esta sendo processada, você receberá um email assim quer terminarmos'
        context['message'] = succes_text
    return render(request, 'bulk-create-users.html', context)
