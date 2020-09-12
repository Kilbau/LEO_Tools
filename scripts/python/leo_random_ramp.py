import hou
import random
import numpy
from PySide2 import QtCore, QtUiTools, QtWidgets

class RandomRamp(QtWidgets.QWidget):

	def __init__(self):
		super(RandomRamp,self).__init__()
		ui_file = "D:/Projects/LEO_DEV/random_ramp/leo_random_ramp.ui"
		self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
		self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)

		self.ui.button_apply.clicked.connect(self.apply_button)
		self.ui.button_update_node.clicked.connect(self.update_button)

		# self.ui.setWindowTitle("LEO Random Ramp") # doesnt work
		# self.ui.setFixedSize(300,600) # Doesnt disable resizing

		# init values
		self.node = None
		self.node_name = None
		self.ramp_parms = []
		self.ramp_parm = None
		self.basis_types = [
					"Linear", "Constant", "CatmullRom", 
					"MonotoneCubic", "Bezier", "BSpline", "Hermite"
					]
		self.ramp_basis = None
		self.resolution = None

		self.min_set_value = None
		self.max_set_value = None

		self.min_adj_value = None
		self.max_adj_value = None

		self.ramp_values = None
		self.ramp_keys = None

		# set basis dropdown
		self.ui.dropdown_basis.clear()
		self.ui.dropdown_basis.addItems(self.basis_types)

	# def calc_mean(self,data):
	# 	"""
	# 	workaround since the statistics module doesnt exist for Python 2.x
	# 	"""
	# 	return float(sum(data)) / float(len(data))

	def update_values(self):
		"""
		updates variables to match the current ui state
		"""
		self.resolution = self.ui.value_samples.value()

		self.min_set_value = self.ui.value_set_min.value()
		self.max_set_value = self.ui.value_set_max.value()
		self.min_adj_value = self.ui.value_adjust_min.value()
		self.max_adj_value = self.ui.value_adjust_max.value()


	def update_ui(self):
		"""
		updates the ui to represent current values
		"""

		# updates Selected Node Label 
		self.ui.label_node_name.setText("Selected Node: {}".format(self.node_name))

		# updates parms dropdown
		self.ui.dropdown_parm.clear()
		self.ui.dropdown_parm.addItems(self.ramp_parms)

	def get_selected_node(self):
		"""
		returns the first selected node and name
		"""
		try:
			self.node = hou.selectedNodes()[0]
			self.node_name = self.node.name()
		except IndexError:
			self.node = None
			self.node_name = None

	def get_ramp_parms(self):
		"""
		for the selected node return a list of all ramp parameters.
		"""
		try:
			ramp_parms = [parm.name() for parm in self.node.parms() 
						if parm.parmTemplate().type() == hou.parmTemplateType.Ramp]
		except AttributeError:
			ramp_parms = []
		except hou.ObjectWasDeleted:
			ramp_parms = []

		if len(ramp_parms) == 0:
			self.ramp_parms = ["No Ramp Parameter Found!"]
		else:
			self.ramp_parms = ramp_parms

	def get_ramp_basis(self):
		"""
		returns hou.rampBasis object which is responsible for the interpolation
		""" 
		selected_basis = self.ui.dropdown_basis.currentText()
		self.ramp_basis = getattr(hou.rampBasis, selected_basis)

	def create_new_ramp_values(self):
		"""
		returns a new ramp with random values between in_min and in_max
		resolution is the number of points in the ramp
		"""
		ramp_values = tuple(random.uniform(self.min_set_value, self.max_set_value) 
					for _ in range(self.resolution))
		self.ramp_values = ramp_values

	def create_adj_ramp_values(self):
		"""
		returns a new ramp based on the existing ramp but the values are offset
		optional the output values are clamped to 0 - 1 to avoid negative values
		"""
		old_ramp = self.ramp_parm.evalAsRamp()

		if old_ramp.isColor():
			# ramp_values = [self.calc_mean(old_ramp.lookup(position))
			# 				+ random.uniform(self.min_adj_value, self.max_adj_value)
			# 				for position in self.ramp_keys
			# 			]

			ramp_values = []
			for position in self.ramp_keys:
				random_value = random.uniform(self.min_adj_value, self.max_adj_value)
				r, g, b = old_ramp.lookup(position)
				
				r += random_value
				g += random_value
				b += random_value

				ramp_values.append((r,g,b))


		else:
			ramp_values = [old_ramp.lookup(position) 
							+ random.uniform(self.min_adj_value, self.max_adj_value)
							for position in self.ramp_keys
						]
		
		if self.ui.checkbox_adjust_clamp.isChecked():
			ramp_values = numpy.clip(ramp_values, 0, 1)
			
		self.ramp_values = tuple(ramp_values)

	def create_ramp_keys(self):
		"""
		returns a tuple from 0 to inclusive 1 evenly distributed
		requires numpy as range() doesnt support floats
		output tuple is len() == resolution, starts with 0.0 and ends with 1.0
		"""
		try:
			ramp_keys = list(numpy.linspace(0,1,self.resolution))
		except ZeroDivisionError:
			ramp_keys = []

		ramp_keys = tuple(ramp_keys)
		self.ramp_keys = ramp_keys

	def get_ramp_parm(self):
		"""
		updates the hou.node.parm with the selected parm
		if the node or parm is not found this will return False
		"""
		ramp_parm_name = self.ui.dropdown_parm.currentText()
		try:
			ramp_parm = self.node.parm(ramp_parm_name)
			self.ramp_parm = ramp_parm
			if self.ramp_parm:
				return True
			else:
				return False
		except hou.ObjectWasDeleted:
			return False
		except AttributeError:
			return False

	def set_ramp(self):
		"""
		applies the new ramp to the selected parameter.
		"""
		# hou.Ramp((basis, basis),(0, 1),(2.5, 4.5))
		ramp = hou.Ramp((self.ramp_basis, self.ramp_basis), self.ramp_keys, self.ramp_values)
		self.ramp_parm.set(ramp)

	def set_warning(self,message):
		self.ui.label_node_name.setText("Warning: {}".format(message))


	def update_button(self):
		"""
		functionality for the "update selected node" button
		"""
		self.get_selected_node()
		
		if self.node:
			self.get_ramp_parms()
			self.update_ui()
		else:
			self.get_ramp_parms()
			self.update_ui()
			self.set_warning("No Valid Node Selected!")

	def apply_button(self):
		"""
		functionality for the "apply" button
		"""

		if self.get_ramp_parm():

			self.get_ramp_basis()

			self.update_values()

			self.create_ramp_keys()

			if self.ui.radiobutton_override.isChecked():
				self.create_new_ramp_values()
				self.set_ramp()
			elif self.ui.radiobutton_adjust.isChecked():
				self.create_adj_ramp_values()
				self.set_ramp()	
			else:
				self.set_warning("Abort: Invalid Radio Button selection")

		else:
			self.get_ramp_parms()
			self.update_ui()
			self.set_warning("Select A Valid Node And Parameter")

	def test(self):
		print(self.ui.value_set_min.value())

def run():
	win = RandomRamp()
	win.show()
