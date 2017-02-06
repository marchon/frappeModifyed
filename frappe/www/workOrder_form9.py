# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate

no_cache = 1
no_sitemap = 1

def get_context(context):
	project = []

	for acc in frappe.db.sql("select * from `tabProject` where true", as_dict=1):
			project.append(acc)
			frappe.errprint(acc)	
	
	return {"projects" : project}