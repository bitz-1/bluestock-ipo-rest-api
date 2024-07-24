from django.db import models

# Create your models here.

class IpoInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_logo_path = models.TextField()
    company_name = models.CharField(max_length=255)
    price_band = models.CharField(max_length=255)
    open = models.CharField(max_length=255)
    close = models.CharField(max_length=255)
    issue_size = models.CharField(max_length=255)
    issue_type = models.CharField(max_length=255)
    listing_date = models.CharField(max_length=255)
    status = models.IntegerField()
    ipo_price = models.CharField(max_length=255)
    listing_price = models.CharField(max_length=255)
    listing_gain = models.CharField(max_length=255)
    listing_date = models.CharField(max_length=255)
    cmp = models.CharField(max_length=255)
    current_return = models.CharField(max_length=255)
    rhp = models.CharField(max_length=255)
    drhp = models.CharField(max_length=255)



