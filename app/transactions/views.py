# from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm

def home(request):

   # return HttpResponse(
   # """
   # <h1>🏦 Bank Screening Platform</h1>
   # <h3>Welcome, Compliance Officer!</h3>
   # <p>Django is running successfully.</p>
   # """
    transaction = Transaction.objects.all()
    context = {
        "officer_name" : "Thejaswini",
        "transactions" : transaction,

    }

    return render(request, "transactions\home.html", context)
def add_transaction(request):

    if request.method == "POST":

        form = TransactionForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = TransactionForm()

    return render(
        request,
        "transactions/add_transaction.html",
        {"form": form},
    )
def edit_transaction(request, id):

    transaction = get_object_or_404(Transaction, id=id)

    if request.method == "POST":

        form = TransactionForm(request.POST, instance=transaction)

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = TransactionForm(instance=transaction)

    return render(
        request,
        "transactions/add_transaction.html",
        {"form": form},
    )
def delete_transaction(request, id):

    transaction = get_object_or_404(Transaction, id=id)

    transaction.delete()

    return redirect("home")

