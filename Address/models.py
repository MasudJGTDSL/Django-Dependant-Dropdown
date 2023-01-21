from django.db import models

class Division(models.Model):
    BanglaDivisionName = models.CharField(
        max_length=200, blank=True, null=True)
    EnglishDivisionName = models.CharField(
        max_length=200, blank=True, null=True)
    lat = models.CharField(
        max_length=200, blank=True, null=True)
    long = models.CharField(
        max_length=200, blank=True, null=True)

    def __str__(self):
        return self.BanglaDivisionName


class District(models.Model):
    BanglaDistrictName = models.CharField(
        max_length=200, blank=True, null=True)
    EnglishDistrictName = models.CharField(
        max_length=200, blank=True, null=True)
    lat = models.CharField(
        max_length=200, blank=True, null=True)
    long = models.CharField(
        max_length=200, blank=True, null=True)
    Division = models.ForeignKey(
        Division, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.BanglaDistrictName


class Upazila(models.Model):
    BanglaUpazilaName = models.CharField(max_length=200, blank=True, null=True)
    EnglishUpazilaName = models.CharField(
        max_length=200, blank=True, null=True)
    District = models.ForeignKey(
        District, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.BanglaUpazilaName


class PostCode(models.Model):
    PostOffice = models.CharField(max_length=200, blank=False, null=False)
    PostCode = models.IntegerField(blank=True, null=True)
    Division = models.ForeignKey(
        Division, blank=True, null=True, on_delete=models.CASCADE)
    District = models.ForeignKey(
        District, blank=True, null=True, on_delete=models.CASCADE)
    Upazila = models.ForeignKey(
        Upazila, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.PostOffice


class PresentAddress(models.Model):
    PersionName=models.CharField(max_length=200, blank=True, null=True)
    Address1 = models.CharField(max_length=200, blank=True, null=True)
    Address2 = models.CharField(max_length=200, blank=True, null=True)
    Division = models.ForeignKey(Division, 
        blank=True, null=True, on_delete=models.CASCADE)
    District = models.ForeignKey(District, 
        blank=True, null=True, on_delete=models.CASCADE)
    Upazila = models.ForeignKey(Upazila, 
        max_length=30, blank=True, null=True, on_delete=models.CASCADE)
    PostOffice = models.CharField(max_length=30, blank=True, null=True)
    PostalCode = models.ForeignKey(PostCode, 
        max_length=30, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.PersionName + ', ' + self.District