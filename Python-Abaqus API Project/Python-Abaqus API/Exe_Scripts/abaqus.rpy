# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-22.50.37 167380
# Run by jiaor on Thu May 19 09:12:25 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=178.494781494141, 
    height=68.1307830810547)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('Exe_1.py', __main__.__dict__)
#* SyntaxError: ('invalid syntax', ('Exe_1.py', 335, 31, 
#* 'Create_Boundary_Condition_by_RP(myString, "RP-1", "Displacement_Load", 
#* "Step-1", UNSET, UNSET, 20, UNSET, UNSET, UNSET)\n'))
cliCommand("""import os""")
cliCommand("""import sys""")
cliCommand("""from datetime import datetime""")
cliCommand("""### [Abaqus] Change/set the work dictionary and results ###""")
\
    cliCommand("""# Acquire the time""")
cliCommand("""time = datetime.now().strftime("%Y%m%d%H%M")""")
cliCommand("""# Script Name""")
cliCommand("""name = os.path.basename(sys.argv[0])""")
cliCommand("""name = name[:-3]""")
cliCommand("""# change the work to folder""")
cliCommand("""folder = os.path.abspath(os.path.join(os.getcwd(), ".."))+'\\\\Results\\\\'+'Test_'+time+'_'+name""")
cliCommand("""# make and change the work to folder""")
cliCommand("""os.makedirs(folder)""")
cliCommand("""os.chdir(folder)""")
cliCommand("""# --------------------------#""")
cliCommand("""# python #abaqus #abaqustutorial #hnrwagner""")
cliCommand("""from abaqus import *""")
cliCommand("""from abaqusConstants import *""")
cliCommand("""import regionToolset""")
cliCommand("""import __main__""")
cliCommand("""import section""")
cliCommand("""import regionToolset""")
cliCommand("""import part""")
cliCommand("""import material""")
cliCommand("""import assembly""")
cliCommand("""import step""")
cliCommand("""import interaction""")
cliCommand("""import load""")
cliCommand("""import mesh""")
cliCommand("""import job""")
cliCommand("""import sketch""")
cliCommand("""import visualization""")
cliCommand("""import xyPlot""")
cliCommand("""import connectorBehavior""")
cliCommand("""import odbAccess""")
cliCommand("""from operator import add""")
cliCommand("""# functions""")
cliCommand("""def Create_Part_3D_Cylinder(radius, length, thickness, part, model):
    s1 = mdb.models[model].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(radius, 0.0))
    s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(radius - thickness, 0.0))
    p = mdb.models[model].Part(name=part, dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p = mdb.models[model].parts[part]
    p.BaseSolidExtrude(sketch=s1, depth=length)
    s1.unsetPrimaryObject()
    p = mdb.models[model].parts[part]
    del mdb.models[model].sketches['__profile__']
""")
cliCommand("""def Create_Datum_Plane_by_Principal(type_plane, part, model, offset_plane):
    p = mdb.models[model].parts[part]
    myPlane = p.DatumPlaneByPrincipalPlane(principalPlane=type_plane, offset=offset_plane)
    myID = myPlane.id
    return myID
""")
cliCommand("""def Create_Set_All_Cells(model, part, set_name):
    p = mdb.models[model].parts[part]
    c = p.cells[:]
    p.Set(cells=c, name=set_name)
""")
cliCommand("""def Create_Material_Data(model, material_name, e11, e22, e33, nu12, nu13, nu23, g12, g13, g23, lts, lcs, tts, tcs, lss,
                         tss):
    mdb.models[model].Material(name=material_name)
    mdb.models[model].materials[material_name].Elastic(type=ENGINEERING_CONSTANTS,
                                                       table=((e11, e22, e33, nu12, nu13, nu23, g12, g13, g23),))
    mdb.models[model].materials[material_name].HashinDamageInitiation(table=((lts, lcs, tts, tcs, lss, tss),))
""")
cliCommand("""def Create_Set_Face(x, y, z, model, part, set_name):
    face = ()
    p = mdb.models[model].parts[part]
    f = p.faces
    myFace = f.findAt((x, y, z), )
    face = face + (f[myFace.index:myFace.index + 1],)
    p.Set(faces=face, name=set_name)
    return myFace
""")
cliCommand("""def Create_Set_Edge(x, y, z, model, part, set_name):
    edge = ()
    p = mdb.models[model].parts[part]
    e = p.edges
    myEdge = e.findAt((x, y, z), )
    edge = edge + (e[myEdge.index:myEdge.index + 1],)
    f = p.Set(edges=edge, name=set_name)
    return myEdge
""")
cliCommand("""# -----------------------------------------------------------------------------""")
cliCommand("""def Create_Set_Vertice(x, y, z, model, part, set_name):
    vertice = ()
    p = mdb.models[model].parts[part]
    v = p.vertices
    myVertice = v.findAt((x, y, z), )
    vertice = vertice + (v[myVertice.index:myVertice.index + 1],)
    p.Set(vertices=vertice, name=set_name)
""")
cliCommand("""def Create_Set_Surface(x, y, z, model, part, set_name):
    face = ()
    p = mdb.models[model].parts[part]
    s = p.faces
    myFace = s.findAt((x, y, z), )
    face = face + (s[myFace.index:myFace.index + 1],)
    p.Surface(side1Faces=face, name=set_name)
""")
cliCommand("""def Create_Assembly(model, part, instance_name):
    a = mdb.models[model].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models[model].parts[part]
    a.Instance(name=instance_name, part=p, dependent=ON)
""")
cliCommand("""# -------------------------------------------------------------""")
cliCommand("""def Create_Reference_Point(x, y, z, model, setname):
    a = mdb.models[model].rootAssembly
    myRP = a.ReferencePoint(point=(x, y, z))
    r = a.referencePoints
    myRP_Position = r.findAt((x, y, z), )
    refPoints1 = (myRP_Position,)
    a.Set(referencePoints=refPoints1, name=setname)
    return myRP, myRP_Position
""")
cliCommand("""def Create_Constraint_Equation(model, constraint_name, set_name, set_name_rp):
    mdb.models[model].Equation(name=constraint_name, terms=((1.0, set_name, 3), (-1.0, set_name_rp, 3)))
""")
cliCommand("""def Create_Boundary_Condition_by_Instance(model, instance_name, set_name, BC_name, step_name, u1_BC, u2_BC, u3_BC,
                                          ur1_BC, ur2_BC, ur3_BC):
    a = mdb.models[model].rootAssembly
    region = a.instances[instance_name].sets[set_name]
    mdb.models[model].DisplacementBC(name=BC_name, createStepName=step_name, region=region, u1=u1_BC, u2=u2_BC,
                                     u3=u3_BC, ur1=ur1_BC, ur2=ur2_BC, ur3=ur3_BC, amplitude=UNSET,
                                     distributionType=UNIFORM, fieldName='', localCsys=None)
""")
cliCommand("""def Create_Boundary_Condition_by_RP(model, RP_name, BC_name, step_name, u1_BC, u2_BC, u3_BC, ur1_BC, ur2_BC, ur3_BC):
    a = mdb.models[model].rootAssembly
    region = a.sets[RP_name]
    mdb.models[model].DisplacementBC(name=BC_name, createStepName=step_name, region=region, u1=u1_BC, u2=u2_BC,
                                     u3=u3_BC, ur1=ur1_BC, ur2=ur2_BC, ur3=ur3_BC, amplitude=UNSET,
                                     distributionType=UNIFORM, fieldName='', localCsys=None)
""")
cliCommand("""def Create_Analysis_Step(model, step_name, pre_step_name, Initial_inc, Max_inc, Min_inc, Inc_Number, NL_ON_OFF):
    a = mdb.models[model].StaticStep(name=step_name, previous=pre_step_name, initialInc=Initial_inc, maxInc=Max_inc,
                                     minInc=Min_inc)
    a = mdb.models[model].steps[step_name].setValues(maxNumInc=Inc_Number)
    a = mdb.models[model].steps[step_name].setValues(nlgeom=NL_ON_OFF)
    a = mdb.models[model].steps[step_name].setValues(stabilizationMagnitude=1E-009, stabilizationMethod=DAMPING_FACTOR,
                                                     continueDampingFactors=False, adaptiveDampingRatio=None)
""")
cliCommand("""def Create_Partion_by_Plane(model, part, id_plane):
    p = mdb.models[model].parts[part]
    c = p.cells[:]
    d = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d[id_plane], cells=c)
""")
cliCommand("""# -----------------------------------------------------------------------------""")
cliCommand("""def Create_Composite_Layup(model, part, set_name, composite_name, number, material, thickness, angle):
    layupOrientation = None
    p = mdb.models[model].parts[part]
    region1 = p.sets[set_name]
    normalAxisRegion = p.surfaces['Outer_Surface']
    primaryAxisRegion = p.sets['Set-Top-Edge']
    compositeLayup = mdb.models[model].parts[part].CompositeLayup(name=composite_name, description='',
                                                                  elementType=CONTINUUM_SHELL, symmetric=False)
    compositeLayup.Section(preIntegrate=OFF, integrationRule=SIMPSON, poissonDefinition=DEFAULT, thicknessModulus=None,
                           temperature=GRADIENT, useDensity=OFF)
    for i in range(0, number, 1):
        compositeLayup.CompositePly(suppressed=False, plyName='Ply-' + str(i), region=region1, material=material,
                                    thicknessType=SPECIFY_THICKNESS, thickness=thickness,
                                    orientationType=SPECIFY_ORIENT, orientationValue=angle[i],
                                    additionalRotationType=ROTATION_NONE, additionalRotationField='', axis=AXIS_3,
                                    angle=0.0, numIntPoints=3)
        compositeLayup.ReferenceOrientation(orientationType=DISCRETE, localCsys=None,
                                            additionalRotationType=ROTATION_ANGLE, angle=90.0,
                                            additionalRotationField='', axis=AXIS_3, stackDirection=STACK_3,
                                            normalAxisDefinition=SURFACE, normalAxisRegion=normalAxisRegion,
                                            normalAxisDirection=AXIS_3, flipNormalDirection=False,
                                            primaryAxisDefinition=EDGE, primaryAxisRegion=primaryAxisRegion,
                                            primaryAxisDirection=AXIS_2, flipPrimaryDirection=False)
""")
cliCommand("""# ----------------------------------------------------------------------------""")
cliCommand("""def Create_Mesh(model, part, size):
    p = mdb.models[model].parts[part]
    elemType1 = mesh.ElemType(elemCode=SC8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, hourglassControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=SC6R, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=UNKNOWN_TET, elemLibrary=STANDARD)
    cells = p.cells[:]
    pickedRegions = (cells,)
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))
    p.seedPart(size=size, deviationFactor=0.1, minSizeFactor=0.1)
    p.generateMesh()
""")
cliCommand("""def Create_SPLA(model, instance_name, set_name, load_name, step_name, load):
    a = mdb.models[model].rootAssembly
    region = a.instances[instance_name].sets[set_name]
    mdb.models[model].ConcentratedForce(name=load_name, createStepName=step_name, region=region, cf2=load,
                                        distributionType=UNIFORM, field='', localCsys=None)
""")
cliCommand("""def Create_Pressure_Load(model, instance_name, load_name, step_name, surface, load):
    a = mdb.models[model].rootAssembly
    region = a.instances[instance_name].surfaces[surface]
    mdb.models[model].Pressure(name=load_name, createStepName=step_name, region=region, distributionType=UNIFORM,
                               field='', magnitude=load, amplitude=UNSET)
""")
cliCommand("""def CreateCutout(model, part, radius_cutout, id_plane, edge, x, y, z):
    p = mdb.models[model].parts[part]
    e, d = p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=d[id_plane], sketchUpEdge=edge, sketchPlaneSide=SIDE1,
                              sketchOrientation=RIGHT, origin=(x, y, z))
    s = mdb.models[model].ConstrainedSketch(name='__profile__', sheetSize=2000.0, gridSpacing=20.0, transform=t)
    g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(radius_cutout, 0.0))
    p.CutExtrude(sketchPlane=d[id_plane], sketchUpEdge=edge, sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, sketch=s,
                 flipExtrudeDirection=OFF)
    s.unsetPrimaryObject()
    del mdb.models[model].sketches['__profile__']
""")
cliCommand("""def AssignStack(model, part, face):
    p = mdb.models[model].parts[part]
    c = p.cells[:]
    p.assignStackDirection(referenceRegion=face, cells=c)
""")
cliCommand("""def CreateJob(model, job_name, cpu):
    a = mdb.models[model].rootAssembly
    mdb.Job(name=job_name, model=model, description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0,
            queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=SINGLE,
            nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
            userSubroutine='', scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=cpu, numDomains=cpu,
            numGPUs=0)
""")
cliCommand("""def SubmitJob(job_name):
    mdb.jobs[job_name].submit(consistencyChecking=OFF)
""")
cliCommand("""# variables""")
cliCommand("""myString = "Buckling_Analysis\"""")
cliCommand("""myRadius = 25.0""")
cliCommand("""myThickness = 2.5""")
cliCommand("""myLength = 526.0""")
cliCommand("""myModel = mdb.Model(name=myString)""")
#: The model "Buckling_Analysis" has been created.
cliCommand("""myPart = "Cylinder\"""")
cliCommand("""# material parameters""")
cliCommand("""myE11 = 133000""")
cliCommand("""myE22 = 11500""")
cliCommand("""myE33 = 11500""")
cliCommand("""myNu12 = 0.32""")
cliCommand("""myNu13 = 0.32""")
cliCommand("""myNu23 = 0.37""")
cliCommand("""myG12 = 4800""")
cliCommand("""myG13 = 4800""")
cliCommand("""myG23 = 4200""")
cliCommand("""myAngle = [-45, 45, 90, 0, 0, 90, 45, -45]""")
cliCommand("""myPlyNumber = len(myAngle)""")
cliCommand("""# hashin damage parameters""")
cliCommand("""myLTS = 1200""")
cliCommand("""myLCS = 972""")
cliCommand("""myTTS = 37""")
cliCommand("""myTCS = 147""")
cliCommand("""myLSS = 71.5""")
cliCommand("""myTSS = 32""")
cliCommand("""Mesh_Size = 2.0""")
cliCommand("""# create model""")
cliCommand("""Create_Part_3D_Cylinder(myRadius, myLength, myThickness, myPart, myString)""")
cliCommand("""myID_1 = Create_Datum_Plane_by_Principal(XZPLANE, myPart, myString, 0.0)""")
cliCommand("""myID_2 = Create_Datum_Plane_by_Principal(XYPLANE, myPart, myString, myLength / 2.0)""")
cliCommand("""myID_3 = Create_Datum_Plane_by_Principal(YZPLANE, myPart, myString, 0.0)""")
cliCommand("""myID_4 = Create_Datum_Plane_by_Principal(XZPLANE, myPart, myString, 50.0)""")
cliCommand("""Create_Set_All_Cells(myString, myPart, "Cylinder_3D")""")
cliCommand("""Create_Set_Face(myRadius - myThickness / 2.0, 0.0, myLength, myString, myPart, "Set-RP-2")""")
#: mdb.models['Buckling_Analysis'].parts['Cylinder'].faces[2]
cliCommand("""Create_Set_Face(myRadius - myThickness / 2.0, 0.0, 0.0, myString, myPart, "Set-RP-1")""")
#: mdb.models['Buckling_Analysis'].parts['Cylinder'].faces[3]
cliCommand("""Create_Set_Face(myRadius, 0.0, myLength / 2.0, myString, myPart, "Outer_Surface")""")
#: mdb.models['Buckling_Analysis'].parts['Cylinder'].faces[0]
cliCommand("""Create_Set_Surface(myRadius, 0.0, myLength / 2.0, myString, myPart, "Outer_Surface")""")
cliCommand("""Create_Set_Surface(myRadius - myThickness, 0.0, myLength / 2.0, myString, myPart, "Internal_Surface")""")
cliCommand("""Create_Material_Data(myString, "CFRP", myE11, myE22, myE33, myNu12, myNu13, myNu23, myG12, myG13, myG23, myLTS, myLCS,
                     myTTS, myTCS, myLSS, myTSS)""")
