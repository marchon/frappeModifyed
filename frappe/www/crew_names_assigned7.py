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
    q = "select employee_name, work_order from tabCrv_attendance order by work_order"
    i = 0
    for acc in frappe.db.sql(q, as_dict=1):
        result.append(acc)
    
    row = ""
    result2 = []
    for cont in result: 
        if i>0:
            if cont['work_order'] == result[i-1]['work_order']:
              row = row + ", " + cont['employee_name'] 
            else:
                cont2 = result[i-1]
                cont2['employee_name'] = row
                row = cont['employee_name']
                result2.append(cont2)
        else:
            row = cont['employee_name']
        i = i + 1 
    if i > 0:
        cont2 = result[i-1]
        cont2['employee_name'] = row
        result2.append(cont2)
    return {"rowContent" : result2}
