# Copyright (c) 2022, Erpdata and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Ride(Document):
	def before_save(self):
		self.total_amount =0
		for item in self.ride_cost_breakup:
			self.total_amount += item.cost
