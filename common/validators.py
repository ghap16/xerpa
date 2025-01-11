from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


VALID_IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
]
 
def valid_image_extension(value):
    if not any([value.endswith(e) for e in VALID_IMAGE_EXTENSIONS]):
        raise ValidationError(
            _("%(value)s is not an image"),
            params={"value": value},
        )
    
def validate_not_zero(value):
    if value == 0:
        raise ValidationError(
            _("%(value)s is zero."),
            params={"value": value},
        )