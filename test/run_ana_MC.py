import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
process.load("CalibMuon.Configuration.CSC_FakeDBConditions_cff")

process.load("Geometry.MuonCommonData.muonEndcapIdealGeometryXML_cfi")

process.load("Geometry.CSCGeometry.cscGeometry_cfi")

process.load("MagneticField.Engine.volumeBasedMagneticField_cfi")

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.load("SimMuon.CSCDigitizer.muonCSCDigis_cfi")

import RecoLocalMuon.CSCRecHitD.cscRecHitD_cfi
process.csc2DRecHits = RecoLocalMuon.CSCRecHitD.cscRecHitD_cfi.csc2DRecHits.clone()
process.load("RecoLocalMuon.CSCSegment.cscSegments_cfi")

process.load("SimGeneral.MixingModule.mixNoPU_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(101)
)
process.source = cms.Source("PoolSource",
    debugFlag = cms.untracked.bool(False),
    debugVebosity = cms.untracked.uint32(10),
    fileNames = cms.untracked.vstring('file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_350_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_351_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_352_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_353_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_354_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_355_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_356_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_357_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_358_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_359_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_360_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_361_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_362_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_363_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_364_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_365_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_366_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_367_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_368_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_369_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_370_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_371_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_372_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_373_probev2.root', 
        'file:/uscmst1b_scratch/lpc1/lpcmuon/ibloch/MC/MC_gen_1_8_0_pre7/CMSSW_1_8_0_pre7/src/data/muons/muplus_e_10_60_374_probev2.root')
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('/afs/cern.ch/user/i/ibloch/scratch0/eventsOutput.root')
)

process.Timing = cms.Service("Timing")

process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")

process.PoolDBESSource = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb'),
        authenticationMethod = cms.untracked.uint32(1)
    ),
    timetype = cms.string('runnumber'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('CSCCrateMapRcd'),
        tag = cms.string('CSCCrateMap')
    )),
    connect = cms.string('frontier://FrontierDev/CMS_COND_CSC')
)

process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    moduleSeeds = cms.PSet(
        g4SimHits = cms.untracked.uint32(735161370),
        ecalUnsuppressedDigis = cms.untracked.uint32(8641370),
        muonCSCDigis = cms.untracked.uint32(87315370),
        hcalDigis = cms.untracked.uint32(61528370),
        mix = cms.untracked.uint32(63370),
        siPixelDigis = cms.untracked.uint32(6016370),
        VtxSmeared = cms.untracked.uint32(435240370),
        hcalUnsuppressedDigis = cms.untracked.uint32(4578370),
        muonDTDigis = cms.untracked.uint32(23002370),
        siStripDigis = cms.untracked.uint32(32300370),
        muonRPCDigis = cms.untracked.uint32(5583370)
    ),
    sourceSeed = cms.untracked.uint32(736370)
)

process.ana = cms.EDFilter("CSCEfficiency",
    mycscunpacker = cms.untracked.string('muonCSCDigis'),
    runOnData = cms.untracked.bool(False),
    update = cms.untracked.bool(False),
    stripDigiTag = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
    WorkInEndcap = cms.untracked.int32(2),
    ExtrapolateFromStation = cms.untracked.int32(2),
    rootFileName = cms.untracked.string('monHists.root'),
    ExtrapolateToRing = cms.untracked.int32(2),
    wireDigiTag = cms.InputTag("muonCSCDigis","MuonCSCWireDigi"),
    ExtrapolateToStation = cms.untracked.int32(1),
    MuonCSCHits = cms.InputTag("mix","g4SimHitsMuonCSCHits")
)

process.p = cms.Path(process.mix*process.simMuonCSCDigis*process.csc2DRecHits*process.cscSegments*process.ana)
process.cscSegments.algo_type = 4


