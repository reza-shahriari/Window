from django.core.management.base import BaseCommand
from backend.srvs.office.gate.models import User


class Command(BaseCommand):
    help = "create a super user"

    def handle(self, *args, **options) -> None:
        print("started process ...")
        User.objects.create_superuser(username="amin.bidad.200@gmail.com", password="1234")
