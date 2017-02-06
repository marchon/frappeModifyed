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
def toDo(desc, person, prio, date):
	frappe.errprint("llama")
	doc = frappe.new_doc("ToDo")
	doc.description = desc
	doc.owner = person
	doc.priority = prio
	doc.date = date
	doc.assigned_by = frappe.session.user
	
	return doc.submit()