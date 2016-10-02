'''
Created on Jul 12, 2016

@author: ad
'''
import unittest
import os 
import pprint
from django.conf import settings 
from size_estimation_new import ElementSizeCalculator, FileSizeEstimator, SequenceSizeEstimator
import converter_util as cu 

def withMethodName(func):
    def inner(*args, **kwargs):
        print 'Running %s ...' % func.__name__
        func(*args, **kwargs)
    return inner
    
class Test_ElementSizeCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.f5 = os.path.join(settings.BASE_DIR, 'seql_converter', 
                            'st25parser', 'testData', 'file5.txt')
        cls.esc5 = ElementSizeCalculator(cls.f5)
        
        cls.f_WO2013041670 = os.path.join(settings.BASE_DIR, 'seql_converter', 
                            'st25parser', 'testData', 'WO2013041670.txt')
        cls.esc_WO2013041670 = ElementSizeCalculator(cls.f_WO2013041670)
        
        cls.f_WO2012_001613 = os.path.join(settings.BASE_DIR, 'seql_converter', 
                            'st25parser', 'testData', 'WO2012-001613-001.zip.txt')
        cls.esc_WO2012_001613 = ElementSizeCalculator(cls.f_WO2012_001613)
        
        f1004 = os.path.join(settings.BASE_DIR, 'seql_converter', 
                            'st25parser', 'testData', 'WO2012-001004-001.zip.txt')
        cls.esc_1004 = ElementSizeCalculator(f1004)
        
        f6550 = os.path.join(settings.BASE_DIR, 'seql_converter', 
                            'st25parser', 'testData', 'WO2012-006550-001.zip.txt')
        cls.esc_6550 = ElementSizeCalculator(f6550)
 
    @withMethodName
    def test_setRow_xmlRoot(self):
        act = [row for row in self.esc5.generalInformationRows if row[6] == 'xmlHeader'][0]
        
        self.assertEqual(0, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(0, act[2])
        self.assertEqual(0, act[3])
        self.assertEqual(len(cu.OTHER_ELEMENTS_ST26['xmlHeader']), act[4])
        self.assertEqual(len(cu.OTHER_ELEMENTS_ST26['xmlHeader']), act[5])
        self.assertEqual('xmlHeader', act[6])
        self.assertEqual('ST.26 specific element', act[7])
    
    @withMethodName 
    def test_setRow_doctypeDeclaration(self):
        act = [row for row in self.esc5.generalInformationRows if row[6] == 'doctypeDeclaration'][0]
        
        self.assertEqual(0, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(0, act[2])
        self.assertEqual(0, act[3])
        self.assertEqual(len(cu.OTHER_ELEMENTS_ST26['doctypeDeclaration']), act[4])
        self.assertEqual(len(cu.OTHER_ELEMENTS_ST26['doctypeDeclaration']), act[5])
        self.assertEqual('doctypeDeclaration', act[6])
        self.assertEqual('ST.26 specific element', act[7])
    @withMethodName
    def test_setRow_styleSheetReference(self):
        act = [row for row in self.esc5.generalInformationRows if row[6] == 'styleSheetReference'][0]
        
        self.assertEqual(0, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(0, act[2])
        self.assertEqual(0, act[3])
        self.assertEqual(len(cu.OTHER_ELEMENTS_ST26['styleSheetReference']), act[4])
        self.assertEqual(len(cu.OTHER_ELEMENTS_ST26['styleSheetReference']), act[5])
        self.assertEqual('styleSheetReference', act[6])
        self.assertEqual('ST.26 specific element', act[7])
    @withMethodName     
    def test_setRow_header(self): 
        act = [row for row in self.esc5.generalInformationRows if row[6] == 'ST26SequenceListing'][0]
        
        self.assertEqual(0, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(45, act[2])
        self.assertEqual(16, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['ST26SequenceListing'], act[4])
        self.assertEqual(cu.TAG_LENGTH_ST26['ST26SequenceListing'], act[5])
        self.assertEqual('ST26SequenceListing', act[6])
        self.assertEqual('ST.25 seqlHeader discarded', act[7])
    @withMethodName    
    def test_setRow_dtdVersion(self): 
        act = [row for row in self.esc5.generalInformationRows if row[6] == 'dtdVersion'][0]

        self.assertEqual(0, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(0, act[2])
        self.assertEqual(3, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['dtdVersion'], act[4])
        self.assertEqual(3 + cu.TAG_LENGTH_ST26['dtdVersion'], act[5])
        self.assertEqual('dtdVersion', act[6])
        self.assertEqual('ST.26 specific element. Assumed format: d.d (for ex.: 1.3)', act[7])

    @withMethodName    
    def test_setRow_fileName(self): 
        act = [row for row in self.esc5.generalInformationRows if row[6] == 'fileName'][0]

        self.assertEqual(0, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(0, act[2])
        self.assertEqual(5, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['fileName'], act[4])
        self.assertEqual(5 + cu.TAG_LENGTH_ST26['fileName'], act[5])
        self.assertEqual('fileName', act[6])
        self.assertEqual('ST.25 file name used with extension xml', act[7])
           
    
#      TODO: test getRow_fileName   
    @withMethodName
    def test_setRow_softwareName(self): 
        act = [row for row in self.esc5.generalInformationRows if row[6] == 'softwareName'][0]
        
        self.assertEqual(0, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(0, act[2])
        self.assertEqual(10, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['softwareName'], act[4])
        self.assertEqual(10 + cu.TAG_LENGTH_ST26['softwareName'], act[5])
        self.assertEqual('softwareName', act[6])
        self.assertEqual('ST.26 specific element. Assumed it has 10 chars', act[7])
    @withMethodName
    def test_setRow_softwareVersion(self): 
        act = [row for row in self.esc5.generalInformationRows if row[6] == 'softwareVersion'][0]

        self.assertEqual(0, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(0, act[2])
        self.assertEqual(3, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['softwareVersion'], act[4])
        self.assertEqual(3 + cu.TAG_LENGTH_ST26['softwareVersion'], act[5])
        self.assertEqual('softwareVersion', act[6])
        self.assertEqual('ST.26 specific element. Assumed format: d.d (for ex.: 1.3)', act[7])
    @withMethodName
    def test_setRow_productionDate(self): 
        act = [row for row in self.esc5.generalInformationRows if row[6] == 'productionDate'][0]

        self.assertEqual(0, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(0, act[2])
        self.assertEqual(len('YYYY-MM-DD'), act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['productionDate'], act[4])
        self.assertEqual(len('YYYY-MM-DD') + cu.TAG_LENGTH_ST26['productionDate'], act[5])
        self.assertEqual('productionDate', act[6])
#         self.assertEqual('ST.26 specific element. Assumed format: d.d (for ex.: 1.3)', act[7])
    @withMethodName       
    def test_setRow_110(self):
        act = [row for row in self.esc5.generalInformationRows if row[0] == 110][0]
        self.assertEqual(110, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(39, act[2])
        self.assertEqual(26, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['ApplicantName'], act[4])
        self.assertEqual(26 + cu.TAG_LENGTH_ST26['ApplicantName'], act[5])
        self.assertEqual('ApplicantName', act[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act[7])
        
        act1 = [row for row in self.esc5.generalInformationRows if row[7] == 'ST.26 specific languageCode attribute for ApplicantName'][0]
        self.assertEqual(110, act1[0])
        self.assertEqual(0, act1[1])
        self.assertEqual(0, act1[2])
        self.assertEqual(len(cu.DEFAULT_CODE), act1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['languageCode'], act1[4])
        self.assertEqual(len(cu.DEFAULT_CODE) + cu.TAG_LENGTH_ST26['languageCode'], act1[5])
        self.assertEqual('languageCode', act1[6])
#         self.assertEqual(cu.BLANK_PLACEHOLDER, act1[7])
    @withMethodName
    def test_setRow_InventorName(self):
        act = [row for row in self.esc5.generalInformationRows if row[6] == 'InventorName']
        self.assertEqual([], act)
        
#         self.assertEqual(0, act[0])
#         self.assertEqual(0, act[1])
#         self.assertEqual(0, act[2])
#         self.assertEqual(0, act[3])
#         self.assertEqual(cu.TAG_LENGTH_ST26['InventorName'], act[4])
#         self.assertEqual(1+cu.TAG_LENGTH_ST26['InventorName'], act[5])
#         self.assertEqual('InventorName', act[6])
#         self.assertEqual(cu.BLANK_PLACEHOLDER, act[7])
        
        act1 = [row for row in self.esc5.generalInformationRows if row[7] == 'ST.26 specific languageCode attribute for InventorName']
        self.assertEqual([], act1)
#         self.assertEqual(0, act1[0])
#         self.assertEqual(0, act1[1])
#         self.assertEqual(0, act1[2])
#         self.assertEqual(len(cu.DEFAULT_CODE), act1[3])
#         self.assertEqual(cu.TAG_LENGTH_ST26['languageCode'], act1[4])
#         self.assertEqual(len(cu.DEFAULT_CODE) + cu.TAG_LENGTH_ST26['languageCode'], act1[5])
#         self.assertEqual('languageCode', act1[6])
    @withMethodName    
    def test_setRow_120(self):
        act = [row for row in self.esc5.generalInformationRows if row[0] == 120][0]
        self.assertEqual(120, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(98, act[2])
        self.assertEqual(78, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['InventionTitle'], act[4])
        self.assertEqual(78 + cu.TAG_LENGTH_ST26['InventionTitle'], act[5])
        self.assertEqual('InventionTitle', act[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act[7])
        
        act1 = [row for row in self.esc5.generalInformationRows if row[7] == 'ST.26 specific languageCode attribute for InventionTitle'][0]
        self.assertEqual(120, act1[0])
        self.assertEqual(0, act1[1])
        self.assertEqual(0, act1[2])
        self.assertEqual(len(cu.DEFAULT_CODE), act1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['languageCode'], act1[4])
        self.assertEqual(len(cu.DEFAULT_CODE) + cu.TAG_LENGTH_ST26['languageCode'], act1[5])
        self.assertEqual('languageCode', act1[6])
    @withMethodName    
    def test_setRow_130(self):
        act = [row for row in self.esc5.generalInformationRows if row[0] == 130][0]
        self.assertEqual(130, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(24, act[2])
        self.assertEqual(13, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['ApplicantFileReference'], act[4])
        self.assertEqual(13 + cu.TAG_LENGTH_ST26['ApplicantFileReference'], act[5])
        self.assertEqual('ApplicantFileReference', act[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act[7])
    @withMethodName 
    def test_setRow_ApplicationIdentification(self):
        actApplicationIdentification_1 = [row for row in self.esc5.generalInformationRows if row[6] == 'ApplicationIdentification']
        self.assertEqual([], actApplicationIdentification_1)
        
        act = [row for row in self.esc_WO2013041670.generalInformationRows if row[6] == 'ApplicationIdentification'][0]
        self.assertEqual(0, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(0, act[2])
        self.assertEqual(0, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['ApplicationIdentification'], act[4])
        self.assertEqual(cu.TAG_LENGTH_ST26['ApplicationIdentification'], act[5])
        self.assertEqual('ApplicationIdentification', act[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act[7])
    @withMethodName    
    def test_setRow_IPOfficeCode(self):
        actIPOfficeCode_1 = [row for row in self.esc5.generalInformationRows if row[6] == 'IPOfficeCode']
#         there is only 1 IPOfficeCode (the one from priority)
        self.assertEqual(1, len(actIPOfficeCode_1))
        
        act = [row for row in self.esc_WO2013041670.generalInformationRows if row[6] == 'IPOfficeCode'][0]
        self.assertEqual(0, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(0, act[2])
        self.assertEqual(0, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['IPOfficeCode'], act[4])
        self.assertEqual(2+cu.TAG_LENGTH_ST26['IPOfficeCode'], act[5])
        self.assertEqual('IPOfficeCode', act[6])
        self.assertEqual('Corresponding to 140. XX placeholder for the purpose of this study', act[7])
    
    @withMethodName    
    def test_setRow_140(self):
        act140_1 = [row for row in self.esc5.generalInformationRows if row[0] == 140]
#         print act140_1
        self.assertEqual([], act140_1)

        act = [row for row in self.esc_WO2013041670.generalInformationRows if row[0] == 140][0]
        self.assertEqual(140, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(28, act[2])
        self.assertEqual(19, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['ApplicationNumberText'], act[4])
        self.assertEqual(19 + cu.TAG_LENGTH_ST26['ApplicationNumberText'], act[5])
        self.assertEqual('ApplicationNumberText', act[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act[7])
    @withMethodName    
    def test_setRow_141(self):
        act141_1 = [row for row in self.esc5.generalInformationRows if row[0] == 141]
        self.assertEqual([], act141_1)
#         self.assertEqual(141, act141_1[0])
#         self.assertEqual(0, act141_1[1])
#         self.assertEqual(0, act141_1[2])
#         self.assertEqual(10, act141_1[3])
#         self.assertEqual(cu.TAG_LENGTH_ST26['FilingDate'], act141_1[4])
#         self.assertEqual(10 + cu.TAG_LENGTH_ST26['FilingDate'], act141_1[5])
#         self.assertEqual('FilingDate', act141_1[6])
#         self.assertEqual(cu.BLANK_PLACEHOLDER, act141_1[7])
        
        act = [row for row in self.esc_WO2013041670.generalInformationRows if row[0] == 141][0]
        self.assertEqual(141, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(23, act[2])
        self.assertEqual(10, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['FilingDate'], act[4])
        self.assertEqual(10 + cu.TAG_LENGTH_ST26['FilingDate'], act[5])
        self.assertEqual('FilingDate', act[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act[7])
    
    @withMethodName    
    def test_setRow_150(self):
        act150_1 = [row for row in self.esc5.generalInformationRows if row[0] == 150][0]
        
        self.assertEqual(150, act150_1[0])
        self.assertEqual(0, act150_1[1])
        self.assertEqual(43, act150_1[2])
        self.assertEqual(13, act150_1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['ApplicationNumberText'], act150_1[4])
        self.assertEqual(13 + cu.TAG_LENGTH_ST26['ApplicationNumberText'], act150_1[5])
        self.assertEqual('ApplicationNumberText', act150_1[6])
        self.assertEqual('only first ST.25 priority retained, if any', act150_1[7])
        
    def test_setRow_151(self):
        act151_1 = [row for row in self.esc5.generalInformationRows if row[0] == 151][0]
        
        self.assertEqual(151, act151_1[0])
        self.assertEqual(0, act151_1[1])
        self.assertEqual(0, act151_1[2])
        self.assertEqual(10, act151_1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['FilingDate'], act151_1[4])
        self.assertEqual(10 + cu.TAG_LENGTH_ST26['FilingDate'], act151_1[5])
        self.assertEqual('FilingDate', act151_1[6])
        self.assertTrue('chars of raw' in act151_1[7])
        
# TODO: test for prio missing    
    @withMethodName    
    def test_setRow_160(self):
        act = [row for row in self.esc5.generalInformationRows if row[0] == 160][0]
        self.assertEqual(160, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(17, act[2])
        self.assertEqual(2, act[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['SequenceTotalQuantity'], act[4])
        self.assertEqual(2 + cu.TAG_LENGTH_ST26['SequenceTotalQuantity'], act[5])
        self.assertEqual('SequenceTotalQuantity', act[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act[7])
    @withMethodName    
    def test_setRow_170(self):
        act = [row for row in self.esc5.generalInformationRows if row[0] == 170][0]
        self.assertEqual(170, act[0])
        self.assertEqual(0, act[1])
        self.assertEqual(31, act[2])
        self.assertEqual(20, act[3])
        self.assertEqual(0, act[4])
        self.assertEqual(0, act[5])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act[6])
        self.assertEqual('information discarded in ST.26', act[7])
    
    def getElementRowsForSequence(self, aCalculator, tag, seqId):
        return [row for row in aCalculator.sequenceRows if row[0] == tag and row[1] == unicode(seqId)]
    @withMethodName    
    def test_row210(self):
#         if self.esc5.sequenceRows:
        rows210 = [row for row in self.esc5.sequenceRows if row[0] == 210]
        self.assertEqual(40, len(rows210))
        
        act_seq1 = self.getElementRowsForSequence(self.esc5, 210, '1')[0]
        self.assertEqual(210, act_seq1[0])
        self.assertEqual('1', act_seq1[1])
        self.assertEqual(10, act_seq1[2])
        self.assertEqual(1, act_seq1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['sequenceIDNumber'], act_seq1[4])
        self.assertEqual(1 + cu.TAG_LENGTH_ST26['sequenceIDNumber'], act_seq1[5])
        self.assertEqual('sequenceIDNumber', act_seq1[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act_seq1[7])
        
        act_seq40 = self.getElementRowsForSequence(self.esc5, 210, '40')[0]

        self.assertEqual(210, act_seq40[0])
        self.assertEqual('40', act_seq40[1])
        self.assertEqual(11, act_seq40[2])
        self.assertEqual(2, act_seq40[3])
    @withMethodName
    def test_SequenceData(self):
        act_seq1 = [row for row in self.esc5.sequenceRows if row[6] == 'SequenceData'][0]
        
        self.assertEqual(0, act_seq1[0])
        self.assertEqual('1', act_seq1[1])
        self.assertEqual(0, act_seq1[2])
        self.assertEqual(0, act_seq1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['SequenceData'], act_seq1[4])
        self.assertEqual(cu.TAG_LENGTH_ST26['SequenceData'], act_seq1[5])
        self.assertEqual('SequenceData', act_seq1[6])
        self.assertEqual('ST.26 specific element', act_seq1[7])
    @withMethodName    
    def test_INSDSeq(self):
        act_seq1 = [row for row in self.esc5.sequenceRows if row[6] == 'INSDSeq'][0]
        
        self.assertEqual(0, act_seq1[0])
        self.assertEqual('1', act_seq1[1])
        self.assertEqual(0, act_seq1[2])
        self.assertEqual(0, act_seq1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDSeq'], act_seq1[4])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDSeq'], act_seq1[5])
        self.assertEqual('INSDSeq', act_seq1[6])
        self.assertEqual('ST.26 specific element', act_seq1[7])
    @withMethodName    
    def test_row211(self):
        act_seq1 = self.getElementRowsForSequence(self.esc5, 211, '1')[0]
        
        self.assertEqual(211, act_seq1[0])
        self.assertEqual('1', act_seq1[1])
        self.assertEqual(12, act_seq1[2])
        self.assertEqual(3, act_seq1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDSeq_length'], act_seq1[4])
        self.assertEqual(3 + cu.TAG_LENGTH_ST26['INSDSeq_length'], act_seq1[5])
        self.assertEqual('INSDSeq_length', act_seq1[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act_seq1[7])
        
        act_seq40 = self.getElementRowsForSequence(self.esc5, 211, '40')[0]

        self.assertEqual(211, act_seq40[0])
        self.assertEqual('40', act_seq40[1])
        self.assertEqual(11, act_seq40[2])
        self.assertEqual(2, act_seq40[3])
    @withMethodName    
    def test_row212(self):
        act_seq1 = self.getElementRowsForSequence(self.esc5, 212, '1')[0]
        
        self.assertEqual(212, act_seq1[0])
        self.assertEqual('1', act_seq1[1])
        self.assertEqual(12, act_seq1[2])
        self.assertEqual(3, act_seq1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDSeq_moltype'], act_seq1[4])
        self.assertEqual(2 + cu.TAG_LENGTH_ST26['INSDSeq_moltype'], act_seq1[5])
        self.assertEqual('INSDSeq_moltype', act_seq1[6])
        self.assertEqual('PRT replaced by AA for proteins', act_seq1[7])
        
        act_seq40 = self.getElementRowsForSequence(self.esc5, 212, '40')[0]

        self.assertEqual(212, act_seq40[0])
        self.assertEqual('40', act_seq40[1])
        self.assertEqual(12, act_seq40[2])
        self.assertEqual(3, act_seq40[3])
        
        act_seq10 = self.getElementRowsForSequence(self.esc_WO2013041670, 212, '10')[0]
        self.assertEqual(212, act_seq10[0])
        self.assertEqual('10', act_seq10[1])
        self.assertEqual(12, act_seq10[2])
        self.assertEqual(3, act_seq10[3])
        self.assertEqual(3 + cu.TAG_LENGTH_ST26['INSDSeq_moltype'], act_seq10[5])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act_seq10[7])
    @withMethodName
    def test_INSDSeq_division(self):
        act_seq1 = [row for row in self.esc5.sequenceRows if row[6] == 'INSDSeq_division'][0]
        
        self.assertEqual(0, act_seq1[0])
        self.assertEqual('1', act_seq1[1])
        self.assertEqual(0, act_seq1[2])
        self.assertEqual(3, act_seq1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDSeq_division'], act_seq1[4])
        self.assertEqual(3 + cu.TAG_LENGTH_ST26['INSDSeq_division'], act_seq1[5])
        self.assertEqual('INSDSeq_division', act_seq1[6])
        self.assertEqual('ST.26 specific element', act_seq1[7])
    @withMethodName
    def test_INSDSeq_feature_table(self):
        act_seq1 = [row for row in self.esc5.sequenceRows if row[6] == 'INSDSeq_feature-table'][0]
        
        self.assertEqual(0, act_seq1[0])
        self.assertEqual('1', act_seq1[1])
        self.assertEqual(0, act_seq1[2])
        self.assertEqual(0, act_seq1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDSeq_feature-table'], act_seq1[4])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDSeq_feature-table'], act_seq1[5])
        self.assertEqual('INSDSeq_feature-table', act_seq1[6])
        self.assertEqual('ST.26 specific element', act_seq1[7])
    @withMethodName        
    def test_featureSource(self):
#         pprint.pprint(self.esc5.sequenceRows)
        
        act_INSDFeature = [row for row in self.esc5.sequenceRows 
                    if row[6] == 'INSDFeature' and 
                    row[7] == 'ST.26 mandatory feature source'][3]
        
        self.assertEqual(0, act_INSDFeature[0])
        self.assertEqual('4', act_INSDFeature[1])
        self.assertEqual(0, act_INSDFeature[2])
        self.assertEqual(0, act_INSDFeature[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDFeature'], act_INSDFeature[4])
        self.assertEqual(0 + cu.TAG_LENGTH_ST26['INSDFeature'], act_INSDFeature[5])
        self.assertEqual('INSDFeature', act_INSDFeature[6])
        self.assertEqual('ST.26 mandatory feature source', act_INSDFeature[7])
        
        act_INSDFeature_key = [row for row in self.esc5.sequenceRows 
                    if row[6] == 'INSDFeature_key' and 
                    row[7] == 'ST.26 mandatory feature source'][3]
        
        self.assertEqual(0, act_INSDFeature_key[0])
        self.assertEqual('4', act_INSDFeature_key[1])
        self.assertEqual(0, act_INSDFeature_key[2])
        self.assertEqual(0, act_INSDFeature_key[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDFeature_key'], act_INSDFeature_key[4])
        self.assertEqual(len('source') + cu.TAG_LENGTH_ST26['INSDFeature_key'], act_INSDFeature_key[5])
        self.assertEqual('INSDFeature_key', act_INSDFeature_key[6])
        self.assertEqual('ST.26 mandatory feature source', act_INSDFeature_key[7])
        
        act_INSDFeature_location = [row for row in self.esc5.sequenceRows 
                    if row[6] == 'INSDFeature_location' and 
                    row[7] == 'ST.26 mandatory feature source'][3]
        
        self.assertEqual(0, act_INSDFeature_location[0])
        self.assertEqual('4', act_INSDFeature_location[1])
        self.assertEqual(0, act_INSDFeature_location[2])
        self.assertEqual(0, act_INSDFeature_location[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDFeature_location'], act_INSDFeature_location[4])
        self.assertEqual(len('1..5') + cu.TAG_LENGTH_ST26['INSDFeature_location'], act_INSDFeature_location[5])
        self.assertEqual('INSDFeature_location', act_INSDFeature_location[6])
        self.assertEqual('ST.26 mandatory feature source', act_INSDFeature_location[7])
        
#         tests for qualifiers
        act_INSDFeature_quals = [row for row in self.esc5.sequenceRows 
                    if row[6] == 'INSDFeature_quals' and 
                    row[7] == 'ST.26 mandatory feature source'][0]
        
        self.assertEqual(0, act_INSDFeature_quals[0])
        self.assertEqual('1', act_INSDFeature_quals[1])
        self.assertEqual(0, act_INSDFeature_quals[2])
        self.assertEqual(0, act_INSDFeature_quals[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDFeature_quals'], act_INSDFeature_quals[4])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDFeature_quals'], act_INSDFeature_quals[5])
        self.assertEqual('INSDFeature_quals', act_INSDFeature_quals[6])
        self.assertEqual('ST.26 mandatory feature source', act_INSDFeature_quals[7])
        
        act_INSDQualifier_elements = [row for row in self.esc5.sequenceRows 
                    if row[6] == 'INSDQualifier' and 
                    'ST.26 mandatory ' in row[7]]
        act_INSDQualifier_organism = act_INSDQualifier_elements[0]
        act_INSDQualifier_mol_type = act_INSDQualifier_elements[1]
        
        self.assertEqual(0, act_INSDQualifier_organism[0])
        self.assertEqual('1', act_INSDQualifier_organism[1])
        self.assertEqual(0, act_INSDQualifier_organism[2])
        self.assertEqual(0, act_INSDQualifier_organism[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDQualifier'], act_INSDQualifier_organism[4])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDQualifier'], act_INSDQualifier_organism[5])
        self.assertEqual('INSDQualifier', act_INSDQualifier_organism[6])
        self.assertEqual('ST.26 mandatory qualifier organism', act_INSDQualifier_organism[7])
        
        self.assertEqual('INSDQualifier', act_INSDQualifier_mol_type[6])
        self.assertEqual('ST.26 mandatory qualifier mol_type', act_INSDQualifier_mol_type[7])
        
        act_INSDQualifier_name_elements = [row for row in self.esc5.sequenceRows 
                    if row[6] == 'INSDQualifier_name' and 
                    'ST.26 mandatory ' in row[7]]
        act_INSDQualifier_name_organism = act_INSDQualifier_name_elements[0]
        act_INSDQualifier_name_mol_type = act_INSDQualifier_name_elements[1]
        
        self.assertEqual(0, act_INSDQualifier_name_organism[0])
        self.assertEqual('1', act_INSDQualifier_name_organism[1])
        self.assertEqual(0, act_INSDQualifier_name_organism[2])
        self.assertEqual(0, act_INSDQualifier_name_organism[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDQualifier_name'], act_INSDQualifier_name_organism[4])
        self.assertEqual(len('organism') + cu.TAG_LENGTH_ST26['INSDQualifier_name'], act_INSDQualifier_name_organism[5])
        self.assertEqual('INSDQualifier_name', act_INSDQualifier_name_organism[6])
        self.assertEqual('ST.26 mandatory qualifier organism', act_INSDQualifier_name_organism[7])
        
        self.assertEqual('INSDQualifier_name', act_INSDQualifier_name_mol_type[6])
        self.assertEqual('ST.26 mandatory qualifier mol_type', act_INSDQualifier_name_mol_type[7])
        
        act_INSDQualifier_value_elements = [row for row in self.esc5.sequenceRows 
                    if row[6] == 'INSDQualifier_value' and 
                    'ST.26 mandatory ' in row[7]]
        act_INSDQualifier_value_organism = act_INSDQualifier_value_elements[0]
        act_INSDQualifier_value_mol_type = act_INSDQualifier_value_elements[1]
        
        self.assertEqual(213, act_INSDQualifier_value_organism[0])
        self.assertEqual('1', act_INSDQualifier_value_organism[1])
        self.assertEqual(23, act_INSDQualifier_value_organism[2])
        self.assertEqual(12, act_INSDQualifier_value_organism[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDQualifier_value'], act_INSDQualifier_value_organism[4])
        self.assertEqual(len('Homo sapiens') + cu.TAG_LENGTH_ST26['INSDQualifier_value'], act_INSDQualifier_value_organism[5])
        self.assertEqual('INSDQualifier_value', act_INSDQualifier_value_organism[6])
        self.assertEqual('ST.26 mandatory qualifier organism', act_INSDQualifier_value_organism[7])
        
        self.assertEqual(0, act_INSDQualifier_value_mol_type[0])
        self.assertEqual('INSDQualifier_value', act_INSDQualifier_value_mol_type[6])
        self.assertEqual('ST.26 mandatory qualifier mol_type', act_INSDQualifier_value_mol_type[7])
        
        
        act_INSDQualifier_value_organism40 = act_INSDQualifier_value_elements[78]
        self.assertEqual(213, act_INSDQualifier_value_organism40[0])
        
        self.assertEqual('40', act_INSDQualifier_value_organism40[1])
        self.assertEqual(35, act_INSDQualifier_value_organism40[2])
        self.assertEqual(24, act_INSDQualifier_value_organism40[3])
    @withMethodName    
    def test_row220(self):
        rows220_1 = self.getElementRowsForSequence(self.esc5, 220, '1')
        self.assertEqual([], rows220_1)
        
        rows220_4 = self.getElementRowsForSequence(self.esc5, 220, '4')
        self.assertEqual(5, len(rows220_4))
        
        act_seq4_0 = rows220_4[0]
         
        self.assertEqual(220, act_seq4_0[0])
        self.assertEqual('4', act_seq4_0[1])
        self.assertEqual(7, act_seq4_0[2])
        self.assertEqual(0, act_seq4_0[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDFeature'], act_seq4_0[4])
        self.assertEqual(0 + cu.TAG_LENGTH_ST26['INSDFeature'], act_seq4_0[5])
        self.assertEqual('INSDFeature', act_seq4_0[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act_seq4_0[7])
        
        act_seq4_5 = rows220_4[4]
        
        self.assertEqual(220, act_seq4_5[0])
        self.assertEqual('4', act_seq4_5[1])
        self.assertEqual(7, act_seq4_5[2])
        self.assertEqual(0, act_seq4_5[3])
    @withMethodName    
    def test_row221(self):
        rows221_1 = self.getElementRowsForSequence(self.esc5, 221, '1')
        self.assertEqual([], rows221_1)
        
        rows221_4 = self.getElementRowsForSequence(self.esc5, 221, '4')
        self.assertEqual(5, len(rows221_4))
        
        act_seq4_0 = rows221_4[0]
          
        self.assertEqual(221, act_seq4_0[0])
        self.assertEqual('4', act_seq4_0[1])
        self.assertEqual(21, act_seq4_0[2])
        self.assertEqual(12, act_seq4_0[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDFeature_key'], act_seq4_0[4])
        self.assertEqual(12 + cu.TAG_LENGTH_ST26['INSDFeature_key'], act_seq4_0[5])
        self.assertEqual('INSDFeature_key', act_seq4_0[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act_seq4_0[7])
         
        act_seq4_5 = rows221_4[4]
         
        self.assertEqual(221, act_seq4_5[0])
        self.assertEqual('4', act_seq4_5[1])
        self.assertEqual(21, act_seq4_5[2])
        self.assertEqual(12, act_seq4_5[3])
    @withMethodName    
    def test_row222(self):
        rows222_1 = self.getElementRowsForSequence(self.esc5, 222, '1')
        self.assertEqual([], rows222_1)
        
        rows222_4 = self.getElementRowsForSequence(self.esc5, 222, '4')
        self.assertEqual(5, len(rows222_4))
        
        act_seq4_0 = rows222_4[0]
          
        self.assertEqual(222, act_seq4_0[0])
        self.assertEqual('4', act_seq4_0[1])
        self.assertEqual(17, act_seq4_0[2])
        self.assertEqual(8, act_seq4_0[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDFeature_location'], act_seq4_0[4])
        self.assertEqual(8 + cu.TAG_LENGTH_ST26['INSDFeature_location'], act_seq4_0[5])
        self.assertEqual('INSDFeature_location', act_seq4_0[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act_seq4_0[7])
         
        act_seq4_5 = rows222_4[4]
         
        self.assertEqual(222, act_seq4_5[0])
        self.assertEqual('4', act_seq4_5[1])
        self.assertEqual(17, act_seq4_5[2])
        self.assertEqual(8, act_seq4_5[3])
    @withMethodName    
    def test_row223(self):
#         count the number of rows corresponding to qualifiers others than org and molt
        rows223_1 = self.getElementRowsForSequence(self.esc5, 223, '1')
        self.assertEqual([], rows223_1)
         
        rows223_4 = self.getElementRowsForSequence(self.esc5, 223, '4')
        self.assertEqual(6, len(rows223_4))
         
        act_seq4_0 = rows223_4[0]
          
        self.assertEqual(223, act_seq4_0[0])
        self.assertEqual('4', act_seq4_0[1])
        self.assertEqual(28, act_seq4_0[2])
        self.assertEqual(15, act_seq4_0[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDQualifier_value'], act_seq4_0[4])
        self.assertEqual(15 + cu.TAG_LENGTH_ST26['INSDQualifier_value'], act_seq4_0[5])
        self.assertEqual('INSDQualifier_value', act_seq4_0[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act_seq4_0[7])
          
        act_seq4_5 = rows223_4[5]
          
        self.assertEqual(223, act_seq4_5[0])
        self.assertEqual('4', act_seq4_5[1])
        self.assertEqual(31, act_seq4_5[2])
        self.assertEqual(20, act_seq4_5[3])
         
        rows223_39 = self.getElementRowsForSequence(self.esc5, 223, '39')
        self.assertEqual(1, len(rows223_39))
         
        act_seq39_0 = rows223_39[0]
          
        self.assertEqual(223, act_seq39_0[0])
        self.assertEqual('39', act_seq39_0[1])
        self.assertEqual(66, act_seq39_0[2])
        self.assertEqual(55, act_seq39_0[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDQualifier_value'], act_seq39_0[4])
        self.assertEqual(55 + cu.TAG_LENGTH_ST26['INSDQualifier_value'], act_seq39_0[5])
        self.assertEqual('INSDQualifier_value', act_seq39_0[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act_seq39_0[7])
    @withMethodName
    def test_rowTranslationQualifier(self):
        
        qualifierRows_seq1 = [row for row in self.esc_1004.sequenceRows 
                    if row[1] == '1' and row[6] == 'INSDQualifier_value']
        act_seq1 = qualifierRows_seq1[2]
        
        self.assertEqual(400, act_seq1[0])
        self.assertEqual('1', act_seq1[1])
        self.assertEqual(0, act_seq1[2])
        self.assertEqual(900, act_seq1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDQualifier_value'], act_seq1[4])
        self.assertEqual(300 + cu.TAG_LENGTH_ST26['INSDQualifier_value'], act_seq1[5])
        self.assertEqual('INSDQualifier_value', act_seq1[6])
        self.assertEqual('3-to-1 letter code', act_seq1[7])
        
        qualifierRows_seq7 = [row for row in self.esc_1004.sequenceRows 
                    if row[1] == '7' and row[6] == 'INSDQualifier_value']
        translation_qual_seq7_first = qualifierRows_seq7[3]
        translation_qual_seq7_second = qualifierRows_seq7[4]
        
        self.assertEqual(400, translation_qual_seq7_first[0])
        self.assertEqual('7', translation_qual_seq7_first[1])
        self.assertEqual(0, translation_qual_seq7_first[2])
        self.assertEqual(84, translation_qual_seq7_first[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDQualifier_value'], translation_qual_seq7_first[4])
        self.assertEqual(28 + cu.TAG_LENGTH_ST26['INSDQualifier_value'], translation_qual_seq7_first[5])
        self.assertEqual('INSDQualifier_value', translation_qual_seq7_first[6])
        self.assertEqual('3-to-1 letter code', translation_qual_seq7_first[7])
        
        self.assertEqual(138, translation_qual_seq7_second[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDQualifier_value'], translation_qual_seq7_second[4])
        self.assertEqual(46 + cu.TAG_LENGTH_ST26['INSDQualifier_value'], translation_qual_seq7_second[5])
    @withMethodName     
    def test_row400(self):
        act_seq1 = self.getElementRowsForSequence(self.esc5, 400, '1')[0]
        
        self.assertEqual(400, act_seq1[0])
        self.assertEqual('1', act_seq1[1])
        self.assertEqual(6102 + 190, act_seq1[2])
        self.assertEqual(738*3, act_seq1[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDSeq_sequence'], act_seq1[4])
        self.assertEqual(738 + cu.TAG_LENGTH_ST26['INSDSeq_sequence'], act_seq1[5])
        self.assertEqual('INSDSeq_sequence', act_seq1[6])
        self.assertEqual('3-to-1 letter code', act_seq1[7])
        
        act_seq10 = self.getElementRowsForSequence(self.esc_WO2013041670, 400, '10')[0]
        
        self.assertEqual(400, act_seq10[0])
        self.assertEqual('10', act_seq10[1])
        self.assertEqual(91, act_seq10[2])
        self.assertEqual(30, act_seq10[3])
        self.assertEqual(cu.TAG_LENGTH_ST26['INSDSeq_sequence'], act_seq10[4])
        self.assertEqual(30 + cu.TAG_LENGTH_ST26['INSDSeq_sequence'], act_seq10[5])
        self.assertEqual('INSDSeq_sequence', act_seq10[6])
        self.assertEqual(cu.BLANK_PLACEHOLDER, act_seq10[7])
   
# class Test_FileSizeEstimator(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.f5 = os.path.join(settings.BASE_DIR, 'seql_converter', 
#                             'st25parser', 'testData', 'file5.txt')
#         cls.fse5 = FileSizeEstimator(cls.f5)
#         f1004 = os.path.join(settings.BASE_DIR, 'seql_converter', 
#                             'st25parser', 'testData', 'WO2012-001004-001.zip.txt')
#         cls.fse_1004 = FileSizeEstimator(f1004)
#     
#     def test_init(self):
#         self.assertEqual(len(cu.OTHER_ELEMENTS_ST26['xmlHeader']), self.fse5.xmlHeaderLength)
#         self.assertEqual(38, self.fse_1004.xmlHeaderLength)
#         self.assertEqual(118, self.fse_1004.doctypeDeclaration)
#         self.assertEqual(60, self.fse_1004.styleSheetReference)
# #       can't run this test bc productionDate is not formatted as yyyy-mm-dd
# #         self.assertEqual(174, self.fse_1004.rootLength)
#         self.assertEqual(0, self.fse_1004.applicationIdentificationLength)
#         self.assertEqual(59, self.fse_1004.applicantFileReferenceLength)
# #       can't run this test bc filingDate is not formatted as yyyy-mm-dd        
# #         self.assertEqual(, self.fse_1004.earliestPriorityApplicationIdentificationLength)
#         self.assertEqual(97, self.fse_1004.applicantNameLength)
#         self.assertEqual(89, self.fse_1004.applicantNameLatinLength)
#         self.assertEqual(48, self.fse_1004.inventorNameLength)
#         self.assertEqual(40, self.fse_1004.inventorNameLatinLength)
#         self.assertEqual(97, self.fse_1004.inventionTitleLength)
#         self.assertEqual(49, self.fse_1004.sequenceTotalQuantityLength)
#         
#         sequences1004 = [s for s in self.fse_1004.seql.generateSequence()]
#         print sequences1004
#         sse1 = SequenceSizeEstimator(sequences1004[0])
#         self.assertEqual(69, sse1.sequenceDataLength)
#         self.assertEqual(36, sse1.INSDSeq_lengthLength)
#         self.assertEqual(38, sse1.INSDSeq_moltypeLength)
#         self.assertEqual(40, sse1.INSDSeq_divisionLength)
#         self.assertEqual(47, sse1.INSDSeq_feature_tableLength)
# 
#         fse1_0 = sse1.featureSizeEstimators[0]
#         self.assertEqual(27, fse1_0['INSDFeatureLength'])
#         self.assertEqual(41, fse1_0['INSDFeature_keyLength'])
#         self.assertEqual(51, fse1_0['INSDFeature_locationLength'])
#         self.assertEqual(39, fse1_0['INSDFeature_qualsLength'])
#         
#         q0_0 = fse1_0['qualifiers'][0]
#         self.assertEqual(31, q0_0['INSDQualifierLength'])
#         self.assertEqual(49, q0_0['INSDQualifier_nameLength'])
#         self.assertEqual(59, q0_0['INSDQualifier_valueLength'])
#         
#         q0_1 = fse1_0['qualifiers'][1]
#         self.assertEqual(31, q0_1['INSDQualifierLength'])
#         self.assertEqual(49, q0_1['INSDQualifier_nameLength'])
#         self.assertEqual(54, q0_1['INSDQualifier_valueLength'])
# 
#         fse1_1 = sse1.featureSizeEstimators[1]
#         self.assertEqual(27, fse1_1['INSDFeatureLength'])
#         self.assertEqual(38, fse1_1['INSDFeature_keyLength'])
#         self.assertEqual(55, fse1_1['INSDFeature_locationLength'])
#         self.assertEqual(39, fse1_1['INSDFeature_qualsLength'])
#         
#         q1_0 = fse1_1['qualifiers'][0]
#         self.assertEqual(31, q1_0['INSDQualifierLength'])
#         self.assertEqual(52, q1_0['INSDQualifier_nameLength'])
#         self.assertEqual(343, q1_0['INSDQualifier_valueLength'])
#         
#         self.assertEqual(2186, sse1.sequenceEstimatedSize)
#         
#         sse2 = SequenceSizeEstimator(self.fse_1004.seql.sequences[1])
#         self.assertEqual(993, sse2.sequenceEstimatedSize)
#         
#         sse16 = SequenceSizeEstimator(self.fse_1004.seql.sequences[16])
#         self.assertEqual(862, sse16.sequenceEstimatedSize)
        
#         self.assertEqual(1221, self.fse_1004.sequenceListingEstimatedSize)
#         self.assertEqual(21974, self.fse_1004.sequencesEstimatedSize)

#         fp = r'/Users/ad/pyton/test/st26fileSize/out_ST26/WO2012-001004_ST26_clean.xml'
#         with open(fp, 'r') as f:
#             sep = '<SequenceData'
#             l = f.read().split(sep)
#             for t in l[1:]:
#                 currentIndex = l.index(t)
#                 print currentIndex
#                 currentSequenceSizeEstimator = self.fse_1004.sequenceSizeEstimators[currentIndex-1]
#                 
#                 reconstructedString =  sep + t 
#                 self.assertEqual(len(reconstructedString), currentSequenceSizeEstimator.sequenceEstimatedSize)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()