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
		self.allimports = []

	def _getFileLines(self, filename):
		if not os.path.isfile(filename):
			return []
		return [line.rstrip('\n') for line in open(filename)]

	def _getFileNameByImport(self, root_dir, importtext):
		if importtext.startswith('dart:'):
			return importtext
			
		if importtext.startswith('package:'):
			return os.path.abspath(os.path.join(self.packages_dir , importtext[8:]))

		return os.path.abspath(os.path.join(root_dir, importtext))


	def parse(self, filename, indent="", stack=[]):
		imports = []        
		logging.info("{0}'{1}'".format(indent, filename))
		script_dir = os.path.dirname(filename)
		for line in self._getFileLines(filename):
			match = self.importpattern.match(line)
			if match:
				imptext = match.group(1)
				impfile = self._getFileNameByImport(script_dir, imptext)

				append = True
				if impfile in stack:
					logging.info("{0}'{1}' - [loop detected]".format(indent + self.indent, impfile))
					append = False
				elif impfile in self.allimports:
					logging.info("{0}'{1}' - [repeat detected]".format(indent + self.indent, impfile))
					append = False
				else:
					self.allimports.append(impfile)
                
				if append:
					imports.append(self.parse(impfile, indent + self.indent, stack + [impfile]))


		return ImportElement(filename, imports)

if __name__ == '__main__':
	logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',stream=sys.stdout, level=logging.INFO)
	rootpath = sys.argv[1]
	packages_dir = sys.argv[2]
	dt = DartImportTree(packages_dir)
	imp = dt.parse(rootpath)
        