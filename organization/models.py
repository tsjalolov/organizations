from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


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
    """tashkilot turi  maktab boxcha tibbiyot sport"""
    name = models.CharField("turi", max_length=60)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tashkilot turi"
        verbose_name_plural = "Tashkilot turlari"


class OrganizationNetworkModel(models.Model):
    """tashkilot tarmog'i"""
    name = models.CharField("Tur", max_length=60)
    typeOfOrganization = models.ForeignKey(TypeOfOrganizationModel, verbose_name="type", on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tashkilot tarmog'i"
        verbose_name_plural = "Tashkilot tarmog'lari"


class OrganizationModel(models.Model):
    """Tashkilot"""
    name = models.CharField("Tashkilot", max_length=60)
    typeOfOrganization = models.ForeignKey(TypeOfOrganizationModel, verbose_name="turi", on_delete=models.PROTECT)
    organizationNetworkModel = models.ForeignKey(OrganizationNetworkModel, verbose_name="tarmog'i", on_delete=models.PROTECT)
    districts = models.ForeignKey(DistrictModel, verbose_name="Tuman", on_delete=models.PROTECT)
    mahalla = models.ForeignKey(MahallaModel, verbose_name="Mahalla", on_delete=models.PROTECT)
    address = models.TextField("address", blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tashkilot"
        verbose_name_plural = "Tashkilotlar"

'''    tashkilotlar alohida ochiladi  '''

class MaktabModel(models.Model):
    """Maktab xususiy ma'lumotlari """

    organization = models.ForeignKey(OrganizationModel, verbose_name="tashkilot", on_delete=models.PROTECT)
    quvvati = models.SmallIntegerField()
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.organization.name

    class Meta:
        verbose_name = "Maktab"
        verbose_name_plural = "Maktablar"


class BoxchaModel(models.Model):
    """ Boxcha xususiy ma'lumotlari """

    organization = models.ForeignKey(OrganizationModel, verbose_name="tashkilot", on_delete=models.PROTECT)

    '''--------------------'''

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.organization.name

    class Meta:
        verbose_name = "Boxcha"
        verbose_name_plural = "Boxchalar"


class TibbiyotModel(models.Model):
    """ Tibbiyot xususiy ma'lumotlari """

    organization = models.ForeignKey(OrganizationModel, verbose_name="tashkilot", on_delete=models.PROTECT)

    '''--------------------'''

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.organization.name

    class Meta:
        verbose_name = "Tibbiyot"
        verbose_name_plural = "Tibbiyotlar"


class SportModel(models.Model):
    """ Sport xususiy ma'lumotlari """

    organization = models.ForeignKey(OrganizationModel, verbose_name="tashkilot", on_delete=models.PROTECT)

    '''--------------------'''

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.organization.name

    class Meta:
        verbose_name = "Sport"
        verbose_name_plural = "Sportlar"


class TomModel(models.Model):
    organization = models.ForeignKey(OrganizationModel, verbose_name="tashkilot", on_delete=models.PROTECT)
    mavjudJami = models.FloatField(verbose_name=('Mavjud yuzasi'))
    tamirtalabi = models.FloatField(verbose_name=('Tamirtalab yuzasi'), default=None, editable=False, null=True)
    status = models.SmallIntegerField('status', choices=[(1,'Soz'),(2,'Qisman tamirtalab'),(3,'To`liq tamirtalab')])
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TomMalumotModel(models.Model):
    tom_id = models.ForeignKey(TomModel, verbose_name="Tom", on_delete=models.PROTECT)
    holat = models.IntegerField( verbose_name='Holati', choices=[(1,'Tamirlandi'),(2,'Tamirlab holatga tushdi')])
    yuza = models.FloatField(verbose_name=('yuzasi'))  # bunga etibor berish kerak 'Tamirlandi'      'Tamirlab holatga tushdi' dan o'tib ketmasin
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
