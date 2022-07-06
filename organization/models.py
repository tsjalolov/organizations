from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class RegionModel(models.Model):
    """Viloyat"""
    name = models.CharField("Viloyat", max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"


class DistrictModel(models.Model):
    """Tuman"""
    name = models.CharField("Tuman", max_length=60)
    sector = models.SmallIntegerField('Sector', validators=[MaxValueValidator(4), MinValueValidator(1)],)
    regions = models.ForeignKey(RegionModel, verbose_name="Viloyat", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"


class MahallaModel(models.Model):
    """Mahalla"""
    name = models.CharField("Mahalla", max_length=60)
    sector = models.SmallIntegerField('Sector', validators=[MaxValueValidator(4), MinValueValidator(1)],)
    district = models.ForeignKey(DistrictModel, verbose_name="Tuman", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahalla"
        verbose_name_plural = "Mahallalar"


class TypeOfOrganizationModel(models.Model):
    """tashkilot turi  maktab boxcha tibbiyot"""
    name = models.CharField("turi", max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tashkilot turi"
        verbose_name_plural = "Tashkilot turlari"


class OrganizationNetworkModel(models.Model):
    """tashkilot tarmog'i"""
    name = models.CharField("Tur", max_length=60)
    typeOfOrganization = models.ForeignKey(TypeOfOrganizationModel, verbose_name="type", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tashkilot tarmog'i"
        verbose_name_plural = "Tashkilot tarmog'lari"


class OrganizationsModel(models.Model):
    """Tashkilot"""
    name = models.CharField("Tashkilot", max_length=60)
    districts = models.ForeignKey(DistrictModel, verbose_name="Tuman", on_delete=models.PROTECT)
    mahalla = models.ForeignKey(MahallaModel, verbose_name="Mahalla", on_delete=models.PROTECT)
    TypeOfOrganization = models.ForeignKey(TypeOfOrganizationModel, verbose_name="turi", on_delete=models.PROTECT)
    OrganizationNetworkModel = models.ForeignKey(OrganizationNetworkModel, verbose_name="tarmog'i", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tashkilot"
        verbose_name_plural = "Tashkilotlar"