cliCommand("""Create_Assembly(myString, myPart, "Cylinder-1")""")
cliCommand("""myRP1, myRP_Position1 = Create_Reference_Point(0.0, 0.0, 0.0, myString, "RP-1")""")
cliCommand("""# myRP2,myRP_Position2 = Create_Reference_Point(0.0,0.0,myLength,myString,"RP-2")""")
cliCommand("""Create_Constraint_Equation(myString, "Constraint-RP-1", "Cylinder-1." + str("Set-RP-1"), "RP-1")""")
cliCommand("""# Create_Constraint_Equation(myString,"Constraint-RP-2","Cylinder-1."+str("Set-RP-2"),"RP-2")""")
cliCommand("""# Create_Analysis_Step(myString,"Step-1","Initial",1.0,1.0,1E-05,100,ON)""")
cliCommand("""Create_Analysis_Step(myString, Create_Boundary_Condition_by_Instance(myString, "Cylinder-1", "Set-RP-2", "BC-Set-RP-2", "Initial", SET, SET, SET,
                                      UNSET, UNSET, UNSET)
Create_Boundary_Condition_by_RP(myString, "RP-1", "Displacement_Load", "Step-1", UNSET, UNSET, 20, UNSET, UNSET, UNSET)""")
#*     Create_Boundary_Condition_by_RP(myString, "RP-1", "Displacement_Load", 
#* "Step-1", UNSET, UNSET, 20, UNSET, UNSET, UNSET)
#*                                   ^
#* SyntaxError: invalid syntax
cliCommand("""Create_Boundary_Condition_by_RP(myString, "RP-1", "Displacement_Load", "Step-1", UNSET, UNSET, 20, UNSET, UNSET, UNSET)""")
#* Unknown step type.
