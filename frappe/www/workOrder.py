# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate

no_cache = 1
no_sitemap = 1

def get_context(context):
	result = ["test1","test2"]
	#for acc in frappe.db.sql("select * from tabwork_order where status = 'Working'")
			#result.append(acc)
	

	return {"rowContent" : result}