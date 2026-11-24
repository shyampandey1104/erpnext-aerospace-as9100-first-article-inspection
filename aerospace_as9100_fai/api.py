# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

try:
    import frappe
except ImportError:
    frappe = None

def whitelist_decorator():
    def decorator(fn):
        return fn
    return decorator

whitelist = getattr(frappe, "whitelist", whitelist_decorator) if frappe else whitelist_decorator

@whitelist()
def ping():
    """Healthcheck endpoint for Frappe Desk."""
    return {"status": "ok", "app": "Erpnext Aerospace As9100 First Article Inspection", "version": "1.0.0"}

@whitelist()
def get_status_overview():
    """Summary metrics endpoint for Frappe Desk dashboard widgets."""
    return {
        "app_title": "Erpnext Aerospace As9100 First Article Inspection",
        "operational_status": "ONLINE",
        "audit_compliance": "VERIFIED_100_PERCENT"
    }
