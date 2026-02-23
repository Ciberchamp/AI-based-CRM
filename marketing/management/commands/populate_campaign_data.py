from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta, date
from marketing.models import Campaign, CampaignResponse, Offer


class Command(BaseCommand):
    help = "Populate sample data for Campaigns and Campaign Responses"

    def handle(self, *args, **options):
        # Clear existing campaign data
        Campaign.objects.all().delete()
        CampaignResponse.objects.all().delete()

        today = date.today()

        # Get or create a sample offer (if none exists)
        offer, created = Offer.objects.get_or_create(
            code="OFFER_001",
            defaults={
                "name": "Spring Discount Offer",
                "description": "20% off all products this spring",
                "status": "ACTIVE",
                "start_date": today,
                "end_date": today + timedelta(days=90),
            }
        )

        # Campaign 1: Email Promotion
        campaign1 = Campaign.objects.create(
            name="Spring Email Promotion",
            description="Email campaign promoting spring discounts",
            status="ACTIVE",
            start_date=today - timedelta(days=10),
            end_date=today + timedelta(days=20),
            target_list="Active Customers List",
            offer=offer
        )

        # Add responses for Campaign 1
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

        # Campaign 2: Social Media Campaign
        campaign2 = Campaign.objects.create(
            name="Social Media Awareness Campaign",
            description="Multi-channel social media campaign to increase brand awareness",
            status="ACTIVE",
            start_date=today - timedelta(days=5),
            end_date=today + timedelta(days=25),
            target_list="Social Media Followers",
            offer=offer
        )

        # Add responses for Campaign 2
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

        # Campaign 3: Planned Campaign
        campaign3 = Campaign.objects.create(
            name="Summer Collection Launch",
            description="Campaign for launching new summer product collection",
            status="PLANNED",
            start_date=today + timedelta(days=30),
            end_date=today + timedelta(days=60),
            target_list="Fashion Enthusiasts",
            offer=offer
        )

        # Add sample responses for Campaign 3
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

        # Campaign 4: Draft Campaign
        campaign4 = Campaign.objects.create(
            name="Holiday Season Campaign",
            description="Comprehensive campaign for holiday shopping season",
            status="DRAFT",
            start_date=today + timedelta(days=120),
            end_date=today + timedelta(days=180),
            target_list="Holiday Shoppers Segment",
            offer=offer
        )

        # Add sample responses for Campaign 4
        CampaignResponse.objects.create(
            campaign=campaign4,
            contact_name="Jennifer White",
            contact_email="jennifer.w@example.com",
            status="PENDING"
        )

        # Campaign 5: Completed Campaign
        campaign5 = Campaign.objects.create(
            name="Winter Flash Sale",
            description="Limited-time winter flash sale campaign",
            status="COMPLETED",
            start_date=today - timedelta(days=60),
            end_date=today - timedelta(days=30),
            target_list="Previous Purchasers",
            offer=offer
        )

        # Add responses for Campaign 5
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
                f"Successfully populated sample data with 5 campaigns and 22 campaign responses!"
            )
        )
