from django.core.management.base import NoArgsCommand

from server.models import *

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        # now do the things that you want with your models here
        print("sup")

        case = Case()
        case.case_id = "TC"
        case.title = "Test case"
        case.case_type = "DR"
        case.last_date = "???"
        case.save()

        party = Party()
        party.name = "Quasar"
        party.party_type = "P"
        party.side = "P"
        party.case = case
        party.save()


        for i in range(10):
            de = DocketEntry()
            de.case = case
            de.side = "P"
            de.date = "today"
            de.name = "MF"
            de.file = "we are filing a lot"
            de.save()

