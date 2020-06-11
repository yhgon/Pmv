########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Tuesday 20 June 2006 10:55:35 
#    
#       The Scripps Research Institute (TSRI)
#       Molecular Graphics Lab
#       La Jolla, CA 92037, USA
#
# Copyright: Daniel Stoffler, Michel Sanner and TSRI
#   
# revision: Guillaume Vareille
#  
#########################################################################
#
# $Header$
#
# $Id$
#
import os

from traceback import print_exc

## loading libraries ##
from Pmv.VisionInterface.PmvNodes import pmvlib
masterNet.getEditor().addLibraryInstance(pmvlib,"Pmv.VisionInterface.PmvNodes", "pmvlib")

from Volume.VisionInterface.VolumeNodes import vollib
masterNet.getEditor().addLibraryInstance(vollib,"Volume.VisionInterface.VolumeNodes", "vollib")

from Vision.StandardNodes import stdlib
masterNet.getEditor().addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

from MolKit.VisionInterface.MolKitNodes import molkitlib
masterNet.getEditor().addLibraryInstance(molkitlib,"MolKit.VisionInterface.MolKitNodes", "molkitlib")

from DejaVu.VisionInterface.DejaVuNodes import vizlib
masterNet.getEditor().addLibraryInstance(vizlib,"DejaVu.VisionInterface.DejaVuNodes", "vizlib")

try:
    ## saving node Select MolFrag ##
    from MolKit.VisionInterface.MolKitNodes import NodeSelector
    Select_MolFrag_0 = NodeSelector(constrkw = {}, name='Select MolFrag', library=molkitlib)
    masterNet.addNode(Select_MolFrag_0,201,156)
    Select_MolFrag_0.inputPortByName['selectionString'].widget.set("CA", run=False)
except:
    print "WARNING: failed to restore NodeSelector named Select MolFrag in network masterNet"
    print_exc()
    Select_MolFrag_0=None

