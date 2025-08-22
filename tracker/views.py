from django.shortcuts import render, redirect
from .models import TrackingHistory, CurrentBalance

# Create your views here.


def index(request):
    if request.method == "POST":
        description = request.POST.get('description')
        amount = request.POST.get('amount')

        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
        expense_type = "CREDIT"
        if float(amount) < 0:
            expense_type = "DEBIT"
        tracking_history = TrackingHistory.objects.create(
            amount = amount,
            expense_type = expense_type,
            current_balance = current_balance,
            description = description
        )
        current_balance.current_balance += float(tracking_history.amount)
        current_balance.save()
        print(description, amount)
        return redirect('/')
    return render(request, 'index.html')