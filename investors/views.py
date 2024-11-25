from django.shortcuts import render

from .models import FinancialStatements


def investor_relations(request):
    financials_queryset = FinancialStatements.objects.all()

    context = {
        "financials_queryset": financials_queryset,
    }

    return render(request, "investors.html", context)
