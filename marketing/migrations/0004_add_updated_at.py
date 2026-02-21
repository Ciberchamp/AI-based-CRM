# No-op migration (previously added updated_at; already included in 0003)

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_plan_initiative_tactic_expense'),
    ]

    operations = []