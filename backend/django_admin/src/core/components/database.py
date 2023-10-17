"""Database."""

import os
from types import MappingProxyType

DATABASES = MappingProxyType(
    {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB', 'notifications_database'),
            'USER': os.environ.get('POSTGRES_USER', 'postgres'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
            'HOST': os.environ.get('POSTGRES_HOST', '127.0.0.1'),
            'PORT': os.environ.get('POSTGRES_PORT', '5432'),
        },
    },
)
