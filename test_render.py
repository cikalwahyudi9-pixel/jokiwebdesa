import os
import sys

sys.path.insert(0, os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

import django
django.setup()

from django.test import Client

client = Client(SERVER_NAME='localhost')

urls_to_test = [
    '/',
    '/tentang/',
    '/video-profil/',
    '/profil/',
    '/potensi/',
    '/umkm/',
    '/artikel/',
    '/galeri/',
    '/program/',
    '/edukasi/',
    '/insight/',
    '/kegiatan/',
]

errors = []
for url in urls_to_test:
    try:
        response = client.get(url)
        if response.status_code != 200:
            errors.append(f"URL {url} returned status {response.status_code}")
        else:
            print(f"URL {url} OK")
    except Exception as e:
        errors.append(f"URL {url} generated exception: {e}")

if errors:
    print("ERRORS FOUND:")
    for err in errors:
        print(err)
    sys.exit(1)
else:
    print("ALL URLS RENDERED SUCCESSFULLY")
