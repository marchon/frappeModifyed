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
    q = "select c.employee_name, c.status, c.att_date, `vineyard name`, work_order, t.description, cu.customer_name "
    q = q + "from tabCrv_attendance c join tabvineyards v join tabTasks t join tabCustomer cu on "
    q = q + "(c.vineyard = v.name and t.name = c.task and c.customer = cu.name)"

    for acc in frappe.db.sql(q, as_dict=1):
        result.append(acc)
    
    
    return {"rowContent" : result}
