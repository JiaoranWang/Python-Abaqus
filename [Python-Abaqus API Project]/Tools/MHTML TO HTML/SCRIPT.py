import jpype
import asposecells

jpype.startJVM()
from asposecells.api import Workbook
### To change the .mht => .html
workbook = Workbook("Abaqus-Python API Operation Manual.mht");
workbook.Save("Abaqus-Python API Operation Manual.html");
jpype.shutdownJVM()
