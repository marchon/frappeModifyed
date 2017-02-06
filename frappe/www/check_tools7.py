# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate

no_cache = 1
no_sitemap = 1

def get_context(context):
	if (frappe.session.user == "Guest" or frappe.db.get_value("User", frappe.session.user, "user_type")=="Website User"):
		frappe.throw(_("You are not permitted to access this page."), frappe.PermissionError)
	else:
		result = []
		return {"rowContent" : result}

@frappe.whitelist()
def enterOperation(op, itemCode, person, date):
	frappe.errprint("llama")
	item = frappe.get_all('equipment',filters={'item_code':itemCode},fields=['name', 'status'])
	if (op == "Check in") and (item[0]['status'] == "In"):
		frappe.msgprint("The item has already been checked in")
	elif (op == "Check out") and (item[0]['status'] == "Out"):
		frappe.msgprint("The item has already been checked out")
	else:
		updateItem = frappe.get_doc('equipment', item[0]['name'])
		doc = frappe.new_doc("equipment_movement")
		doc.operation = op
		doc.item = item[0]['name']
		doc.user = person
		doc.date = date
		doc.submit()
		if (op == "Check in"):
			updateItem.status = "In"
		else:
			updateItem.status = "Out"
		updateItem.save()
		frappe.msgprint(op + " done.")
	return 0