import datetime
import sublime, sublime_plugin

class FirstCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if region.empty():
				line = self.view.line(region)
				dt = datetime.datetime.now().strftime("%Y-%m-%d")
				self.view.insert(edit, line.begin(), dt)
