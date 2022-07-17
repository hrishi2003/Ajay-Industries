# Copyright (c) 2013, efeone Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document
import frappe
from frappe.utils import (add_days, getdate, formatdate, date_diff,
	add_years, get_timestamp, nowdate, flt, cstr, add_months, get_last_day, cint)
from frappe import _

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	data_n = []
	print(f'\n\n\n\n\n\n\n\n\n\n{data_n}\n\n\n\n\n\n\n\n\n')
	for elem in data:
		# print(f'\n\n\n\n\n\n\n\n\n\nelem{elem}\n\n\n\n\n\n\n\n\n')
		if elem not in data_n:
			data_n.append(elem)
	print(f'\n\n\n\n\n\n\n\n\n\n{data_n}\n\n\n\n\n\n\n\n\n')
	return columns, data_n

def get_columns():
	print("get_columns")
	return[
		# _("Sr No.") + ":Data:100",
		_("Name") + ":Link/Sales Order:150",
		_("Docstatus") + ":Data:150",
		_("Company") + ":Link/Company:150",
		_("Customer") + ":Data:150",
		_("Date") + ":Date:100",
		_("Delivery Date") + ":Date:100",
		_("Item Code") + ":Data:120",
		_("Parent Item") + ":Data:130",
		_("Status") + ":Data:150",
		# _("Sales Order: Item Code") + ":Data:120",
		_("Item Name") + ":Data:120",
		_("From Warehouse") + ":Data:140",
		_("Qty") + ":Data:100",
		# _("Sales Order: Name") + ":Data:150",
	]

def get_data(filters=None):
	print("get_data")
	data=[]
	sales_order_list=frappe.get_all("Sales Order")
	for so in sales_order_list:
		is_inclusive_tax = False
		sales_order_doc = frappe.get_doc("Sales Order",so.name)
		for item in sales_order_doc.packed_items:
			name = sales_order_doc.name if sales_order_doc.name else ""
			docstatus = sales_order_doc.docstatus if sales_order_doc.docstatus else ""
			company = ""
			customer = sales_order_doc.customer if sales_order_doc.customer else ""
			date = sales_order_doc.transaction_date if sales_order_doc.transaction_date else ""
			delivery_date = sales_order_doc.delivery_date if sales_order_doc.delivery_date else ""
			item_code = item.item_code if item.item_code or ''
			parent_item = item.parent_item if item.parent_item else ""
			status =  sales_order_doc.status if sales_order_doc.status else ""
			item_name = item.item_name if item.item_name or ''
			from_warehouse = item.warehouse if item.warehouse or ''
			qty = item.qty if item.qty or ''
			

			row = [
					# sr_no,
					name,
					docstatus,
					company,
					customer,
					date,
					delivery_date,
					item_code,
					parent_item,
					status,
					item_name,
					from_warehouse,
					qty,
			]
			data.append(row)
	return data



# def code(sales_order):
# 	l=[]
# 	sales_order_doc = frappe.get_doc("Sales Order",sales_order)
# 	for i in sales_order_doc.items:
# 		l.append(i.item_code)
# 	for item in sales_order_doc.packed_items:
# 		if item.parent_item not in l:
# 			l.append(item.parent_item)
	
# 	for j in l:
# 		return j	

# def item_qty(sales_order):
# 	l=[]
# 	qty= []
# 	sales_order_doc = frappe.get_doc("Sales Order",sales_order)
# 	for i in sales_order_doc.items:
# 		l.append(i.item_code)
# 		qty.append(i.qty)
# 	for item in sales_order_doc.packed_items:
# 		if item.parent_item not in l:
# 			qty.append(item.qty)

# 	for j in qty:
# 		return j	

# def item_names(sales_order):
# 	name = []
# 	l=[]
# 	sales_order_doc = frappe.get_doc("Sales Order",sales_order)
# 	for i in sales_order_doc.items:
# 		l.append(i.item_code)
# 		name.append(i.item_name)
# 	for item in sales_order_doc.packed_items:
# 		if item.parent_item not in l:
# 			name.append(item.item_name)

# 	for j in name:
# 		return j	

# def item_warehouse(sales_order):
# 	l=[]
# 	warehouse = []
# 	sales_order_doc = frappe.get_doc("Sales Order",sales_order)
# 	for i in sales_order_doc.items:
# 		l.append(i.item_code)
# 		warehouse.append(i.warehouse)
# 	for item in sales_order_doc.packed_items:
# 		if item.parent_item not in l:
# 			warehouse.append(item.warehouse)

# 	for j in warehouse:
# 		return j	

