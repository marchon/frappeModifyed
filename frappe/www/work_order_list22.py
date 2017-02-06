# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate

no_cache = 1
no_sitemap = 1

ROWS_PER_PAGE = 1

def get_context(context):
	result = []
	q = "select name, subject, project, status, priority, exp_start_date, expected_time, task_weight, exp_end_date, progress, description, depends_on_tasks, act_start_date, actual_time, act_end_date, total_costing_amount, total_expense_claim, total_billing_amount, review_date, closing_date, company from `tabWork Order`"

	#q = "select `tabWork Order`.company, description, customer_name, address, country from tabCustomer join `tabWork Order` join tabProject join tabCompany on (`tabWork Order`.company = tabCompany.company_name and `tabWork Order`.project = tabProject.project_name and tabCustomer.customer_name = tabProject.customer)"
	#q = q + " where `tabWork Order`.status = 'Working'"
	for acc in frappe.db.sql(q, as_dict=1):
			result.append(acc)
			frappe.errprint(acc)
	

	return {"rowContent" : result,
			"pages" : ROWS_PER_PAGE}
