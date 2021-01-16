import clr

# Import RevitAPI
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('RevitNodes')
import Revit
# Import geometry conversion extension methods
clr.ImportExtensions(Revit.GeometryConversion)
# Import ToDSType(bool) extension method
clr.ImportExtensions(Revit.Elements)

# Import DocumentManager and TransactionManager
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Imports Ilists module into python
clr.AddReference('System')
from System.Collections.Generic import List as cList

# Ilist Application
New_List = cList[ElementId]("elements")

doc = DocumentManager.Instance.CurrentDBDocument
uidoc=DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
app = uiapp.Application
uiapp = DocumentManager.Instance.CurrentUIApplication

# Function to convert input to list if it is not a list + unwrap it
def toList(x):
	if isinstance(x,list): return UnwrapElement(x)
	else : return [UnwrapElement(x)]

# The input ports
input_element = toList(IN[0]) # Convert to list if necessary

#Do some action in a Transaction
TransactionManager.Instance.EnsureInTransaction(doc)

TransactionManager.Instance.TransactionTaskDone()

# Output and Changing element to Dynamo for export
# https://github.com/DynamoDS/Dynamo/wiki/Python-0.6.3-to-0.7.x-Migration#wrapping
# <element>.ToDSType(True), #Not created in script, mark as Revit-owned
# <element>.ToDSType(False) #Created in script, mark as non-Revit-owned

OUT = element


#### Things to add
# ways to handle input with multiple list levels. this was encountered before somewhere. find it and add it
