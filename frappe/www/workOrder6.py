# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate

no_cache = 1
no_sitemap = 1

def get_context(context):
	result = []
	for acc in frappe.db.sql("select * from `tabWork Order` where status = 'Working'", as_dict=1):
			result.append(acc)
			frappe.errprint(acc)
	

	return {"rowContent" : result}
