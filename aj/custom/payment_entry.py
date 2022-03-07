import frappe
from frappe.model.document import Document

    
def ac(self,method=None):   
    if self.payment_type == 'Pay':
        if self._requires_branch_accounting:
            if self.paid_from_account_currency == 'INR':
                if self.debit_account:
                    default_company = frappe.db.get_single_value('Global Defaults', 'default_company')
                    doc = frappe.new_doc('GL Entry')
                    doc.account = self.debit_account
                    doc.voucher_no = self.name
                    doc.voucher_type = 'Payment Entry'
                    doc.debit = int(self.paid_amount) + int(self.total_taxes_and_charges)
                    doc.party_type = self.party_type
                    doc.posting_date = self.posting_date
                    doc.party = self.party
                    doc.company = default_company
                    doc.save(ignore_permissions=True)

                if self.credit_account:  
                    default_company = frappe.db.get_single_value('Global Defaults', 'default_company') 
                    doc = frappe.new_doc('GL Entry')
                    doc.account = self.credit_account
                    doc.voucher_no = self.name
                    doc.voucher_type = 'Payment Entry'
                    doc.credit = int(self.paid_amount) + int(self.total_taxes_and_charges)
                    # doc.party_type = 'Customer'
                    doc.posting_date = self.posting_date
                    # doc.party = self.customer
                    doc.company = default_company
                    doc.save(ignore_permissions=True)

            else:
                if self.debit_account:
                    default_company = frappe.db.get_single_value('Global Defaults', 'default_company')
                    doc = frappe.new_doc('GL Entry')
                    doc.account = self.debit_account
                    doc.voucher_no = self.name
                    doc.voucher_type = 'Payment Entry'
                    doc.debit = int(self.base_paid_amount) + int(self.base_total_taxes_and_charges)
                    doc.party_type = self.party_type
                    doc.posting_date = self.posting_date
                    doc.party = self.party
                    doc.company = default_company
                    doc.save(ignore_permissions=True)

                if self.credit_account:  
                    default_company = frappe.db.get_single_value('Global Defaults', 'default_company') 
                    doc = frappe.new_doc('GL Entry')
                    doc.account = self.credit_account
                    doc.voucher_no = self.name
                    doc.voucher_type = 'Payment Entry'
                    doc.credit = int(self.base_paid_amount) + int(self.base_total_taxes_and_charges)
                    # doc.party_type = 'Customer'
                    doc.posting_date = self.posting_date
                    # doc.party = self.customer
                    doc.company = default_company
                    doc.save(ignore_permissions=True)



