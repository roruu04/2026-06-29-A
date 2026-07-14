import decimal
from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class Customer:
    CustomerId : int
    FirstName : Optional[str] = None
    LastName : Optional[str] = None
    Company : Optional[str] = None
    Address : Optional[str] = None
    City : Optional[str] = None
    State : Optional[str] = None
    Country : Optional[str] = None
    PostalCode : Optional[str] = None
    Phone : Optional[str] = None
    Fax : Optional[str] = None
    Email : Optional[str] = None
    SupportRepId : Optional[int] = None
    totaleFatturato : Optional[float]=None

    def __hash__(self):
        return hash(self.CustomerId)
    def __eq__(self, other):
        return self.CustomerId == other.CustomerId
    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
