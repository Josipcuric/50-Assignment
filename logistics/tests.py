from django.test import TestCase
from django.contrib.auth.models import User
from .models import Campaign

class CampaignTest(TestCase):
    def test_campaign_creation(self):
        user = User.objects.create_user(username='manager', password='password')
        campaign = Campaign.objects.create(
            title="Ad Test", description="Testing", start_date="2025-01-01",
            end_date="2025-12-31", manager=user
        )
        self.assertEqual(campaign.title, "Ad Test")