try:
    ## saving node Extract Atom Property ##
    from MolKit.VisionInterface.MolKitNodes import AtomsProperty
    Extract_Atom_Property_1 = AtomsProperty(constrkw = {}, name='Extract Atom Property', library=molkitlib)
    masterNet.addNode(Extract_Atom_Property_1,136,203)
    Extract_Atom_Property_1.inputPortByName['propertyName'].widget.set("coords", run=False)
    apply(Extract_Atom_Property_1.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore AtomsProperty named Extract Atom Property in network masterNet"
    print_exc()
    Extract_Atom_Property_1=None

try:
    ## saving node UT-BlurSpheres(1) ##
    from Volume.VisionInterface.VolumeNodes import UTblurSpheres
    UT_BlurSpheres_1__4 = UTblurSpheres(constrkw = {}, name='UT-BlurSpheres(1)', library=vollib)
    masterNet.addNode(UT_BlurSpheres_1__4,179,297)
    UT_BlurSpheres_1__4.inputPortByName['blobbyness'].widget.set(-0.7, run=False)
    apply(UT_BlurSpheres_1__4.inputPortByName['resX'].widget.configure, (), {'labelCfg': {'text': 'X res  (Xdim=31)       '}})
    UT_BlurSpheres_1__4.inputPortByName['resX'].widget.set(1.5, run=False)
    apply(UT_BlurSpheres_1__4.inputPortByName['resY'].widget.configure, (), {'labelCfg': {'text': 'Y res  (Ydim=32)       '}})
    UT_BlurSpheres_1__4.inputPortByName['resY'].widget.set(1.5, run=False)
    apply(UT_BlurSpheres_1__4.inputPortByName['resZ'].widget.configure, (), {'labelCfg': {'text': 'Z res  (Zdim=31)       '}})
    UT_BlurSpheres_1__4.inputPortByName['resZ'].widget.set(1.5, run=False)
    apply(UT_BlurSpheres_1__4.inputPortByName['switch'].widget.configure, (), {'command': UT_BlurSpheres_1__4.usedims_cb})
except:
    print "WARNING: failed to restore UTblurSpheres named UT-BlurSpheres(1) in network masterNet"
    print_exc()
    UT_BlurSpheres_1__4=None

try:
    ## saving node Dial ##
    from Vision.StandardNodes import DialNE
    Dial_5 = DialNE(constrkw = {}, name='Dial', library=stdlib)
    masterNet.addNode(Dial_5,360,141)
    Dial_5.inputPortByName['dial'].widget.set(3.0, run=False)
except:
    print "WARNING: failed to restore DialNE named Dial in network masterNet"
    print_exc()
    Dial_5=None

try:
    ## saving node UT-Isocontour ##
    from Volume.VisionInterface.VolumeNodes import Isocontour
    UT_Isocontour_6 = Isocontour(constrkw = {}, name='UT-Isocontour', library=vollib)
    masterNet.addNode(UT_Isocontour_6,171,363)
except:
    print "WARNING: failed to restore Isocontour named UT-Isocontour in network masterNet"
    print_exc()
    UT_Isocontour_6=None

try:
    ## saving node heme2DChain ##
    from DejaVu.VisionInterface.GeometryNodes import IndexedPolygonsNE
    heme2DChain_7 = IndexedPolygonsNE(constrkw = {}, name='heme2DChain', library=vizlib)
    masterNet.addNode(heme2DChain_7,152,441)
    apply(heme2DChain_7.inputPortByName['name'].configure, (), {'color': 'white', 'cast': True, 'shape': 'oval'})
    heme2DChain_7.inputPortByName['name'].unbindWidget()
    apply(heme2DChain_7.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore IndexedPolygonsNE named heme2DChain in network masterNet"
    print_exc()
    heme2DChain_7=None

try:
    ## saving node Pmv Viewer ##
    from Pmv.VisionInterface.PmvNodes import PmvViewer
    Pmv_Viewer_8 = PmvViewer(viewer=masterNet.editor.vf.GUI.VIEWER, constrkw = {'viewer': 'masterNet.editor.vf.GUI.VIEWER'}, name='Pmv Viewer', library=pmvlib)
    masterNet.addNode(Pmv_Viewer_8,247,544)
    ##
    ## Saving State for Viewer
    Pmv_Viewer_8.vi.TransformRootOnly(1)
    ##

    ## Light Model
    ## End Light Model

    ## Light sources
    ## End Light sources 7

    ## Cameras
    ## Camera Number 0
    state = {'color': (0.0, 0.0, 0.0, 1.0), 'height': 488, 'lookAt': [0.0, 0.0, 0.0], 'rootx': 37, 'pivot': [0.0, 0.0, 0.0], 'translation': [0.0, 0.0, 0.0], 'sideBySideTranslation': 0.0, 'fov': 40.0, 'scale': [1.0, 1.0, 1.0], 'stereoMode': 'MONO', 'width': 654, 'sideBySideRotAngle': 3.0, 'boundingbox': 0, 'projectionType': 0, 'contours': False, 'direction': [0.0, 0.0, -30.0], 'far': 50.0, 'lookFrom': [0.0, 0.0, 30.0], 'antialiased': False, 'rotation': [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0], 'suspendRedraw': False, 'near': 0.10000000000000001, 'drawThumbnail': False, 'rooty': 103}
    apply(Pmv_Viewer_8.vi.cameras[0].Set, (), state)

    state = {'end': 40, 'density': 0.10000000000000001, 'color': (0.0, 0.0, 0.0, 1.0), 'enabled': 1, 'start': 25, 'mode': 'GL_LINEAR'}
    apply(Pmv_Viewer_8.vi.cameras[0].fog.Set, (), state)

    ## End Cameras

    ## Clipping planes
    ## End Clipping planes

    ## Root object
    state = {'blendFunctions': ('GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA'), 'stippleLines': False, 'replace': True, 'scissorAspectRatio': 1.0, 'immediateRendering': False, 'shading': 'smooth', 'pivot': [83.500075920400988, 43.145352350575962, 2.6762942887498062], 'translation': [-83.50007583774142, -43.145350892594998, -2.6762933654744256], 'scissorH': 200, 'frontPolyMode': 'fill', 'inheritFrontPolyMode': False, 'inheritStippleLines': 0, 'inheritShading': False, 'instanceMatrices': [[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scissorX': 0, 'scissorY': 0, 'listed': True, 'inheritPointWidth': 0, 'pickable': 1, 'pointWidth': 3, 'scissorW': 200, 'culling': 'back', 'stipplePolygons': False, 'pickableVertices': False, 'inheritMaterial': False, 'depthMask': 1, 'scale': [0.25904384577437878, 0.25904384577437878, 0.25904384577437878], 'lighting': False, 'inheritCulling': False, 'inheritStipplePolygons': 0, 'rotation': [-0.152919977903, 0.773267865181, 0.61536359787, 0.0, 0.429013133049, 0.612895965576, -0.663555800915, 0.0, -0.890260159969, 0.162528112531, -0.425466090441, 0.0, 0.0, 0.0, 0.0, 1.0], 'transparent': False, 'outline': False, 'name': 'root', 'backPolyMode': 'fill', 'visible': True, 'inheritBackPolyMode': False, 'scissor': 0, 'protected': True, 'inheritLineWidth': 0, 'lineWidth': 1, 'inheritXform': 0}
    apply(Pmv_Viewer_8.vi.rootObject.Set, (), state)

    ## End Root Object

    ## Material for root
    if Pmv_Viewer_8.vi.rootObject:
        pass  ## needed in case there no modif
    ## End Materials for root

    ## Clipping Planes for root
    if Pmv_Viewer_8.vi.rootObject:
        Pmv_Viewer_8.vi.rootObject.clipP = []
        Pmv_Viewer_8.vi.rootObject.clipPI = []
        pass  ## needed in case there no modif
    ## End Clipping Planes for root

except:
    print "WARNING: failed to restore PmvViewer named Pmv Viewer in network masterNet"
    print_exc()
    Pmv_Viewer_8=None

try:
    ## saving node Select MolFrag ##
    from MolKit.VisionInterface.MolKitNodes import NodeSelector
    Select_MolFrag_9 = NodeSelector(constrkw = {}, name='Select MolFrag', library=molkitlib)
    masterNet.addNode(Select_MolFrag_9,56,30)
    Select_MolFrag_9.inputPortByName['nodeType'].widget.set("Chain", run=False)
    Select_MolFrag_9.inputPortByName['selectionString'].widget.set("A,B,C,D", run=False)
except:
    print "WARNING: failed to restore NodeSelector named Select MolFrag in network masterNet"
    print_exc()
    Select_MolFrag_9=None

try:
    ## saving node iterate ##
    from Vision.StandardNodes import Iterate
    iterate_10 = Iterate(constrkw = {}, name='iterate', library=stdlib)
    masterNet.addNode(iterate_10,111,94)
except:
    print "WARNING: failed to restore Iterate named iterate in network masterNet"
    print_exc()
    iterate_10=None

try:
    ## saving node Get id ##
    from Vision.StandardNodes import GetAttr
    Get_id_11 = GetAttr(constrkw = {}, name='Get id', library=stdlib)
    masterNet.addNode(Get_id_11,43,236)
    apply(Get_id_11.inputPortByName['attr'].widget.configure, (), {'choices': ['AAradii', 'AtomRadiiPatterns', 'NodesFromName', '_MarkTree', '__cmp__', '__doc__', '__eq__', '__hash__', '__init__', '__module__', '__ne__', '__repr__', '__str__', '_atomRadius', '_copyNode', '_numberOfDeletedNodes', '_uniqIndex', 'addBond', 'adopt', 'assignUniqIndex', 'attach_nonbonded_fragments', 'bonds', 'buildBondsBhtree', 'buildBondsByDistance', 'buildBondsByDistanceOnAtoms', 'buildBrokenBonds', 'childByName', 'children', 'childrenName', 'childrenSetClass', 'closerThan', 'compare', 'compiled_patterns', 'configureProgressBar', 'connectResidues', 'defaultRadii', 'deleteSubTree', 'dump', 'elementType', 'findLevels', 'findType', 'full_name', 'gaps', 'get', 'getAtoms', 'getCenter', 'getNext', 'getParentOfType', 'getPrevious', 'getRoot', 'getTypeList', 'hasBonds', 'id', 'isAbove', 'isBelow', 'isDna', 'isHetatmChain', 'isProteic', 'makeNameUniq', 'merge', 'mergeNPH', 'name', 'number', 'p', 'parent', 'parser', 'read', 'remove', 'removeAllHydrogens', 'removeBond', 'residues', 'secondaryStructure', 'setClass', 'shortestDist', 'split', 'subTree', 'top', 'updateProgressBar', 'write']})
    Get_id_11.inputPortByName['attr'].widget.set("id", run=False)
except:
    print "WARNING: failed to restore GetAttr named Get id in network masterNet"
    print_exc()
    Get_id_11=None

try:
    ## saving node Filename ##
    from Vision.StandardNodes import Filename
    Filename_12 = Filename(constrkw = {}, name='Filename', library=stdlib)
    masterNet.addNode(Filename_12,36,368)
    apply(Filename_12.inputPortByName['number'].configure, (), {'datatype': 'object', 'cast': True, 'shape': 'oval', 'color': 'white'})
    Filename_12.inputPortByName['format'].widget.set("heme2%sChain", run=False)
    apply(Filename_12.configure, (), {'expanded': False})
except:
    print "WARNING: failed to restore Filename named Filename in network masterNet"
    print_exc()
    Filename_12=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_13 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_13,35,305)
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_13=None

try:
    ## saving node RemoveDupVert ##
    from DejaVu.VisionInterface.DejaVuNodes import RemoveDuplicatedVerticesNE
    RemoveDupVert_14 = RemoveDuplicatedVerticesNE(constrkw = {}, name='RemoveDupVert', library=vizlib)
    masterNet.addNode(RemoveDupVert_14,36,453)
except:
    print "WARNING: failed to restore RemoveDuplicatedVerticesNE named RemoveDupVert in network masterNet"
    print_exc()
    RemoveDupVert_14=None

try:
    ## saving node QSlim ##
    from DejaVu.VisionInterface.DejaVuNodes import QSlim
    QSlim_15 = QSlim(constrkw = {}, name='QSlim', library=vizlib)
    masterNet.addNode(QSlim_15,36,499)
    apply(QSlim_15.inputPortByName['percent'].widget.configure, (), {'continuous': None})
    QSlim_15.inputPortByName['percent'].widget.set(49.3421052632, run=False)
    QSlim_15.inputPortByName['targetfaces'].widget.set("2850", run=False)
except:
    print "WARNING: failed to restore QSlim named QSlim in network masterNet"
    print_exc()
    QSlim_15=None

try:
    ## saving node hemoglobin_deoxy ##
    mol = masterNet.editor.vf.loadMoleculeIfNeeded("Data"+os.sep+"hemoglobin-deoxy.pdb")
    assert mol
    from Pmv.VisionInterface.PmvNodes import PmvMolecule
    hemoglobin_deoxy_16 = PmvMolecule(molecule=masterNet.editor.vf.expandNodes("hemoglobin_deoxy")[0], constrkw = {'molecule': 'masterNet.editor.vf.expandNodes("hemoglobin_deoxy")[0]'}, name='hemoglobin_deoxy', library=pmvlib)
    masterNet.addNode(hemoglobin_deoxy_16,299,39)
except:
    print "WARNING: failed to restore PmvMolecule named hemoglobin_deoxy in network masterNet"
    print_exc()
    hemoglobin_deoxy_16=None

try:
    ## saving node trypsynthase ##
    mol = masterNet.editor.vf.loadMoleculeIfNeeded("Data"+os.sep+"trypsynthase.pdb")
    assert mol
    from Pmv.VisionInterface.PmvNodes import PmvMolecule
    trypsynthase_17 = PmvMolecule(molecule=masterNet.editor.vf.expandNodes("trypsynthase")[0], constrkw = {'molecule': 'masterNet.editor.vf.expandNodes("trypsynthase")[0]'}, name='trypsynthase', library=pmvlib)
    masterNet.addNode(trypsynthase_17,287,84)
except:
    print "WARNING: failed to restore PmvMolecule named trypsynthase in network masterNet"
    print_exc()
    trypsynthase_17=None

try:
    ## saving node atcase ##
    mol = masterNet.editor.vf.loadMoleculeIfNeeded("Data"+os.sep+"atcase.pdb")
    assert mol
    from Pmv.VisionInterface.PmvNodes import PmvMolecule
    atcase_18 = PmvMolecule(molecule=masterNet.editor.vf.expandNodes("atcase")[0], constrkw = {'molecule': 'masterNet.editor.vf.expandNodes("atcase")[0]'}, name='atcase', library=pmvlib)
    masterNet.addNode(atcase_18,230,8)
except:
    print "WARNING: failed to restore PmvMolecule named atcase in network masterNet"
    print_exc()
    atcase_18=None

masterNet.freeze()

## saving connections for network hemoglobin ##
if Select_MolFrag_0 is not None and Extract_Atom_Property_1 is not None:
    try:
        masterNet.connectNodes(
            Select_MolFrag_0, Extract_Atom_Property_1, "nodes", "atoms", blocking=True)
    except:
        print "WARNING: failed to restore connection between Select_MolFrag_0 and Extract_Atom_Property_1 in network masterNet"
if Dial_5 is not None and UT_BlurSpheres_1__4 is not None:
    try:
        masterNet.connectNodes(
            Dial_5, UT_BlurSpheres_1__4, "value", "radius", blocking=True)
    except:
        print "WARNING: failed to restore connection between Dial_5 and UT_BlurSpheres_1__4 in network masterNet"
if Extract_Atom_Property_1 is not None and UT_BlurSpheres_1__4 is not None:
    try:
        masterNet.connectNodes(
            Extract_Atom_Property_1, UT_BlurSpheres_1__4, "propertyValues", "coords", blocking=True)
    except:
        print "WARNING: failed to restore connection between Extract_Atom_Property_1 and UT_BlurSpheres_1__4 in network masterNet"
if UT_BlurSpheres_1__4 is not None and UT_Isocontour_6 is not None:
    try:
        masterNet.connectNodes(
            UT_BlurSpheres_1__4, UT_Isocontour_6, "maskGrid", "grid3D", blocking=True)
    except:
        print "WARNING: failed to restore connection between UT_BlurSpheres_1__4 and UT_Isocontour_6 in network masterNet"
if UT_Isocontour_6 is not None and heme2DChain_7 is not None:
    try:
        masterNet.connectNodes(
            UT_Isocontour_6, heme2DChain_7, "normals", "vnormals", blocking=True)
    except:
        print "WARNING: failed to restore connection between UT_Isocontour_6 and heme2DChain_7 in network masterNet"
if UT_Isocontour_6 is not None and heme2DChain_7 is not None:
    try:
        masterNet.connectNodes(
            UT_Isocontour_6, heme2DChain_7, "indices", "indices", blocking=True)
    except:
        print "WARNING: failed to restore connection between UT_Isocontour_6 and heme2DChain_7 in network masterNet"
if UT_Isocontour_6 is not None and heme2DChain_7 is not None:
    try:
        masterNet.connectNodes(
            UT_Isocontour_6, heme2DChain_7, "coords", "coords", blocking=True)
    except:
        print "WARNING: failed to restore connection between UT_Isocontour_6 and heme2DChain_7 in network masterNet"
if Select_MolFrag_9 is not None and iterate_10 is not None:
    try:
        masterNet.connectNodes(
            Select_MolFrag_9, iterate_10, "nodes", "listToLoopOver", blocking=True)
    except:
        print "WARNING: failed to restore connection between Select_MolFrag_9 and iterate_10 in network masterNet"
if iterate_10 is not None and Get_id_11 is not None:
    try:
        masterNet.connectNodes(
            iterate_10, Get_id_11, "oneItem", "objects", blocking=True)
    except:
        print "WARNING: failed to restore connection between iterate_10 and Get_id_11 in network masterNet"
if Get_id_11 is not None and Index_13 is not None:
    try:
        masterNet.connectNodes(
            Get_id_11, Index_13, "attrs", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between Get_id_11 and Index_13 in network masterNet"
if Index_13 is not None and Filename_12 is not None:
    try:
        masterNet.connectNodes(
            Index_13, Filename_12, "data", "number", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_13 and Filename_12 in network masterNet"
if Filename_12 is not None and heme2DChain_7 is not None:
    try:
        masterNet.connectNodes(
            Filename_12, heme2DChain_7, "filename", "name", blocking=True)
    except:
        print "WARNING: failed to restore connection between Filename_12 and heme2DChain_7 in network masterNet"
if heme2DChain_7 is not None and RemoveDupVert_14 is not None:
    try:
        masterNet.connectNodes(
            heme2DChain_7, RemoveDupVert_14, "indexedPolygons", "geom", blocking=True)
    except:
        print "WARNING: failed to restore connection between heme2DChain_7 and RemoveDupVert_14 in network masterNet"
if RemoveDupVert_14 is not None and QSlim_15 is not None:
    try:
        masterNet.connectNodes(
            RemoveDupVert_14, QSlim_15, "geom", "geometry", blocking=True)
    except:
        print "WARNING: failed to restore connection between RemoveDupVert_14 and QSlim_15 in network masterNet"
if QSlim_15 is not None and Pmv_Viewer_8 is not None:
    try:
        masterNet.connectNodes(
            QSlim_15, Pmv_Viewer_8, "geometry", "geometries", blocking=True)
    except:
        print "WARNING: failed to restore connection between QSlim_15 and Pmv_Viewer_8 in network masterNet"
if hemoglobin_deoxy_16 is not None and Select_MolFrag_9 is not None:
    try:
        masterNet.connectNodes(
            hemoglobin_deoxy_16, Select_MolFrag_9, "Molecule", "nodes", blocking=True)
    except:
        print "WARNING: failed to restore connection between hemoglobin_deoxy_16 and Select_MolFrag_9 in network masterNet"
if iterate_10 is not None and Select_MolFrag_0 is not None:
    try:
        masterNet.connectNodes(
            iterate_10, Select_MolFrag_0, "oneItem", "nodes", blocking=True)
    except:
        print "WARNING: failed to restore connection between iterate_10 and Select_MolFrag_0 in network masterNet"
masterNet.unfreeze()
try:
    masterNet.run()
except:
    pass
##
## Saving State for objects in Viewer
##

## Object root|pickSpheres
## Object root|misc
## Object root|CoarseAPBSbox
## Object root|FineAPBSbox
## Object root|hemoglobin_deoxy
## Object root|trypsynthase
## Object root|atcase
## Object root|heme2AChain
state = {'blendFunctions': ('GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA'), 'stippleLines': False, 'replace': False, 'scissorAspectRatio': 1.0, 'immediateRendering': False, 'shading': 'smooth', 'pivot': [0.0, 0.0, 0.0], 'translation': [0.0, 0.0, 0.0], 'scissorH': 200, 'frontPolyMode': 'fill', 'inheritFrontPolyMode': True, 'inheritStippleLines': True, 'inheritShading': True, 'instanceMatrices': [[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scissorX': 0, 'scissorY': 0, 'listed': True, 'inheritPointWidth': True, 'pickable': 1, 'pointWidth': 3, 'scissorW': 200, 'culling': 'back', 'stipplePolygons': False, 'pickableVertices': False, 'inheritMaterial': True, 'depthMask': 1, 'scale': [1.0, 1.0, 1.0], 'lighting': True, 'inheritCulling': True, 'inheritStipplePolygons': True, 'rotation': [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0], 'transparent': False, 'outline': False, 'name': 'heme2AChain', 'backPolyMode': 'fill', 'visible': True, 'inheritBackPolyMode': True, 'scissor': 0, 'protected': False, 'inheritLineWidth': True, 'lineWidth': 1, 'inheritXform': 1}
obj = Pmv_Viewer_8.vi.FindObjectByName('root|heme2AChain')
if obj:
    apply(obj.Set, (), state)

## Material for heme2AChain
if obj:
    pass  ## needed in case there no modif
## End Materials for heme2AChain

## Clipping Planes for heme2AChain
if obj:
    obj.clipP = []
    obj.clipPI = []
    pass  ## needed in case there no modif
## End Clipping Planes for heme2AChain

## Object root|heme2BChain
state = {'blendFunctions': ('GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA'), 'stippleLines': False, 'replace': False, 'scissorAspectRatio': 1.0, 'immediateRendering': False, 'shading': 'smooth', 'pivot': [0.0, 0.0, 0.0], 'translation': [0.0, 0.0, 0.0], 'scissorH': 200, 'frontPolyMode': 'fill', 'inheritFrontPolyMode': True, 'inheritStippleLines': True, 'inheritShading': True, 'instanceMatrices': [[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scissorX': 0, 'scissorY': 0, 'listed': True, 'inheritPointWidth': True, 'pickable': 1, 'pointWidth': 3, 'scissorW': 200, 'culling': 'back', 'stipplePolygons': False, 'pickableVertices': False, 'inheritMaterial': True, 'depthMask': 1, 'scale': [1.0, 1.0, 1.0], 'lighting': True, 'inheritCulling': True, 'inheritStipplePolygons': True, 'rotation': [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0], 'transparent': False, 'outline': False, 'name': 'heme2BChain', 'backPolyMode': 'fill', 'visible': True, 'inheritBackPolyMode': True, 'scissor': 0, 'protected': False, 'inheritLineWidth': True, 'lineWidth': 1, 'inheritXform': 1}
obj = Pmv_Viewer_8.vi.FindObjectByName('root|heme2BChain')
if obj:
    apply(obj.Set, (), state)

## Material for heme2BChain
if obj:
    pass  ## needed in case there no modif
## End Materials for heme2BChain

## Clipping Planes for heme2BChain
if obj:
    obj.clipP = []
    obj.clipPI = []
    pass  ## needed in case there no modif
## End Clipping Planes for heme2BChain

## Object root|heme2CChain
state = {'blendFunctions': ('GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA'), 'stippleLines': False, 'replace': False, 'scissorAspectRatio': 1.0, 'immediateRendering': False, 'shading': 'smooth', 'pivot': [0.0, 0.0, 0.0], 'translation': [0.0, 0.0, 0.0], 'scissorH': 200, 'frontPolyMode': 'fill', 'inheritFrontPolyMode': True, 'inheritStippleLines': True, 'inheritShading': True, 'instanceMatrices': [[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scissorX': 0, 'scissorY': 0, 'listed': True, 'inheritPointWidth': True, 'pickable': 1, 'pointWidth': 3, 'scissorW': 200, 'culling': 'back', 'stipplePolygons': False, 'pickableVertices': False, 'inheritMaterial': True, 'depthMask': 1, 'scale': [1.0, 1.0, 1.0], 'lighting': True, 'inheritCulling': True, 'inheritStipplePolygons': True, 'rotation': [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0], 'transparent': False, 'outline': False, 'name': 'heme2CChain', 'backPolyMode': 'fill', 'visible': True, 'inheritBackPolyMode': True, 'scissor': 0, 'protected': False, 'inheritLineWidth': True, 'lineWidth': 1, 'inheritXform': 1}
obj = Pmv_Viewer_8.vi.FindObjectByName('root|heme2CChain')
if obj:
    apply(obj.Set, (), state)

## Material for heme2CChain
if obj:
    pass  ## needed in case there no modif
## End Materials for heme2CChain

## Clipping Planes for heme2CChain
if obj:
    obj.clipP = []
    obj.clipPI = []
    pass  ## needed in case there no modif
## End Clipping Planes for heme2CChain

## Object root|heme2DChain
state = {'blendFunctions': ('GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA'), 'stippleLines': False, 'replace': False, 'scissorAspectRatio': 1.0, 'immediateRendering': False, 'shading': 'smooth', 'pivot': [0.0, 0.0, 0.0], 'translation': [0.0, 0.0, 0.0], 'scissorH': 200, 'frontPolyMode': 'fill', 'inheritFrontPolyMode': True, 'inheritStippleLines': True, 'inheritShading': True, 'instanceMatrices': [[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scissorX': 0, 'scissorY': 0, 'listed': True, 'inheritPointWidth': True, 'pickable': 1, 'pointWidth': 3, 'scissorW': 200, 'culling': 'back', 'stipplePolygons': False, 'pickableVertices': False, 'inheritMaterial': True, 'depthMask': 1, 'scale': [1.0, 1.0, 1.0], 'lighting': True, 'inheritCulling': True, 'inheritStipplePolygons': True, 'rotation': [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0], 'transparent': False, 'outline': False, 'name': 'heme2DChain', 'backPolyMode': 'fill', 'visible': True, 'inheritBackPolyMode': True, 'scissor': 0, 'protected': False, 'inheritLineWidth': True, 'lineWidth': 1, 'inheritXform': 1}
obj = Pmv_Viewer_8.vi.FindObjectByName('root|heme2DChain')
if obj:
    apply(obj.Set, (), state)

## Material for heme2DChain
if obj:
    pass  ## needed in case there no modif
## End Materials for heme2DChain

## Clipping Planes for heme2DChain
if obj:
    obj.clipP = []
    obj.clipPI = []
    pass  ## needed in case there no modif
## End Clipping Planes for heme2DChain

## Object root|misc|pickSpheresGeom
## Object root|misc|addBondsGeom
## Object root|misc|measure_geoms
## Object root|misc|edit_geoms
## Object root|hemoglobin_deoxy|selection
## Object root|hemoglobin_deoxy|lines
## Object root|hemoglobin_deoxy|AtomLabels
## Object root|hemoglobin_deoxy|ResidueLabels
## Object root|hemoglobin_deoxy|ChainLabels
## Object root|hemoglobin_deoxy|ProteinLabels
## Object root|hemoglobin_deoxy|sticks
## Object root|hemoglobin_deoxy|balls
## Object root|hemoglobin_deoxy|cpk
## Object root|hemoglobin_deoxy|CAsticks
## Object root|hemoglobin_deoxy|CAballs
## Object root|trypsynthase|selection
## Object root|trypsynthase|lines
## Object root|trypsynthase|AtomLabels
## Object root|trypsynthase|ResidueLabels
## Object root|trypsynthase|ChainLabels
## Object root|trypsynthase|ProteinLabels
## Object root|trypsynthase|sticks
## Object root|trypsynthase|balls
## Object root|trypsynthase|cpk
## Object root|trypsynthase|CAsticks
## Object root|trypsynthase|CAballs
## Object root|atcase|selection
## Object root|atcase|lines
## Object root|atcase|AtomLabels
## Object root|atcase|ResidueLabels
## Object root|atcase|ChainLabels
## Object root|atcase|ProteinLabels
## Object root|atcase|sticks
## Object root|atcase|balls
## Object root|atcase|cpk
## Object root|atcase|CAsticks
## Object root|atcase|CAballs
## Object root|misc|pickSpheresGeom|pickSpheres
## Object root|misc|addBondsGeom|addBondsSpheres
## Object root|misc|measure_geoms|measureDistGeom
## Object root|misc|measure_geoms|measureAngleGeom
## Object root|misc|measure_geoms|measureTorsionGeom
## Object root|misc|edit_geoms|editAtomTypeSphere
## Object root|misc|edit_geoms|editAtomChargeSphere
## Object root|hemoglobin_deoxy|lines|bonded
## Object root|hemoglobin_deoxy|lines|nobnds
## Object root|hemoglobin_deoxy|lines|bondorder
## Object root|trypsynthase|lines|bonded
## Object root|trypsynthase|lines|nobnds
## Object root|trypsynthase|lines|bondorder
## Object root|atcase|lines|bonded
## Object root|atcase|lines|nobnds
## Object root|atcase|lines|bondorder
## Object root|misc|measure_geoms|measureDistGeom|distLine
## Object root|misc|measure_geoms|measureDistGeom|distLabel
## Object root|misc|measure_geoms|measureDistGeom|distSpheres
## Object root|misc|measure_geoms|measureAngleGeom|angleLine
## Object root|misc|measure_geoms|measureAngleGeom|angleLabel
## Object root|misc|measure_geoms|measureAngleGeom|angleSpheres
## Object root|misc|measure_geoms|measureAngleGeom|angles
state = {'blendFunctions': ('GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA'), 'stippleLines': False, 'replace': True, 'scissorAspectRatio': 1.0, 'immediateRendering': False, 'shading': 'smooth', 'pivot': [0.0, 0.0, 0.0], 'translation': [0.0, 0.0, 0.0], 'scissorH': 200, 'frontPolyMode': 'fill', 'inheritFrontPolyMode': 0, 'inheritStippleLines': True, 'inheritShading': True, 'instanceMatrices': [[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scissorX': 0, 'scissorY': 0, 'listed': True, 'inheritPointWidth': True, 'pickable': 1, 'pointWidth': 3, 'scissorW': 200, 'culling': 'none', 'stipplePolygons': 1, 'pickableVertices': False, 'inheritMaterial': 0, 'depthMask': 1, 'scale': [1.0, 1.0, 1.0], 'lighting': False, 'inheritCulling': False, 'inheritStipplePolygons': 0, 'rotation': [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0], 'transparent': 0, 'outline': False, 'name': 'angles', 'backPolyMode': 'fill', 'visible': True, 'inheritBackPolyMode': False, 'scissor': 0, 'protected': False, 'inheritLineWidth': True, 'lineWidth': 1, 'inheritXform': 1}
obj = Pmv_Viewer_8.vi.FindObjectByName('root|misc|measure_geoms|measureAngleGeom|angles')
if obj:
    apply(obj.Set, (), state)

## Material for angles
if obj:
    from opengltk.OpenGL import GL
    state = {'opacity': [1.0], 'binding': [10.0, 10.0, 10.0, 10.0, 10.0, 10.0], 'emission': [[0.0, 0.0, 0.0, 1.0]], 'shininess': [50.0], 'specular': [[0.89999997615814209, 0.89999997615814209, 0.89999997615814209, 1.0]], 'ambient': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 1.0]], 'diffuse': [[1.0, 0.5, 0.0, 1.0]]}
    apply(obj.materials[GL.GL_FRONT].Set, (), state)

    pass  ## needed in case there no modif
## End Materials for angles

## Clipping Planes for angles
if obj:
    obj.clipP = []
    obj.clipPI = []
    pass  ## needed in case there no modif
## End Clipping Planes for angles

## Object root|misc|measure_geoms|measureTorsionGeom|torsionLine
## Object root|misc|measure_geoms|measureTorsionGeom|torsionLabel
## Object root|misc|measure_geoms|measureTorsionGeom|torsionSpheres
## End Object root|misc|measure_geoms|measureTorsionGeom|torsionSpheres
