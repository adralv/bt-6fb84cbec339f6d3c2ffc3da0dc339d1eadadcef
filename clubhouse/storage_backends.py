from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings
import os
from urllib.parse import urljoin

class SupabaseStorage(S3Boto3Storage):
    def __init__(self, **kwargs):
        kwargs.update({
            'endpoint_url': settings.SUPABASE_URL + '/storage/v1',
            'access_key': settings.SUPABASE_KEY,
            'secret_key': settings.SUPABASE_KEY,  # Supabase uses key as both access and secret
            'file_overwrite': False,
            'bucket_name': settings.SUPABASE_BUCKET_NAME,
            'auto_create_bucket': False,
            'default_acl': 'public-read',
            'querystring_auth': False,
        })
        super().__init__(**kwargs)

    def url(self, name):
        # Return public URL directly instead of signed URL
        return urljoin(settings.SUPABASE_STORAGE_URL + '/', name)