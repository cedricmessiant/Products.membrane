"""\
skeleton tests package
"""
from Products.Archetypes.public import process_types
from Products.Archetypes.public import listTypes

from Products.membrane.config import PROJECTNAME
import dummy

content_types, constructors, ftis = process_types(listTypes(PROJECTNAME),
                                                  PROJECTNAME)