from django.core.management.base import NoArgsCommand

from server.models import *

from .process import get_everything

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        # now do the things that you want with your models here
        print("sup")

        e = get_everything()

        case = Case()
        case.case_id = e['main_case_info']['Case ID'][0]
        case.title = "Case Loaded from scraper"
        case.case_type = "DR"
        case.last_date = "???"
        case.save()


        for p in e['parties']:
            party = Party()
            party.name = p['name']
            party.party_type = p['type']
            party.side = "P"
            party.case = case
            party.save()

        return

        for i in range(10):
            de = DocketEntry()
            de.case = case
            de.side = "P"
            de.date = "today"
            de.name = "MF"
            de.file = "we are filing a lot"
            de.save()

