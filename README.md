# Tools for working with Dart code

imports_tree.py - Get tree of imports for specified dart file.
---------------

Get tree of imports for specified file.

Usage:
```
        python imports_tree.py D:\Reps\dart_web_toolkit\test\dart_web_toolkit_test.dart D:\Reps\dart_web_toolkit\packages
```

Example of output:

```
2017-09-27 22:59:28,182 INFO 'D:\Reps\dart_web_toolkit\test\dart_web_toolkit_test.dart'
2017-09-27 22:59:28,182 INFO   'dart:html'
2017-09-27 22:59:28,183 INFO   'D:\Reps\dart_web_toolkit\packages\unittest/unittest.dart'
2017-09-27 22:59:28,183 INFO     'dart:async'
2017-09-27 22:59:28,184 INFO     'dart:collection'
2017-09-27 22:59:28,184 INFO     'dart:isolate'
2017-09-27 22:59:28,184 INFO     'D:\Reps\dart_web_toolkit\packages\matcher/matcher.dart'
2017-09-27 22:59:28,184 INFO     'D:\Reps\dart_web_toolkit\packages\unittest\src/utils.dart'
2017-09-27 22:59:28,185 INFO       'D:\Reps\dart_web_toolkit\packages\stack_trace/stack_trace.dart'
2017-09-27 22:59:28,185 INFO     'D:\Reps\dart_web_toolkit\packages\unittest\src/configuration.dart'
2017-09-27 22:59:28,186 INFO       'D:\Reps\dart_web_toolkit\packages\unittest/unittest.dart' show TestCase'
2017-09-27 22:59:28,187 INFO   'D:\Reps\dart_web_toolkit\packages\dart_web_toolkit/event.dart'
2017-09-27 22:59:28,188 INFO     'dart:html'
2017-09-27 22:59:28,188 INFO     'dart:async'
2017-09-27 22:59:28,188 INFO   'D:\Reps\dart_web_toolkit\packages\dart_web_toolkit/ui.dart'
2017-09-27 22:59:28,189 INFO     'dart:html'
2017-09-27 22:59:28,189 INFO     'dart:math'
2017-09-27 22:59:28,189 INFO     'D:\Reps\dart_web_toolkit\packages\dart_web_toolkit\event.dart'
2017-09-27 22:59:28,190 INFO       'dart:html'
2017-09-27 22:59:28,190 INFO       'dart:async'
```
