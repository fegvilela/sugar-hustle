from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class DeliveryType(str, Enum):
    DELIVERY = "delivery"
    TAKEOUT = "takeout"


class MeasurementUnit(str, Enum):
    G = "g"
    KG = "kg"
    L = "L"
    ML = "mL"
    UNITS = "unit(s)"


class ResourceType(str, Enum):
    INGRIDIENT = "ingredient"
    PACKAGING = "packaging"


@dataclass
class Orders:
    id: int
    client_id: int
    delivery_type: DeliveryType
    is_paid: bool = False
    total_price: float
    discount: float = 0.0
    scheduled_to: datetime
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None


@dataclass
class OrderDetails:
    id: int
    order_id: int
    product_id: int
    product_quantity: int
    note: str = ""
    unit_price: float
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None


@dataclass
class Products:
    id: int
    name: str
    description: str = ""
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None


@dataclass
class ProductDetails:
    id: int
    product_id: int
    quantity: float = 0.0
    measurement_unit: MeasurementUnit
    note: str = ""
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None


@dataclass
class Clients:
    id: int
    name: str
    address: str = ""
    phone_number: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None


@dataclass
class Resources:
    id: int
    name: str
    description: str = ""
    type: ResourceType
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None
