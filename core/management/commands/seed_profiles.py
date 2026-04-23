from django.core.management.base import BaseCommand
from core.models import Profile
import json
import uuid
from django.utils import timezone
from pathlib import Path

class Command(BaseCommand):
    help = 'Seed the database with profiles from a JSON file.'

    def add_arguments(self, parser):
        parser.add_argument('json_path', type=str, help='Path to the profiles JSON file')

    def handle(self, *args, **options):
        json_path = options['json_path']
        with open(json_path, 'r', encoding='utf-8') as f:
            profiles = json.load(f)
        created, skipped = 0, 0
        for p in profiles:
            obj, created_flag = Profile.objects.get_or_create(
                name=p['name'],
                defaults={
                    'id': uuid.uuid7(),
                    'gender': p['gender'],
                    'gender_probability': p['gender_probability'],
                    'age': p['age'],
                    'age_group': p['age_group'],
                    'country_id': p['country_id'],
                    'country_name': p['country_name'],
                    'country_probability': p['country_probability'],
                    'created_at': p.get('created_at', timezone.now()),
                }
            )
            if created_flag:
                created += 1
            else:
                skipped += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded: {created}, Skipped (duplicates): {skipped}"))
