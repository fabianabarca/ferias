from django.contrib.gis.db import models
from products.models import Variety
from django.contrib.auth.models import User

# Create your models here.


class Marketplace(models.Model):
    """Model definition for Marketplace (la feria)."""

    SIZE_CHOICES = [
        ("S", "Pequeña"),
        ("M", "Mediana"),
        ("L", "Grande"),
        ("XL", "Muy grande"),
    ]
    BRANCH_CHOICES = [
        ("Atlántico", "Comité Regional Atlántico"),
        ("Brunca", "Comité Regional Brunca"),
        ("Central Central", "Comité Regional Central Central"),
        ("Central Occidental Este", "Comité Regional Central Occidental Este"),
        ("Central Occidental Oeste", "Comité Regional Central Occidental Oeste"),
        ("Central Oriental", "Comité Regional Central Oriental"),
        ("Chorotega", "Comité Regional Chorotega"),
        ("Huetar Norte", "Comité Regional Huetar Norte"),
        ("Pacífico Central", "Comité Regional Pacífico Central"),
    ]
    PARKING_CHOICES = [
        ("lane", "en la calle"),
        ("street_side", "al lado de la calle en espacio dedicado"),
        ("surface", "un un espacio amplio de parqueo"),
    ]
    MARKETPLACE_TYPE_CHOICES = [
        ("feria", "Feria del Agricultor"),
        ("mercado", "Mercado Libre"),
        ("otro", "Otro tipo de feria"),
    ]

    marketplace_url = models.CharField(max_length=50, primary_key=True)
    # General information
    name = models.CharField(max_length=127)
    name_alternate = models.CharField(max_length=127, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    opening_hours = models.CharField(max_length=1023, blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    area = models.PolygonField(blank=True, null=True)
    size = models.CharField(choices=SIZE_CHOICES, max_length=2, blank=True, null=True)
    province = models.CharField(max_length=31)
    canton = models.CharField(max_length=31)
    district = models.CharField(max_length=31)
    postal_code = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=127, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    opening_date = models.DateField(blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(
        choices=BRANCH_CHOICES, max_length=63, blank=True, null=True
    )
    marketplace_type = models.CharField(
        max_length=31, choices=MARKETPLACE_TYPE_CHOICES, blank=True, null=True
    )
    # Infrastructure
    parking = models.CharField(
        choices=PARKING_CHOICES, max_length=31, blank=True, null=True
    )
    bicycle_parking = models.BooleanField(blank=True, null=True)
    fairground = models.BooleanField(blank=True, null=True)
    indoor = models.BooleanField(blank=True, null=True)
    toilets = models.BooleanField(blank=True, null=True)
    handwashing = models.BooleanField(blank=True, null=True)
    drinking_water = models.BooleanField(blank=True, null=True)
    # Services
    food = models.BooleanField(blank=True, null=True)
    drinks = models.BooleanField(blank=True, null=True)
    handicrafts = models.BooleanField(blank=True, null=True)
    butcher = models.BooleanField(blank=True, null=True)
    dairy = models.BooleanField(blank=True, null=True)
    seafood = models.BooleanField(blank=True, null=True)
    spices = models.BooleanField(blank=True, null=True)
    garden_centre = models.BooleanField(blank=True, null=True)
    florist = models.BooleanField(blank=True, null=True)
    # Other
    payment = models.ManyToManyField("Payment", blank=True)
    other_services = models.CharField(max_length=255, blank=True, null=True)
    # Products (varieties)
    varieties = models.ManyToManyField(Variety, blank=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    """Model definition for Photo."""

    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="marketplaces")
    description = models.CharField(
        max_length=255, blank=True, null=True, help_text="Descripción de la foto (alt)."
    )
    alt = models.CharField(max_length=255, blank=True, null=True)
    profile = models.BooleanField(default=False, blank=True, null=True)
    cover = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.url


class Payment(models.Model):
    """Model definition for Payment."""

    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class MarketplaceHistory(models.Model):
    """Model definition for Marketplace (la feria) historical records."""

    SIZE_CHOICES = [
        ("S", "Pequeña"),
        ("M", "Mediana"),
        ("L", "Grande"),
        ("XL", "Muy grande"),
    ]
    BRANCH_CHOICES = [
        ("Atlántico", "Comité Regional Atlántico"),
        ("Brunca", "Comité Regional Brunca"),
        ("Central Central", "Comité Regional Central Central"),
        ("Central Occidental Este", "Comité Regional Central Occidental Este"),
        ("Central Occidental Oeste", "Comité Regional Central Occidental Oeste"),
        ("Central Oriental", "Comité Regional Central Oriental"),
        ("Chorotega", "Comité Regional Chorotega"),
        ("Huetar Norte", "Comité Regional Huetar Norte"),
        ("Pacífico Central", "Comité Regional Pacífico Central"),
    ]
    PARKING_CHOICES = [
        ("lane", "en la calle"),
        ("street_side", "al lado de la calle en espacio dedicado"),
        ("surface", "un un espacio amplio de parqueo"),
    ]

    marketplace_history_id = models.CharField(max_length=127, primary_key=True)
    marketplace = models.ForeignKey("Marketplace", on_delete=models.CASCADE)
    # General information
    name = models.CharField(max_length=127)
    name_alternate = models.CharField(max_length=127, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    opening_hours = models.CharField(max_length=1023, blank=True, null=True)
    opening_date = models.DateField(blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    area = models.PolygonField(blank=True, null=True)
    province = models.CharField(max_length=31)
    canton = models.CharField(max_length=31)
    district = models.CharField(max_length=31)
    postal_code = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    size = models.CharField(choices=SIZE_CHOICES, max_length=2, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=127, blank=True, null=True)
    website = models.URLField(max_length=127, blank=True, null=True)
    instagram = models.URLField(max_length=127, blank=True, null=True)
    facebook = models.URLField(max_length=127, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(
        choices=BRANCH_CHOICES, max_length=63, blank=True, null=True
    )
    # Infrastructure
    parking = models.CharField(
        choices=PARKING_CHOICES, max_length=31, blank=True, null=True
    )
    bicycle_parking = models.BooleanField(blank=True, null=True)
    fairground = models.BooleanField(blank=True, null=True)
    indoor = models.BooleanField(blank=True, null=True)
    toilets = models.BooleanField(blank=True, null=True)
    handwashing = models.BooleanField(blank=True, null=True)
    drinking_water = models.BooleanField(blank=True, null=True)
    # Services
    food = models.BooleanField(blank=True, null=True)
    drinks = models.BooleanField(blank=True, null=True)
    handicrafts = models.BooleanField(blank=True, null=True)
    butcher = models.BooleanField(blank=True, null=True)
    dairy = models.BooleanField(blank=True, null=True)
    seafood = models.BooleanField(blank=True, null=True)
    garden_centre = models.BooleanField(blank=True, null=True)
    florist = models.BooleanField(blank=True, null=True)
    # Other
    payment = models.ManyToManyField("Payment", blank=True)
    other_services = models.CharField(max_length=255, blank=True, null=True)
    # Products (varieties)
    varieties = models.ManyToManyField(Variety, blank=True)
    # History
    saved_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comments_reviewer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.saved_at})"
