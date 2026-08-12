"""
Jelajah Sumberagung — Base Settings
"""

from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY', default='django-insecure-change-me-in-production')
DEBUG = env('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

INSTALLED_APPS = [
    # Jazzmin harus sebelum django.contrib.admin
    'jazzmin',

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'tinymce',
    'imagekit',

    # Project apps
    'apps.core',
    'apps.pages',
    'apps.profil',
    'apps.potensi',
    'apps.umkm',
    'apps.artikel',
    'apps.galeri',
    'apps.program',
    'apps.edukasi',
    'apps.insight',
    'apps.kegiatan',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.core.context_processors.site_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Google Analytics
GOOGLE_ANALYTICS_ID = env('GOOGLE_ANALYTICS_ID', default='')

# TinyMCE configuration
TINYMCE_DEFAULT_CONFIG = {
    'height': 400,
    'menubar': True,
    'plugins': [
        'advlist autolink lists link image charmap preview anchor',
        'searchreplace visualblocks code fullscreen',
        'insertdatetime media table paste code help wordcount',
    ],
    'toolbar': (
        'undo redo | formatselect | bold italic underline | '
        'alignleft aligncenter alignright alignjustify | '
        'bullist numlist outdent indent | removeformat | help'
    ),
    'language': 'id',
}

# File upload limits
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/webp']
ALLOWED_DOCUMENT_TYPES = ['application/pdf', 'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.ms-powerpoint',
    'application/vnd.openxmlformats-officedocument.presentationml.presentation',
]

# Jazzmin Admin Configuration
JAZZMIN_SETTINGS = {
    'site_title': 'Jelajah Sumberagung',
    'site_header': 'Jelajah Sumberagung',
    'site_brand': 'Admin Panel',
    'site_logo': None,
    'welcome_sign': 'Selamat datang di Admin Panel Jelajah Sumberagung',
    'copyright': 'Tim KKN Universitas Diponegoro 2026',
    'search_model': ['artikel.Artikel', 'umkm.UMKM'],
    'topmenu_links': [
        {'name': 'Lihat Website', 'url': '/', 'new_window': True},
    ],
    'show_sidebar': True,
    'navigation_expanded': True,
    'order_with_respect_to': [
        'pages', 'profil', 'potensi', 'umkm',
        'artikel', 'galeri', 'program', 'edukasi', 'insight', 'kegiatan',
    ],
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
        'artikel.Artikel': 'fas fa-newspaper',
        'artikel.KategoriArtikel': 'fas fa-tags',
        'umkm.UMKM': 'fas fa-store',
        'umkm.KategoriUMKM': 'fas fa-tags',
        'umkm.FotoUMKM': 'fas fa-image',
        'umkm.PendampinganBeforeAfter': 'fas fa-exchange-alt',
        'galeri.ItemGaleri': 'fas fa-images',
        'galeri.KategoriGaleri': 'fas fa-tags',
        'program.Program': 'fas fa-hand-holding-heart',
        'program.DokumentasiProgram': 'fas fa-camera',
        'edukasi.ItemEdukasi': 'fas fa-book-open',
        'edukasi.KategoriEdukasi': 'fas fa-tags',
        'insight.EventKesehatan': 'fas fa-heartbeat',
        'insight.DataAgregatKesehatan': 'fas fa-chart-bar',
        'kegiatan.Kegiatan': 'fas fa-calendar-alt',
        'profil.ProfilDesa': 'fas fa-map-marker-alt',
        'potensi.ItemPotensi': 'fas fa-leaf',
        'potensi.KategoriPotensi': 'fas fa-tags',
        'core.Kontribusi': 'fas fa-comments',
    },
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',
    'use_google_fonts_cdn': True,
    'show_ui_builder': False,
    'changeform_format': 'horizontal_tabs',
    'language_chooser': False,
    'custom_css': 'css/jazzmin_custom.css',
}

JAZZMIN_UI_TWEAKS = {
    'navbar_small_text': False,
    'footer_small_text': False,
    'body_small_text': False,
    'brand_small_text': False,
    'brand_colour': 'navbar-dark',
    'accent': 'accent-success',
    'navbar': 'navbar-dark',
    'no_navbar_border': True,
    'navbar_fixed': True,
    'layout_boxed': False,
    'footer_fixed': False,
    'sidebar_fixed': True,
    'sidebar': 'sidebar-dark-primary',
    'sidebar_nav_small_text': False,
    'sidebar_disable_expand': False,
    'sidebar_nav_child_indent': False,
    'sidebar_nav_compact_style': False,
    'sidebar_nav_legacy_style': False,
    'sidebar_nav_flat_style': False,
    'theme': 'darkly',
    'dark_mode_theme': 'darkly',
    'button_classes': {
        'primary': 'btn-primary',
        'secondary': 'btn-secondary',
        'info': 'btn-info',
        'warning': 'btn-warning',
        'danger': 'btn-danger',
        'success': 'btn-success',
    },
}
