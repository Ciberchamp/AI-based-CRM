from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta, date
from marketing.models import Offer, Treatment, Campaign, CampaignResponse


class Command(BaseCommand):
    help = "Populate sample data for Offers, Treatments, Campaigns and Campaign Responses"

    def handle(self, *args, **options):
        # Clear existing data
        Campaign.objects.all().delete()
        CampaignResponse.objects.all().delete()
        Treatment.objects.all().delete()
        Offer.objects.all().delete()

        today = date.today()

        # Offer 1: Spring Discount
        offer1 = Offer.objects.create(
            code="SPRING-2026",
            name="Spring Discount Promotion",
            description="20% off all spring collection items for the season",
            status="ACTIVE",
            start_date=today,
            end_date=today + timedelta(days=90),
            is_active=True
        )

        Treatment.objects.create(
            offer=offer1,
            channel="EMAIL",
            name="Spring Promo Email",
            subject="Spring is Here! Get 20% Off",
            body="Dear Customer, Enjoy 20% discount on all spring items this season!",
            is_active=True
        )

        Treatment.objects.create(
            offer=offer1,
            channel="WEB",
            name="Spring Banner Campaign",
            subject="Homepage Banner",
            body="Seasonal spring promotion banner displayed on homepage and product pages",
            is_active=True
        )

        Treatment.objects.create(
            offer=offer1,
            channel="SMS",
            name="SMS Spring Alert",
            subject="Spring Sale Alert",
            body="Spring sale is live! Get 20% off on all items. Shop now!",
            is_active=True
        )

        # Offer 2: Loyalty Rewards
        offer2 = Offer.objects.create(
            code="LOYALTY-PLUS",
            name="Loyalty Rewards Program",
            description="Earn points on every purchase and redeem for exclusive rewards",
            status="ACTIVE",
            start_date=today - timedelta(days=30),
            end_date=today + timedelta(days=365),
            is_active=True
        )

        Treatment.objects.create(
            offer=offer2,
            channel="EMAIL",
            name="Loyalty Program Enrollment",
            subject="Join Our Rewards Program",
            body="Sign up for our loyalty program and start earning points today!",
            is_active=True
        )

        Treatment.objects.create(
            offer=offer2,
            channel="WEB",
            name="Loyalty Dashboard",
            subject="Member Dashboard",
            body="Access your points balance and exclusive rewards on your member dashboard",
            is_active=True
        )

        Treatment.objects.create(
            offer=offer2,
            channel="PHONE",
            name="Loyalty Support Line",
            subject="Support",
            body="Call our loyalty support team for rewards and points inquiries",
            is_active=True
        )

        # Offer 3: Summer Collection
        offer3 = Offer.objects.create(
            code="SUMMER-2026",
            name="Summer Collection Launch",
            description="Exclusive new summer products with premium styling",
            status="DRAFT",
            start_date=today + timedelta(days=30),
            end_date=today + timedelta(days=120),
            is_active=True
        )

        Treatment.objects.create(
            offer=offer3,
            channel="EMAIL",
            name="Summer Collection Announcement",
            subject="Summer Styles Arriving Soon",
            body="Get ready for summer! New collection launching next month.",
            is_active=True
        )

        Treatment.objects.create(
            offer=offer3,
            channel="DIRECT_MAIL",
            name="Summer Catalog",
            subject="Summer Look Book",
            body="Glossy summer catalog featuring all new styles mailed to selected customers",
            is_active=True
        )

        # Offer 4: VIP Exclusive
        offer4 = Offer.objects.create(
            code="VIP-EXCLUSIVE",
            name="VIP Exclusive Access",
            description="Early access to sales and exclusive VIP-only products",
            status="ACTIVE",
            start_date=today - timedelta(days=15),
            end_date=today + timedelta(days=180),
            is_active=True
        )

        Treatment.objects.create(
            offer=offer4,
            channel="EMAIL",
            name="VIP Early Access Email",
            subject="You're Invited! VIP Early Access",
            body="As a VIP member, get 48-hour early access to all sales",
            is_active=True
        )

        Treatment.objects.create(
            offer=offer4,
            channel="SMS",
            name="VIP Flash Sale Alert",
            subject="VIP Flash Sale",
            body="Exclusive VIP flash sale - 30% off select items for 24 hours only!",
            is_active=True
        )

        Treatment.objects.create(
            offer=offer4,
            channel="WEB",
            name="VIP Portal Access",
            subject="Exclusive VIP Store",
            body="Access the exclusive VIP store with members-only pricing",
            is_active=True
        )

        # Offer 5: Holiday Special
        offer5 = Offer.objects.create(
            code="HOLIDAY-2026",
            name="Holiday Season Special",
            description="Holiday gift bundles and special packages with gift wrapping",
            status="DRAFT",
            start_date=today + timedelta(days=120),
            end_date=today + timedelta(days=180),
            is_active=False
        )

        Treatment.objects.create(
            offer=offer5,
            channel="EMAIL",
            name="Holiday Gift Guide",
            subject="Your Holiday Gift Guide",
            body="Discover perfect gifts for everyone on your list with our curated holiday collection",
            is_active=True
        )

        Treatment.objects.create(
            offer=offer5,
            channel="DIRECT_MAIL",
            name="Holiday Brochure",
            subject="Holiday Gift Collection",
            body="Beautiful holiday brochure with gift ideas and special holiday offers",
            is_active=True
        )

        # Campaign 1: Spring Email Promotion
        campaign1 = Campaign.objects.create(
            name="Spring Email Promotion",
            description="Email campaign promoting spring discounts to active customers",
            status="ACTIVE",
            start_date=today - timedelta(days=10),
            end_date=today + timedelta(days=20),
            target_list="Active Customers List",
            offer=offer1
        )

        CampaignResponse.objects.create(
            campaign=campaign1,
            contact_name="John Smith",
            contact_email="john.smith@example.com",
            status="ACCEPTED"
        )
        CampaignResponse.objects.create(
            campaign=campaign1,
            contact_name="Sarah Johnson",
            contact_email="sarah.j@example.com",
            status="ACCEPTED"
        )
        CampaignResponse.objects.create(
            campaign=campaign1,
            contact_name="Mike Wilson",
            contact_email="mike.w@example.com",
            status="REJECTED"
        )
        CampaignResponse.objects.create(
            campaign=campaign1,
            contact_name="Emma Davis",
            contact_email="emma.d@example.com",
            status="PENDING"
        )
        CampaignResponse.objects.create(
            campaign=campaign1,
            contact_name="Alex Brown",
            contact_email="alex.b@example.com",
            status="ACCEPTED"
        )

        # Campaign 2: Loyalty Program Social Media
        campaign2 = Campaign.objects.create(
            name="Loyalty Program Social Media Campaign",
            description="Multi-channel social media campaign to promote loyalty rewards program",
            status="ACTIVE",
            start_date=today - timedelta(days=5),
            end_date=today + timedelta(days=25),
            target_list="Social Media Followers",
            offer=offer2
        )

        CampaignResponse.objects.create(
            campaign=campaign2,
            contact_name="Lisa Anderson",
            contact_email="lisa.a@example.com",
            status="ACCEPTED"
        )
        CampaignResponse.objects.create(
            campaign=campaign2,
            contact_name="James Taylor",
            contact_email="james.t@example.com",
            status="PENDING"
        )
        CampaignResponse.objects.create(
            campaign=campaign2,
            contact_name="Rachel Green",
            contact_email="rachel.g@example.com",
            status="ACCEPTED"
        )
        CampaignResponse.objects.create(
            campaign=campaign2,
            contact_name="Tom Martinez",
            contact_email="tom.m@example.com",
            status="REJECTED"
        )

        # Campaign 3: Summer Collection Launch
        campaign3 = Campaign.objects.create(
            name="Summer Collection Launch Campaign",
            description="Comprehensive campaign for launching new summer product collection",
            status="PLANNED",
            start_date=today + timedelta(days=30),
            end_date=today + timedelta(days=60),
            target_list="Fashion Enthusiasts",
            offer=offer3
        )

        CampaignResponse.objects.create(
            campaign=campaign3,
            contact_name="Kate Wilson",
            contact_email="kate.w@example.com",
            status="PENDING"
        )
        CampaignResponse.objects.create(
            campaign=campaign3,
            contact_name="David Lee",
            contact_email="david.l@example.com",
            status="PENDING"
        )

        # Campaign 4: VIP Exclusive Access
        campaign4 = Campaign.objects.create(
            name="VIP Exclusive Access Program",
            description="Targeted campaign for VIP customer segment with exclusive benefits",
            status="ACTIVE",
            start_date=today - timedelta(days=3),
            end_date=today + timedelta(days=30),
            target_list="VIP Customer Segment",
            offer=offer4
        )

        CampaignResponse.objects.create(
            campaign=campaign4,
            contact_name="Jennifer White",
            contact_email="jennifer.w@example.com",
            status="ACCEPTED"
        )
        CampaignResponse.objects.create(
            campaign=campaign4,
            contact_name="Mark Rodriguez",
            contact_email="mark.r@example.com",
            status="ACCEPTED"
        )
        CampaignResponse.objects.create(
            campaign=campaign4,
            contact_name="Nicole Lewis",
            contact_email="nicole.l@example.com",
            status="PENDING"
        )

        # Campaign 5: Holiday Season Campaign
        campaign5 = Campaign.objects.create(
            name="Holiday Season Campaign",
            description="Holiday gift bundles and special packages campaign",
            status="COMPLETED",
            start_date=today - timedelta(days=60),
            end_date=today - timedelta(days=30),
            target_list="Previous Purchasers",
            offer=offer5
        )

        CampaignResponse.objects.create(
            campaign=campaign5,
            contact_name="Robert Harris",
            contact_email="robert.h@example.com",
            status="ACCEPTED"
        )
        CampaignResponse.objects.create(
            campaign=campaign5,
            contact_name="Patricia Clark",
            contact_email="patricia.c@example.com",
            status="ACCEPTED"
        )
        CampaignResponse.objects.create(
            campaign=campaign5,
            contact_name="Christopher Young",
            contact_email="chris.y@example.com",
            status="REJECTED"
        )
        CampaignResponse.objects.create(
            campaign=campaign5,
            contact_name="Susan Hall",
            contact_email="susan.h@example.com",
            status="ACCEPTED"
        )
        CampaignResponse.objects.create(
            campaign=campaign5,
            contact_name="Daniel King",
            contact_email="daniel.k@example.com",
            status="PENDING"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully populated sample data with:\n"
                "- 5 Offers\n"
                "- 13 Treatments\n"
                "- 5 Campaigns\n"
                "- 22 Campaign Responses"
            )
        )
