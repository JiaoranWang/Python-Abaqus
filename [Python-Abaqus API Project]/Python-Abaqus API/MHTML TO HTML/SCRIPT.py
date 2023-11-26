import jpype
import asposecells

jpype.startJVM()
from asposecells.api import Workbook

workbook = Workbook("Abaqus-Python API Operation Manual.mht");
workbook.Save("Abaqus-Python API Operation Manual.html");
jpype.shutdownJVM()
