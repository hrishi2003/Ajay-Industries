import frappe
from frappe.model.document import Document


@frappe.whitelist()
def get_mapped_income_account(customer):
    income_account = ""
    if frappe.db.exists({ 'doctype': 'Income Account Mapping', 'customer': customer }):
        income_account = frappe.db.get_value('Income Account Mapping', {'customer': customer}, ['income_account'])
    return income_account

def ac(self,method=None):
    if self.customer_tax_not_payable:
        gl = frappe.get_doc('GL Entry',{'account':self.debit_to,'voucher_no':self.name,'posting_date':self.posting_date})
        gl.debit = gl.debit - self.total_taxes_and_charges
        print('gllllllllllllllllllllll',gl.voucher_no,'gggggggggggggggggggggggggggggggggcvvvvvvvvvv%%%%%%%%%%')
        print('gllllllllllllllllllllll',gl.debit,'gggggggggggggggggggggggggggggggggcvvvvvvvvvv%%%%%%%%%%')
        frappe.db.set_value('GL Entry', {'account':self.debit_to,'voucher_no':self.name,'posting_date':self.posting_date}, 'debit', gl.debit)
        default_company = frappe.db.get_single_value('Global Defaults', 'default_company')
        doc = frappe.new_doc('GL Entry')
        doc.account = self.gst_account
        doc.voucher_no = self.name
        doc.voucher_type = 'Sales Invoice'
        doc.debit = self.total_taxes_and_charges
        doc.against = self.customer
        doc.party_type = 'Customer'
        doc.posting_date = self.posting_date
        doc.party = self.customer
        doc.company = default_company
        doc.save(ignore_permissions=True)

    