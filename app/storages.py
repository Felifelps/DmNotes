# myapp/storages.py

from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    default_acl = 'public-read'
    file_overwrite = False

    def get_object_parameters(self, name):
        return {
            'ContentType': self._infer_content_type(name),
        }

    def _infer_content_type(self, name):
        import mimetypes
        content_type, _ = mimetypes.guess_type(name)
        return content_type or 'application/octet-stream'
