import logging
import sys
import re
import os.path

class ImportElement:
	def __init__(self, name, imports):
		self.name = name
		self.imports = imports

class DartImportTree:
	def __init__(self, packages_dir):
		self.importpattern = re.compile('\\s*import\\s*[\',\"](.*?)[\',\"]')
		self.packages_dir = packages_dir
		self.indent = "  "

	def _getFileLines(self, filename):
		if not os.path.isfile(filename):
			return []
		return [line.rstrip('\n') for line in open(filename)]

	def _getFileNameByImport(self, root_dir, importtext):
		if importtext.startswith('dart:'):
			return importtext

		if importtext.startswith('package:'):
			return os.path.join(self.packages_dir , importtext[8:])

		return os.path.join(root_dir, importtext)


	def parse(self, filename, indent="", stack=[]):
		imports = []
		logging.info("{0}'{1}'".format(indent, filename))
		script_dir = os.path.dirname(filename)
		for line in self._getFileLines(filename):
			match = self.importpattern.match(line)
			if match:
				imptext = match.group(1)
				impfile = self._getFileNameByImport(script_dir, imptext)
				if impfile not in stack:
					imports.append(self.parse(impfile, indent + self.indent, stack + [impfile]))
				else:
					logging.info("{0}'{1}' - loop detected".format(indent + self.indent, impfile))


		return ImportElement(filename, imports)

if __name__ == '__main__':
	logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',stream=sys.stdout, level=logging.INFO)
	rootpath = sys.argv[1]
	packages_dir = sys.argv[2]
	dt = DartImportTree(packages_dir)
	imp = dt.parse(rootpath)
        