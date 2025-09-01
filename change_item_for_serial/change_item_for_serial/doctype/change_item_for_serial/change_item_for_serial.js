frappe.ui.form.on('Change Item For Serial', {
    refresh(frm) {
        frm.add_custom_button(__('Change Item'), () => {
            frappe.call({
                method: 'change_item_for_serial.change_item_for_serial.doctype.change_item_for_serial.change_item_for_serial.change_item',
                args: {
                    serial_nos: frm.doc.serial_nos,
                    new_item_code: frm.doc.new_item_code
                },
                callback() {
                    frappe.msgprint(__('Item code updated'));
                }
            });
        });
    }
});
