from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Wallet, Transaction
from .forms import SendMoneyForm
from django.db.models import Q, F
from django.db import transaction


@login_required(login_url='login-url')
def index_view(request):
    wallet = Wallet.objects.get(user=request.user)
    transactions = Transaction.objects.filter(Q(from_wallet__user=request.user) | Q(to_wallet__user=request.user))

    form = SendMoneyForm()
    if request.method == 'POST':
        form = SendMoneyForm(request.POST)
        if form.is_valid():

            with transaction.atomic():
                to_wallet = Wallet.objects.select_for_update().get(user__phone_number=form.cleaned_data['phone_number'])
                from_wallet = Wallet.objects.select_for_update().get(user=request.user)

                if from_wallet != to_wallet:
                    to_wallet.balance = F('balance') + form.cleaned_data['amount']
                    from_wallet.balance = F('balance') - form.cleaned_data['amount']
                    to_wallet.save()

                    from_wallet.save()
                    from_wallet.balance = F('balance') - 10000
                    from_wallet.save()
                    Transaction.objects.create(
                        from_wallet=from_wallet,
                        to_wallet=to_wallet,
                        amount=form.cleaned_data['amount']
                    )

                return redirect(reverse('index-url'))

    return render(request, 'index.html', {'wallet': wallet, 'form': form, 'transactions': transactions})
