"""Utilities for updating the item code on existing Serial No records."""

from __future__ import annotations

from typing import Iterable, List

import frappe


def change_item_for_serial(serial_nos: Iterable[str] | str, new_item_code: str) -> None:
    """Update ``item_code`` for the given Serial Numbers.

    Args:
        serial_nos: An iterable of serial numbers or a comma/line separated string
            containing serial numbers to update.
        new_item_code: Item code that should replace the current one.

    The function fetches each ``Serial No`` document and updates its ``item_code``
    directly in the database.  A log entry is created for every changed serial.
    """

    if isinstance(serial_nos, str):
        # Accept comma or newline separated strings and normalise to a list
        serial_nos = [sn.strip() for sn in serial_nos.replace(",", "\n").splitlines() if sn.strip()]

    for serial in serial_nos:  # type: ignore[arg-type]
        doc = frappe.get_doc("Serial No", serial)
        old_item = doc.item_code

        # ``db_set`` bypasses validation, which is useful for administrative fixes
        doc.db_set("item_code", new_item_code)

        frappe.logger(__name__).info(
            "Changed item for Serial No %s from %s to %s", serial, old_item, new_item_code
        )
