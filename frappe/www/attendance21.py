# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate

no_cache = 1
no_sitemap = 1

def get_context(context):
	employees = []
	customers = []
	for acc in frappe.db.sql("select employee_name from `tabEmployee` where true", as_dict=1):
			employees.append(acc)
			frappe.errprint(acc)	
	
	for acc in frappe.db.sql("select customer_name from `tabCustomer` where true", as_dict=1):
			customers.append(acc)
			frappe.errprint(acc)		


	return {"Semployees" : employees, "Scustomers" : customers}