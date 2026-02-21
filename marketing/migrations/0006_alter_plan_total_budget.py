# No-op migration (total_budget already set in 0005)

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_plan_total_budget_alter_plan_updated_at'),
    ]

    operations = []
