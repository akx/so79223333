from django.db import models


class FinancialStatements(models.Model):
    financials_upload = models.FileField(upload_to="documents/financials/")

    class Meta:
        verbose_name_plural = "Financial Statements"
