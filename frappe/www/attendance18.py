# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate

no_cache = 1
no_sitemap = 1

def get_context(context):
	emp = frappe.session.user
	#user = frappe.db.get_values("User", emp, "*")[0]
	employee = frappe.db.get_values("Employee", {"user_id":emp}, "*")[0]
	
	employee_ = employee['employee']
	employee_name = employee['employee_name']
	att_date = getdate(nowdate())
	company = employee['company']	

	return { "employee" : employee_,
		"employee_name" : employee_name,
		"att_date" : att_date,
		"company": company}
