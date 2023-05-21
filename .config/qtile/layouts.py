from libqtile.layout.xmonad import MonadTall
from libqtile.layout.columns import Columns
from libqtile.layout.matrix import Matrix
from libqtile.layout.max import Max

from themes import Colors

class Layouts:
	
	color = Colors()

	def monadTall(self):
		layout = MonadTall(
			border_focus = self.color.red,
			border_normal = self.color.grey,
			single_border_width = 0,
			single_margin = 10,
			margin = 10,
		)
		return layout
	
	def max(self):
		layout = Max()
		return layout
	
	def matrix(self):
		layout = Matrix(
			border_focus = self.color.red,
			border_normal = self.color.grey,
			border_width = 2,
			margin = 8,
		)
		return layout
	
	def columns(self):
		layout = Columns(
			border_focus = self.color.red,
			border_focus_stack = self.color.red,
			border_normal = self.color.grey,
			border_normal_stack = self.color.red,
			insert_position = 1,
			margin = 8,
		)
		return layout
	
	
	def init_layouts(self):
		return [
			self.monadTall(),
			self.max(),
			# self.matrix(),
			#self.columns(),
		]
