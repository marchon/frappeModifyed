# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate

no_cache = 1
no_sitemap = 1

def get_context(context):
	if (frappe.session.user == "Guest" or
        frappe.db.get_value("User", frappe.session.user, "user_type")=="Website User"):
        	frappe.throw(_("You are not permitted to access this page."), frappe.PermissionError)

	vineyards = []
	clients = []

	for acc in frappe.db.sql("select * from `tabvineyards` where true", as_dict=1):
			vineyards.append(acc)
			frappe.errprint(acc)	
			
	for acc in frappe.db.sql("select * from `tabCustomer` where true", as_dict=1):
			clients.append(acc)
			frappe.errprint(acc)		
	

	return {"SClient" : clients}
