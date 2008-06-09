import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
process.load("EventFilter.CSCRawToDigi.cscFrontierCablingUnpck_cff")

process.load("EventFilter.CSCRawToDigi.cscUnpacker_cfi")

process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")

process.load("Geometry.CSCGeometry.cscGeometry_cfi")

process.load("CalibMuon.Configuration.CSC_FakeDBConditions_cff")

process.load("RecoLocalMuon.CSCRecHitD.cscRecHitD_cfi")

process.load("RecoLocalMuon.CSCSegment.cscSegments_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(101)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('dcache:/pnfs/cms/WAX/11/store/data/MTCC/pass1/3792/A/mtcc.00003792.A.testStorageManager_0.1.root')
)

process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")

process.Timing = cms.Service("Timing")

process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")

process.ana = cms.EDFilter("CSCEfficiency",
    runOnData = cms.untracked.bool(True),
    update = cms.untracked.bool(False),
    WorkInEndcap = cms.untracked.int32(1),
    ExtrapolateFromStation = cms.untracked.int32(2),
    rootFileName = cms.untracked.string('monHists.root'),
    ExtrapolateToRing = cms.untracked.int32(2),
    stripDigiTag = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
    wireDigiTag = cms.InputTag("muonCSCDigis","MuonCSCWireDigi"),
    ExtrapolateToStation = cms.untracked.int32(1),
    MuonCSCHits = cms.InputTag("mix","g4SimHitsMuonCSCHits")
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('data.root')
)

process.p = cms.Path(process.muonCSCDigis*process.csc2DRecHits*process.cscSegments*process.ana)
process.muonCSCDigis.isMTCCData = True
process.muonCSCDigis.UseExaminer = False
process.cscSegments.algo_type = 4


