#########################################################################
#
# Date: Aug 2004  Authors: Daniel Stoffler
#
#       stoffler@scripps.edu
#
# Copyright: Daniel Stoffler, and TSRI
#
#########################################################################
import sys, os, unittest
from time import sleep
from Pmv.VisionInterface.PmvNodes import pmvlib, PmvNode

mv= None

###############################
## implement setUp and tearDown
###############################
class PmvNodeTests (unittest.TestCase):
    def setUp(self):
        global mv
        if mv is None:        
            from Pmv.moleculeViewer import MoleculeViewer
            mv = MoleculeViewer(customizer = './.empty', logMode = 'no',
                                withShell=False,verbose=False)
                                
            mv.browseCommands('fileCommands', package="Pmv", topCommand=0)
            mv.browseCommands('bondsCommands',package='Pmv', topCommand=0)

            mv.browseCommands('colorCommands',package='Pmv', topCommand=0)
            mv.browseCommands('deleteCommands',package='Pmv', topCommand=0)
            mv.browseCommands('displayCommands',
                   commands=['displaySticksAndBalls','undisplaySticksAndBalls',
                              'displayCPK', 'undisplayCPK',
                              'displayLines','undisplayLines',
                              'displayBackboneTrace','undisplayBackboneTrace',
                              'DisplayBoundGeom'
                              ], package='Pmv', topCommand=0)

            mv.setOnAddObjectCommands(['buildBondsByDistance','displayLines',
                                       'colorByAtomType'], topCommand=0)
            #mv.loadModule("interactiveCommands", 'Pmv')
            mv.loadCommand("visionCommands", "vision", "Pmv")
            # Don't want to trap exceptions and errors... the user pref is set to 1 by
            # default
            #mv.setUserPreference(('trapExceptions', '0'), log = 0)
            mv.setUserPreference(('warningMsgFormat', 'printed'), log = 0)
        self.mv = mv
        
    def tearDown(self):
        #self.mv.vision = None
        #self.mv.Exit(0)
        import gc
        gc.collect()
        del self.mv
        mv = None    
        import gc
        gc.collect()
    
    ##########################
    ## Helper methods
    ##########################
    
    def pause(self, sleepTime=0.1):
        mv.GUI.ROOT.update()
        sleep(sleepTime)
    
    
    ############################################################################
    ## Tests
    ############################################################################
    
    
    def test_01_OpenCloseVisionQuit(self):
        """test if we can show and hide the Visual Programming Environment, then
        quit Pmv (with Vision hidden)"""
        mv.vision.show()
        self.pause()
        mv.vision.hide()
        self.pause()
    
    
    def test_02_OpenCloseOpenVisionQuit(self):
        """test if we can show, hide and show again the Visual Programming
        Environment, then quit Pmv (with Vision shown)"""
        mv.vision.show()
        self.pause()
        mv.vision.hide()
        self.pause()
        mv.vision.show()
        self.pause()
    
    
    def test_03_PmvNode(self):
        """test the Pmv node"""
        mv.vision.show()
        masterNet = mv.vision.ed.currentNetwork
        node0 = PmvNode(vf=masterNet.editor.vf, constrkw = {'vf': 'masterNet.editor.vf'}, name='Pmv', library=pmvlib)
        masterNet.addNode(node0,111,52)
        self.pause()
        # This node runs upon adding to a network. Does it output the right stuff?
        data = node0.outputPorts[0].data
        assert data is not None, "Expected data, got %s"%data
        assert  data == mv, "Expected %s, got %s"%(
            mv, node0.outputPorts[0].data.__class__)
    
    
    def test_04_HemoglobinIteratingNetwork(self):
        """
    """
        # starts from here
        mv.vision.show()
        ed = mv.vision.ed
        ed.loadNetwork('Data'+os.sep+'hemoglobin-blobby_net.py')
        net = ed.currentNetwork
        pmvNode = net.getNodeByName('Pmv Viewer')[0]
        blob =pmvNode.vi.FindObjectByName('root|heme2BChain')
        assert len(blob.vertexSet.vertices) == 2010 , len(blob.vertexSet.vertices)
        ed.deleteNetwork(net)
        mv.vision.hide()
        
if __name__ == '__main__':
    unittest.main()    
