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
	for elem in data:
		if elem not in data_n:
			data_n.append(elem)
	return columns, data_n

def get_columns():
	print("get_columns")
	return[
		_("Name") + ":Link/Sales Order:150",
		_("Docstatus") + ":Data:150",
		_("Company") + ":Link/Company:150",
		_("Customer") + ":Data:150",
		_("Date") + ":Date:100",
		_("Delivery Date") + ":Date:100",
		_("Item Code") + ":Data:120",
		_("Parent Item") + ":Data:130",
		_("Status") + ":Data:150",
		_("Item Name") + ":Data:120",
		_("From Warehouse") + ":Data:140",
		_("Qty") + ":Data:100",
	]

def get_data(filters=None):
	print("get_data")
	data=[]
	sales_order_list=frappe.get_all("Sales Order",filters=[['docstatus','in',['0','1']]])
	for so in sales_order_list:
		is_inclusive_tax = False
		sales_order_doc = frappe.get_doc("Sales Order",so.name)
		for items in sales_order_doc.items:
			if sales_order_doc.packed_items:
				for item in sales_order_doc.packed_items:
					if items.item_code == item.parent_item:
						name = sales_order_doc.name if sales_order_doc.name else ""
						docstatus = sales_order_doc.docstatus if sales_order_doc.docstatus else ""
						company = ""
						customer = sales_order_doc.customer if sales_order_doc.customer else ""
						date = sales_order_doc.transaction_date if sales_order_doc.transaction_date else ""
						delivery_date = sales_order_doc.delivery_date if sales_order_doc.delivery_date else ""
						item_code = item.item_code if item.item_code else ''
						parent_item = item.parent_item if item.parent_item else ""
						status =  sales_order_doc.status if sales_order_doc.status else ""
						item_name = item.item_name if item.item_name else ''
						from_warehouse = item.warehouse if item.warehouse else ''
						qty = item.qty if item.qty else ''

						row = [
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

					else:
						l=[]
						bundle = frappe.get_all('Product Bundle','new_item_code')
						for i in bundle:
							l.append(i['new_item_code'])
						if items.item_code not in l:
							print('!£$%^&*90876543245678976543')
							name = sales_order_doc.name if sales_order_doc.name else ""
							docstatus = sales_order_doc.docstatus if sales_order_doc.docstatus else ""
							company = ""
							customer = sales_order_doc.customer if sales_order_doc.customer else ""
							date = sales_order_doc.transaction_date if sales_order_doc.transaction_date else ""
							delivery_date = sales_order_doc.delivery_date if sales_order_doc.delivery_date else ""
							item_code = items.item_code if items.item_code not in sales_order_doc.packed_items else ''
							parent_item = ""
							status =  sales_order_doc.status if sales_order_doc.status else ""
							item_name = items.item_name if items.item_code not in l else ''
							from_warehouse = items.warehouse if items.item_code not in l else ''
							qty = items.qty if items.item_code not in l else ''

						row = [
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

			else:
				name = sales_order_doc.name if sales_order_doc.name else ""
				docstatus = sales_order_doc.docstatus if sales_order_doc.docstatus else ""
				company = ""
				customer = sales_order_doc.customer if sales_order_doc.customer else ""
				date = sales_order_doc.transaction_date if sales_order_doc.transaction_date else ""
				delivery_date = sales_order_doc.delivery_date if sales_order_doc.delivery_date else ""
				item_code = items.item_code if items.item_code else ''
				parent_item = ""
				status =  sales_order_doc.status if sales_order_doc.status else ""
				item_name = items.item_name if items.item_name else ''
				from_warehouse = items.warehouse if items.warehouse else ''
				qty = items.qty if items.qty else ''

				row = [
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