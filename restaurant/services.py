from typing import Iterable
from .models import Restaurant, MenuItem


def create_restaurant_with_default_menu(
    name: str,
    address: str = "",
    phone: str = "",
) -> Restaurant:
    restaurant = Restaurant.objects.create(
        name=name,
        address=address,
        phone=phone,
        is_active=True,
    )

    default_items = [
        {"name": "Rice & Curry", "price": 450.00},
        {"name": "Fried Rice", "price": 550.00},
    ]
    for item in default_items:
        MenuItem.objects.create(
            restaurant=restaurant,
            name=item["name"],
            price=item["price"],
            is_available=True,
        )

    return restaurant


def bulk_update_menu_availability(
    restaurant: Restaurant,
    available_ids: Iterable[int],
) -> None:
    MenuItem.objects.filter(restaurant=restaurant).update(is_available=False)
    MenuItem.objects.filter(
        restaurant=restaurant,
        id__in=list(available_ids),
    ).update(is_available=True)


