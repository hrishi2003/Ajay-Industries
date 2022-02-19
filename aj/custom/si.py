import frappe
from frappe.model.document import Document


@frappe.whitelist()
def get_mapped_income_account(customer):
    income_account = ""
    if frappe.db.exists({ 'doctype': 'Income Account Mapping', 'customer': customer }):
        income_account = frappe.db.get_value('Income Account Mapping', {'customer': customer}, ['income_account'])
    return income_account