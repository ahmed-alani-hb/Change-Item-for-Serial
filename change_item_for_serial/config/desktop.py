from frappe import _

def get_data():
    return [
        {
            "module_name": "Change Item for Serial",
            "color": "grey",
            "icon": "octicon octicon-tag",
            "type": "link",
            "label": _("Change Item for Serial"),
            "link": "Form/Change Item For Serial",
        }
    ]
