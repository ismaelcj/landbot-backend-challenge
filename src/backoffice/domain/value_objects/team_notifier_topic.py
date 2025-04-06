from enum import Enum


class TeamNotifierTopic(Enum):

    SALES_ASSISTANCE = "assistance.sales"
    PRICING_ASSISTANCE = "assistance.pricing"
    NEW_RETAIL_CUSTOMER = 'customer.retail'
    NEW_WALE_CUSTOMER = 'customer.wale'

    def __str__(self) -> str:
        return self.value
