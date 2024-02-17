# first we are going to configure this for our project actully
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "review.settings")

# the we are going to setup our django

import django
django.setup()


from review_app.models import AccessRecord, Topic, Webpage
from faker import Faker
import random
fakegen = Faker()


topics = ["Instagram", "Facebook", "Twitter", "Pintres", "Linkedin"]

def add_topic():
    t = Topic.objects.get_or_create(name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for i in range(N):
        # get the topic for entry
        top=add_topic()

        fake_url = fakegen.url()

        fake_date = fakegen.date()

        fake_name = fakegen.company()

        # Create a new webpage entry

        web = Webpage.objects.get_or_create(topics=top, url=fake_url, name=fake_name)[0]

        # Cerate a new dateEntry

        acc_rec = AccessRecord.objects.get_or_create(name=web, date=fake_date)[0]

if __name__ == "__main__":
    print("Populating database")
    populate(20)
    print("Populating complete")





