# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "aerospace_as9100_fai"
app_title = "Erpnext Aerospace As9100 First Article Inspection"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Aerospace As9100 First Article Inspection - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/aerospace_as9100_fai/css/aerospace_as9100_fai.bundle.css"
app_include_js = "/assets/aerospace_as9100_fai/js/aerospace_as9100_fai.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Aerospace As9100 First Article Inspection Entry": {
        "validate": "aerospace_as9100_fai.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "aerospace_as9100_fai.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "aerospace_as9100_fai.tasks.hourly_sync"
    ],
    "daily": [
        "aerospace_as9100_fai.tasks.daily_reconciliation"
    ],
    "weekly": [
        "aerospace_as9100_fai.tasks.weekly_digest"
    ]
}
