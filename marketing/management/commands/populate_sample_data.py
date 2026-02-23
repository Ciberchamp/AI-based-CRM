from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta, date
from marketing.models import Plan, Initiative, Tactic, Expense


class Command(BaseCommand):
    help = "Populate sample data for Plans, Initiatives, and Tactics"

    def handle(self, *args, **options):
        # Clear existing data
        Plan.objects.all().delete()
        Initiative.objects.all().delete()
        Tactic.objects.all().delete()
        Expense.objects.all().delete()

        today = date.today()

        # Plan 1: Q1 Marketing Campaign
        plan1 = Plan.objects.create(
            name="Q1 Marketing Campaign",
            description="First quarter marketing initiatives focused on customer acquisition",
            status="ACTIVE",
            start_date=today,
            end_date=today + timedelta(days=90),
            total_budget=50000.00
        )

        # Initiative 1.1: Email Marketing
        init1_1 = Initiative.objects.create(
            plan=plan1,
            name="Email Marketing",
            description="Weekly email campaigns to subscribers",
            status="ACTIVE",
            start_date=today,
            end_date=today + timedelta(days=90),
            planned_amount=15000.00,
            actual_amount=12500.00
        )

        # Tactics for Initiative 1.1
        Tactic.objects.create(
            initiative=init1_1,
            name="Newsletter Setup",
            description="Create and configure email templates",
            status="COMPLETED",
            start_date=today,
            end_date=today + timedelta(days=7),
            planned_amount=2000.00,
            actual_amount=1800.00
        )

        Tactic.objects.create(
            initiative=init1_1,
            name="List Segmentation",
            description="Segment email list by customer type",
            status="ACTIVE",
            start_date=today + timedelta(days=8),
            end_date=today + timedelta(days=30),
            planned_amount=5000.00,
            actual_amount=4200.00
        )

        Tactic.objects.create(
            initiative=init1_1,
            name="Campaign Execution",
            description="Send weekly promotional emails",
            status="ACTIVE",
            start_date=today + timedelta(days=31),
            end_date=today + timedelta(days=90),
            planned_amount=8000.00,
            actual_amount=6500.00
        )

        # Initiative 1.2: Social Media
        init1_2 = Initiative.objects.create(
            plan=plan1,
            name="Social Media Strategy",
            description="Build brand presence on social channels",
            status="PLANNED",
            start_date=today + timedelta(days=15),
            end_date=today + timedelta(days=90),
            planned_amount=20000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init1_2,
            name="Content Calendar",
            description="Plan 90 days of social content",
            status="PLANNED",
            start_date=today + timedelta(days=15),
            end_date=today + timedelta(days=22),
            planned_amount=3000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init1_2,
            name="Ad Campaigns",
            description="Run paid social media campaigns",
            status="PLANNED",
            start_date=today + timedelta(days=23),
            end_date=today + timedelta(days=90),
            planned_amount=17000.00,
            actual_amount=0.00
        )

        # Initiative 1.3: Analytics
        init1_3 = Initiative.objects.create(
            plan=plan1,
            name="Analytics & Reporting",
            description="Track and measure campaign performance",
            status="DRAFT",
            start_date=today + timedelta(days=60),
            end_date=today + timedelta(days=90),
            planned_amount=15000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init1_3,
            name="Dashboard Setup",
            description="Create performance dashboards",
            status="DRAFT",
            start_date=today + timedelta(days=60),
            end_date=today + timedelta(days=75),
            planned_amount=5000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init1_3,
            name="Weekly Reports",
            description="Generate and share performance reports",
            status="DRAFT",
            start_date=today + timedelta(days=76),
            end_date=today + timedelta(days=90),
            planned_amount=10000.00,
            actual_amount=0.00
        )

        # Plan 2: Product Launch
        plan2 = Plan.objects.create(
            name="Product Launch Initiative",
            description="Launch new product to market with integrated marketing strategy",
            status="PLANNED",
            start_date=today + timedelta(days=30),
            end_date=today + timedelta(days=120),
            total_budget=75000.00
        )

        # Initiative 2.1: Pre-Launch
        init2_1 = Initiative.objects.create(
            plan=plan2,
            name="Pre-Launch Activities",
            description="Build awareness before launch date",
            status="PLANNED",
            start_date=today + timedelta(days=30),
            end_date=today + timedelta(days=60),
            planned_amount=25000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init2_1,
            name="Teaser Campaign",
            description="Create buzz with teaser content",
            status="PLANNED",
            start_date=today + timedelta(days=30),
            end_date=today + timedelta(days=45),
            planned_amount=10000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init2_1,
            name="Press Release",
            description="Distribute to media outlets",
            status="PLANNED",
            start_date=today + timedelta(days=50),
            end_date=today + timedelta(days=60),
            planned_amount=15000.00,
            actual_amount=0.00
        )

        # Initiative 2.2: Launch Day
        init2_2 = Initiative.objects.create(
            plan=plan2,
            name="Launch Day Execution",
            description="Execute on launch day",
            status="PLANNED",
            start_date=today + timedelta(days=61),
            end_date=today + timedelta(days=61),
            planned_amount=25000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init2_2,
            name="Live Event",
            description="Host virtual launch event",
            status="PLANNED",
            start_date=today + timedelta(days=61),
            end_date=today + timedelta(days=61),
            planned_amount=15000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init2_2,
            name="Email Blast",
            description="Send launch announcement to all subscribers",
            status="PLANNED",
            start_date=today + timedelta(days=61),
            end_date=today + timedelta(days=61),
            planned_amount=10000.00,
            actual_amount=0.00
        )

        # Initiative 2.3: Post-Launch
        init2_3 = Initiative.objects.create(
            plan=plan2,
            name="Post-Launch Momentum",
            description="Maintain momentum after launch",
            status="PLANNED",
            start_date=today + timedelta(days=62),
            end_date=today + timedelta(days=120),
            planned_amount=25000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init2_3,
            name="Customer Onboarding",
            description="Help new customers get started",
            status="PLANNED",
            start_date=today + timedelta(days=62),
            end_date=today + timedelta(days=90),
            planned_amount=15000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init2_3,
            name="Feedback Collection",
            description="Gather customer feedback and testimonials",
            status="PLANNED",
            start_date=today + timedelta(days=91),
            end_date=today + timedelta(days=120),
            planned_amount=10000.00,
            actual_amount=0.00
        )

        # Plan 3: Customer Retention
        plan3 = Plan.objects.create(
            name="Customer Retention Program",
            description="Focus on retaining existing customers and increasing lifetime value",
            status="ACTIVE",
            start_date=today - timedelta(days=30),
            end_date=today + timedelta(days=180),
            total_budget=45000.00
        )

        # Initiative 3.1: Loyalty Program
        init3_1 = Initiative.objects.create(
            plan=plan3,
            name="Loyalty Program",
            description="Introduce rewards program for repeat customers",
            status="ACTIVE",
            start_date=today - timedelta(days=30),
            end_date=today + timedelta(days=180),
            planned_amount=20000.00,
            actual_amount=8500.00
        )

        Tactic.objects.create(
            initiative=init3_1,
            name="Program Design",
            description="Design loyalty rewards structure",
            status="COMPLETED",
            start_date=today - timedelta(days=30),
            end_date=today - timedelta(days=10),
            planned_amount=5000.00,
            actual_amount=4800.00
        )

        Tactic.objects.create(
            initiative=init3_1,
            name="System Integration",
            description="Integrate with e-commerce platform",
            status="COMPLETED",
            start_date=today - timedelta(days=10),
            end_date=today + timedelta(days=5),
            planned_amount=8000.00,
            actual_amount=3700.00
        )

        Tactic.objects.create(
            initiative=init3_1,
            name="Member Communications",
            description="Send personalized member updates",
            status="ACTIVE",
            start_date=today + timedelta(days=6),
            end_date=today + timedelta(days=180),
            planned_amount=7000.00,
            actual_amount=0.00
        )

        # Initiative 3.2: VIP Support
        init3_2 = Initiative.objects.create(
            plan=plan3,
            name="VIP Customer Support",
            description="Provide premium support to top-tier customers",
            status="ACTIVE",
            start_date=today - timedelta(days=15),
            end_date=today + timedelta(days=180),
            planned_amount=15000.00,
            actual_amount=6200.00
        )

        Tactic.objects.create(
            initiative=init3_2,
            name="Dedicated Account Manager",
            description="Assign dedicated managers to VIP accounts",
            status="ACTIVE",
            start_date=today - timedelta(days=15),
            end_date=today + timedelta(days=180),
            planned_amount=10000.00,
            actual_amount=6200.00
        )

        Tactic.objects.create(
            initiative=init3_2,
            name="Priority Support Queue",
            description="Implement priority support for VIPs",
            status="COMPLETED",
            start_date=today - timedelta(days=15),
            end_date=today - timedelta(days=5),
            planned_amount=5000.00,
            actual_amount=0.00
        )

        # Plan 4: Market Expansion
        plan4 = Plan.objects.create(
            name="Market Expansion 2026",
            description="Expand into three new geographic markets",
            status="DRAFT",
            start_date=today + timedelta(days=45),
            end_date=today + timedelta(days=270),
            total_budget=120000.00
        )

        # Initiative 4.1: Market Research
        init4_1 = Initiative.objects.create(
            plan=plan4,
            name="Market Research",
            description="Research three new target markets",
            status="DRAFT",
            start_date=today + timedelta(days=45),
            end_date=today + timedelta(days=90),
            planned_amount=25000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init4_1,
            name="Competitive Analysis",
            description="Analyze competitors in each market",
            status="DRAFT",
            start_date=today + timedelta(days=45),
            end_date=today + timedelta(days=70),
            planned_amount=12000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init4_1,
            name="Customer Surveys",
            description="Survey potential customers in target markets",
            status="DRAFT",
            start_date=today + timedelta(days=60),
            end_date=today + timedelta(days=90),
            planned_amount=13000.00,
            actual_amount=0.00
        )

        # Initiative 4.2: Go-to-Market Strategy
        init4_2 = Initiative.objects.create(
            plan=plan4,
            name="Go-to-Market Strategy",
            description="Develop GTM strategy for each market",
            status="DRAFT",
            start_date=today + timedelta(days=91),
            end_date=today + timedelta(days=150),
            planned_amount=50000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init4_2,
            name="Localization",
            description="Localize product and marketing materials",
            status="DRAFT",
            start_date=today + timedelta(days=91),
            end_date=today + timedelta(days=120),
            planned_amount=25000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init4_2,
            name="Partnership Development",
            description="Identify and develop local partnerships",
            status="DRAFT",
            start_date=today + timedelta(days=121),
            end_date=today + timedelta(days=150),
            planned_amount=25000.00,
            actual_amount=0.00
        )

        # Initiative 4.3: Launch Execution
        init4_3 = Initiative.objects.create(
            plan=plan4,
            name="Launch Execution",
            description="Execute market entry for each region",
            status="DRAFT",
            start_date=today + timedelta(days=151),
            end_date=today + timedelta(days=270),
            planned_amount=45000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init4_3,
            name="Regional Marketing Campaigns",
            description="Run region-specific marketing campaigns",
            status="DRAFT",
            start_date=today + timedelta(days=151),
            end_date=today + timedelta(days=210),
            planned_amount=30000.00,
            actual_amount=0.00
        )

        Tactic.objects.create(
            initiative=init4_3,
            name="Sales Team Training",
            description="Train sales teams for new markets",
            status="DRAFT",
            start_date=today + timedelta(days=151),
            end_date=today + timedelta(days=170),
            planned_amount=15000.00,
            actual_amount=0.00
        )

        # Plan 5: Operational Efficiency
        plan5 = Plan.objects.create(
            name="Operational Efficiency Initiative",
            description="Streamline operations and reduce costs",
            status="COMPLETED",
            start_date=today - timedelta(days=90),
            end_date=today,
            total_budget=35000.00
        )

        # Initiative 5.1: Process Automation
        init5_1 = Initiative.objects.create(
            plan=plan5,
            name="Process Automation",
            description="Automate repetitive business processes",
            status="COMPLETED",
            start_date=today - timedelta(days=90),
            end_date=today,
            planned_amount=20000.00,
            actual_amount=19200.00
        )

        Tactic.objects.create(
            initiative=init5_1,
            name="Workflow Automation",
            description="Automate marketing workflows",
            status="COMPLETED",
            start_date=today - timedelta(days=90),
            end_date=today - timedelta(days=60),
            planned_amount=10000.00,
            actual_amount=9800.00
        )

        Tactic.objects.create(
            initiative=init5_1,
            name="Data Integration",
            description="Integrate data across systems",
            status="COMPLETED",
            start_date=today - timedelta(days=60),
            end_date=today,
            planned_amount=10000.00,
            actual_amount=9400.00
        )

        # Initiative 5.2: Training & Documentation
        init5_2 = Initiative.objects.create(
            plan=plan5,
            name="Staff Training",
            description="Train staff on new processes",
            status="COMPLETED",
            start_date=today - timedelta(days=60),
            end_date=today,
            planned_amount=15000.00,
            actual_amount=14500.00
        )

        Tactic.objects.create(
            initiative=init5_2,
            name="Training Program",
            description="Conduct training sessions for all teams",
            status="COMPLETED",
            start_date=today - timedelta(days=60),
            end_date=today - timedelta(days=30),
            planned_amount=8000.00,
            actual_amount=7800.00
        )

        Tactic.objects.create(
            initiative=init5_2,
            name="Documentation",
            description="Create comprehensive process documentation",
            status="COMPLETED",
            start_date=today - timedelta(days=30),
            end_date=today,
            planned_amount=7000.00,
            actual_amount=6700.00
        )

        self.stdout.write(
            self.style.SUCCESS("Successfully populated sample data with 5 plans, 14 initiatives, and 27 tactics!")
        )
