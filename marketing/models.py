from django.db import models


PLAN_STATUS_CHOICES = [
    ("DRAFT", "Draft"),
    ("PLANNED", "Planned"),
    ("ACTIVE", "Active"),
    ("COMPLETED", "Completed"),
]


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


class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=PLAN_STATUS_CHOICES, default="DRAFT")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)

    def __str__(self):
        return self.name

    @property
    def initiatives_planned_total(self):
        return self.initiatives.aggregate(total=models.Sum("planned_amount"))["total"] or 0

    @property
    def initiatives_actual_total(self):
        return self.initiatives.aggregate(total=models.Sum("actual_amount"))["total"] or 0

    @property
    def initiatives_variance(self):
        return self.initiatives_planned_total - self.initiatives_actual_total


class Initiative(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="initiatives")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=PLAN_STATUS_CHOICES, default="DRAFT")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    planned_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    actual_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.plan.name} - {self.name}"

    @property
    def tactics_planned_total(self):
        return self.tactics.aggregate(total=models.Sum("planned_amount"))["total"] or 0

    @property
    def tactics_actual_total(self):
        return self.tactics.aggregate(total=models.Sum("actual_amount"))["total"] or 0

    @property
    def tactics_variance(self):
        return self.tactics_planned_total - self.tactics_actual_total


class Tactic(models.Model):
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE, related_name="tactics")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=PLAN_STATUS_CHOICES, default="DRAFT")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    planned_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    actual_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.initiative.name} - {self.name}"


class Expense(models.Model):
    tactic = models.ForeignKey(Tactic, on_delete=models.CASCADE, related_name="expenses")
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    spent_on = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tactic.name} - {self.name}"
