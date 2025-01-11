import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.validators import validate_not_zero


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(_("Description"), max_length=100)
    amount = models.DecimalField(_('Amount'), max_digits=8, decimal_places=2, validators=[validate_not_zero])
    date = models.DateTimeField(_("Date"))

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = _("Transaction")
