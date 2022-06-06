from django.core.management.base import BaseCommand
from app.models import CryptoPair


class Command(BaseCommand):
    def handle(self, *args, **options):
        typelist = ["UST/USD",
                   "SHIB/USD",
                   "LUNC/USD",
                   "TRX/USD",
                   "BCH/USD",
                   "BTC/ZAR",
                   "WAVES/USD",]
        for i in typelist:
            c = CryptoPair(name=i)
            c.save()
