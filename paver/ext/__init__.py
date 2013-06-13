"""
  paver.ext
  ~~~~~~~~~

  Redirect imports for extensions.  This module basically makes it possible
  for us to transition from paverext.foo to paver_foo without having to
  force all extensions to upgrade at the same time.

  When a user does ``from paver.ext.foo import bar`` it will attempt to
  import ``from paver_foo import bar`` first and when that fails it will
  try to import ``from paverext.foo import bar``.
"""


def setup():
    from ..exthook import ExtensionImporter
    importer = ExtensionImporter(['paver_%s', 'paverext.%s'], __name__)
    importer.install()


setup()
del setup
