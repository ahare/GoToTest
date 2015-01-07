import sublime, sublime_plugin, os.path

class GoToTestCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    desiredfile = ""
    currentfile = self.view.file_name()
    if currentfile.endswith("_test.go"):
      desiredfile = currentfile[:-8] + ".go"
    else:
      desiredfile = currentfile[:-3] + "_test.go"
    if os.path.isfile(desiredfile):
      sublime.active_window().open_file(desiredfile)
