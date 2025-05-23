#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb
Department.drop_tables()
Department.create_tables()

# payroll = Department("Payroll", "Build A, 5th Floor")
payroll = Department.create("Payroll", "Build A, 5th Floor")
# print(payroll)
# print(payroll)
payroll.name = "PAYROLL"
payroll.location = "Build B, 10th Floor"
payroll.update()
print(payroll)
# payroll.save()
# print(payroll)
hr = Department.create("Human Resources", "Building C, East Wing")
# print(hr)

# hr = Department("Human Resources", "Building C, East Wing")
# print(hr)
# hr.save()
# print(hr)
hr.name = "HR"
hr.location = "Builing D, West Wing"
hr.update()
print(hr)



ipdb.set_trace()
