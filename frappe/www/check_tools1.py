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
    
    return {"rowContent" : result}

@frappe.whitelist()
def enterOperation(op, itemCode, person, date):
	frappe.errprint("llama")
	item = frappe.get_all('equipment',filters={'item_code':itemCode},fields=['name'])
	frappe.errprint(item)
	doc = frappe.new_doc("equipment_movement")
	doc.operation = op
	doc.item = item[0]['name']
	doc.user = person
	doc.date = date
	
	return doc.submit()