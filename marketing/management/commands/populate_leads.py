from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta, date
from marketing.models import Lead, Offer


class Command(BaseCommand):
    help = "Populate sample data for Leads"

    def handle(self, *args, **options):
        # Clear existing lead data
        Lead.objects.all().delete()

        today = date.today()

        # Get existing offers to relate leads
        try:
            spring_offer = Offer.objects.get(code="SPRING-2026")
            loyalty_offer = Offer.objects.get(code="LOYALTY-PLUS")
            vip_offer = Offer.objects.get(code="VIP-EXCLUSIVE")
            summer_offer = Offer.objects.get(code="SUMMER-2026")
        except Offer.DoesNotExist:
            self.stdout.write(
                self.style.ERROR("Offers not found. Please run populate_offers_campaigns first.")
            )
            return

        # Lead 1: Hot lead from web form
        Lead.objects.create(
            first_name="Emily",
            last_name="Rodriguez",
            job_title="Marketing Director",
            company="TechStart Solutions",
            industry="Technology",
            company_size="51-200",
            email="emily.rodriguez@techstart.com",
            phone="+1-555-0101",
            city="San Francisco",
            country="USA",
            status="working",
            source="web",
            rating="hot",
            owner="Sarah Chen",
            offer=spring_offer,
            notes="Interested in spring promotion, requested demo for team"
        )

        # Lead 2: Qualified lead from campaign
        Lead.objects.create(
            first_name="Michael",
            last_name="Thompson",
            job_title="CEO",
            company="Growth Marketing Co",
            industry="Marketing",
            company_size="11-50",
            email="michael.t@growthmarketing.com",
            phone="+1-555-0102",
            city="New York",
            country="USA",
            status="qualified",
            source="campaign",
            rating="hot",
            owner="James Wilson",
            offer=loyalty_offer,
            notes="Signed up for loyalty program, high engagement"
        )

        # Lead 3: New lead from referral
        Lead.objects.create(
            first_name="Amanda",
            last_name="Parker",
            job_title="VP of Sales",
            company="Retail Innovations Inc",
            industry="Retail",
            company_size="201-500",
            email="a.parker@retailinnovations.com",
            phone="+1-555-0103",
            city="Chicago",
            country="USA",
            status="new",
            source="referral",
            rating="warm",
            owner="Sarah Chen",
            offer=vip_offer,
            notes="Referred by existing customer, interested in VIP program"
        )

        # Lead 4: Working lead from partner
        Lead.objects.create(
            first_name="David",
            last_name="Chang",
            job_title="Product Manager",
            company="Innovation Labs",
            industry="Software",
            company_size="11-50",
            email="david.chang@innovationlabs.com",
            phone="+1-555-0104",
            city="Austin",
            country="USA",
            status="working",
            source="partner",
            rating="warm",
            owner="James Wilson",
            offer=spring_offer,
            notes="Partner referral, evaluating spring discount offer"
        )

        # Lead 5: Qualified lead from web
        Lead.objects.create(
            first_name="Jessica",
            last_name="Martinez",
            job_title="Head of Operations",
            company="Global Services LLC",
            industry="Consulting",
            company_size="51-200",
            email="j.martinez@globalservices.com",
            phone="+1-555-0105",
            city="Los Angeles",
            country="USA",
            status="qualified",
            source="web",
            rating="hot",
            owner="Sarah Chen",
            offer=loyalty_offer,
            notes="Completed qualification process, ready to enroll in loyalty program"
        )

        # Lead 6: New lead from campaign
        Lead.objects.create(
            first_name="Robert",
            last_name="Kim",
            job_title="Business Development Manager",
            company="NextGen Enterprises",
            industry="Technology",
            company_size="201-500",
            email="robert.kim@nextgen.com",
            phone="+1-555-0106",
            city="Seattle",
            country="USA",
            status="new",
            source="campaign",
            rating="cold",
            owner="James Wilson",
            offer=summer_offer,
            notes="Responded to summer campaign email"
        )

        # Lead 7: Disqualified lead
        Lead.objects.create(
            first_name="Linda",
            last_name="Brown",
            job_title="Owner",
            company="Small Business Co",
            industry="Retail",
            company_size="1-10",
            email="linda@smallbiz.com",
            phone="+1-555-0107",
            city="Portland",
            country="USA",
            status="disqualified",
            source="web",
            rating="cold",
            owner="Sarah Chen",
            offer=None,
            notes="Budget constraints, not a fit for current offerings"
        )

        # Lead 8: Working lead from web
        Lead.objects.create(
            first_name="Christopher",
            last_name="Lee",
            job_title="Digital Marketing Manager",
            company="E-Commerce Plus",
            industry="E-commerce",
            company_size="51-200",
            email="chris.lee@ecommerceplus.com",
            phone="+1-555-0108",
            city="Miami",
            country="USA",
            status="working",
            source="web",
            rating="warm",
            owner="James Wilson",
            offer=vip_offer,
            notes="Exploring VIP exclusive access options"
        )

        # Lead 9: Qualified lead from referral
        Lead.objects.create(
            first_name="Sophia",
            last_name="Anderson",
            job_title="Chief Marketing Officer",
            company="Brand Builders Inc",
            industry="Marketing",
            company_size="101-200",
            email="sophia.anderson@brandbuilders.com",
            phone="+1-555-0109",
            city="Boston",
            country="USA",
            status="qualified",
            source="referral",
            rating="hot",
            owner="Sarah Chen",
            offer=loyalty_offer,
            notes="High-value referral, interested in comprehensive loyalty solution"
        )

        # Lead 10: New lead from other source
        Lead.objects.create(
            first_name="Daniel",
            last_name="Garcia",
            job_title="Sales Director",
            company="Premium Retail Group",
            industry="Retail",
            company_size="501+",
            email="d.garcia@premiumretail.com",
            phone="+1-555-0110",
            city="Dallas",
            country="USA",
            status="new",
            source="other",
            rating="warm",
            owner="James Wilson",
            offer=vip_offer,
            notes="Trade show contact, interested in VIP offerings for corporate clients"
        )

        # Lead 11: Working lead from campaign
        Lead.objects.create(
            first_name="Michelle",
            last_name="Taylor",
            job_title="Partnership Manager",
            company="Alliance Partners",
            industry="Consulting",
            company_size="11-50",
            email="michelle.taylor@alliancepartners.com",
            phone="+1-555-0111",
            city="Denver",
            country="USA",
            status="working",
            source="campaign",
            rating="warm",
            owner="Sarah Chen",
            offer=spring_offer,
            notes="Engaged with spring email campaign, scheduling follow-up"
        )

        # Lead 12: New lead from partner
        Lead.objects.create(
            first_name="Brian",
            last_name="White",
            job_title="E-commerce Director",
            company="Online Marketplace Inc",
            industry="E-commerce",
            company_size="201-500",
            email="brian.white@onlinemarketplace.com",
            phone="+1-555-0112",
            city="Atlanta",
            country="USA",
            status="new",
            source="partner",
            rating="warm",
            owner="James Wilson",
            offer=summer_offer,
            notes="Partner introduction, interested in summer collection launch"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully populated 12 leads with proper offer relationships!"
            )
        )
