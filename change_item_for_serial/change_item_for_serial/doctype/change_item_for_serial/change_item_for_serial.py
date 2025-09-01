"""Server-side logic for Change Item For Serial doctype."""

from __future__ import annotations

import frappe
from frappe.model.document import Document


# Import the utility function directly to avoid name collisions with the
# package's nested module of the same name.
from change_item_for_serial.utils import (
    change_item_for_serial as change_serial_util,
)


class ChangeItemForSerial(Document):
    """Single DocType used to change the item code for Serial Nos."""
    pass


@frappe.whitelist()
def change_item(serial_nos: str, new_item_code: str) -> None:
    """Endpoint to update item codes for provided Serial Nos."""
    change_serial_util(serial_nos, new_item_code)
