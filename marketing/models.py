from django.db import models


class Offer(models.Model):
    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("ACTIVE", "Active"),
        ("RETIRED", "Retired"),
    ]

    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="DRAFT")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Treatment(models.Model):
    CHANNEL_CHOICES = [
        ("EMAIL", "Email"),
        ("WEB", "Web"),
        ("SMS", "SMS"),
        ("PHONE", "Phone"),
        ("DIRECT_MAIL", "Direct Mail"),
    ]

    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="treatments")
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)  # will be edited with rich-text editor later
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.offer.code} - {self.name} ({self.channel})"
