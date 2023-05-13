from portfolio.forms import MailingForm
from portfolio.models import Work


def mailing_data(data) -> dict:
    data = data
    work_qs = Work.objects.filter(asset_id=data['name_of_work'])
    context = {

    }
    print(work_qs)
    return context



