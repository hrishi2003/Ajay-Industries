import frappe
from frappe.model.document import Document

    
def ac(self,method=None):    
    if self.requires_branch_accounting:
        if self.currency == 'INR':
            if self.debit_account:
                default_company = frappe.db.get_single_value('Global Defaults', 'default_company')
                doc = frappe.new_doc('GL Entry')
                doc.account = self.debit_account
                doc.voucher_no = self.name
                doc.voucher_type = 'Purchase Invoice'
                doc.debit = self.rounded_total
                doc.against = self.supplier
                doc.party_type = 'Supplier'
                doc.posting_date = self.posting_date
                doc.party = self.supplier
                doc.company = default_company
                doc.cost_center = self.cost_center
                doc.save(ignore_permissions=True)

            if self.credit_account:  
                default_company = frappe.db.get_single_value('Global Defaults', 'default_company') 
                doc = frappe.new_doc('GL Entry')
                doc.account = self.credit_account
                doc.voucher_no = self.name
                doc.voucher_type = 'Purchase Invoice'
                doc.credit = self.rounded_total
                doc.against = self.supplier
                # doc.party_type = 'Customer'
                doc.posting_date = self.posting_date
                # doc.party = self.customer
                doc.company = default_company
                doc.cost_center = self.cost_center
                doc.save(ignore_permissions=True)

        else:
            if self.debit_account:
                default_company = frappe.db.get_single_value('Global Defaults', 'default_company')
                doc = frappe.new_doc('GL Entry')
                doc.account = self.debit_account
                doc.voucher_no = self.name
                doc.voucher_type = 'Purchase Invoice'
                doc.debit = self.base_rounded_total
                doc.against = self.supplier
                doc.party_type = 'Supplier'
                doc.posting_date = self.posting_date
                doc.party = self.supplier
                doc.company = default_company
                doc.cost_center = self.cost_center
                doc.save(ignore_permissions=True)

            if self.credit_account:  
                default_company = frappe.db.get_single_value('Global Defaults', 'default_company') 
                doc = frappe.new_doc('GL Entry')
                doc.account = self.credit_account
                doc.voucher_no = self.name
                doc.voucher_type = 'Purchase Invoice'
                doc.credit = self.base_rounded_total
                doc.against = self.supplier
                # doc.party_type = 'Customer'
                doc.posting_date = self.posting_date
                # doc.party = self.customer
                doc.company = default_company
                doc.cost_center = self.cost_center
                doc.save(ignore_permissions=True)


