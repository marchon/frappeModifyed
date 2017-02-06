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
def toDo(desc, person):
	frappe.errprint("llama")
	user = frappe.get_doc({"doctype" : "User", "email" : person})
	frappe.errprint("desc" + person)
	frappe.errprint(user)
	doc = frappe.new_doc({
			"doctype" : "ToDo",
			"description": desc,
			"owner": person
		})
	return doc.insert()