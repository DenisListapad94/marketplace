from shop.models.base import TimeConfig, Rating
from django.db import models


class ProviderRating(Rating, TimeConfig):
    provider = models.ForeignKey(
        to="Provider",
        related_name="provider_rating",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    provider_detail = models.CharField(max_length=60, null=True)