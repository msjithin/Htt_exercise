import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/D84ED2D3-5B42-E811-B73B-0CC47A745294.root')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.mergedGenParticles = cms.EDProducer("MergedGenParticleProducer",
    inputPacked = cms.InputTag("packedGenParticles"),
    inputPruned = cms.InputTag("prunedGenParticles")
)


process.myGenerator = cms.EDProducer("GenParticles2HepMCConverter",
    genEventInfo = cms.InputTag("generator"),
    genParticles = cms.InputTag("mergedGenParticles"),
    signalParticlePdgIds = cms.vint32(25)
)


process.rivetProducerHTXS = cms.EDProducer("HTXSRivetProducer",
    HepMCCollection = cms.InputTag("myGenerator","unsmeared"),
    LHERunInfo = cms.InputTag("externalLHEProducer"),
    ProductionMode = cms.string('AUTO')
)


process.tauGenJets = cms.EDProducer("TauGenJetProducer",
    GenParticles = cms.InputTag("prunedGenParticles"),
    includeNeutrinos = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.tauGenJetsSelectorAllHadrons = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    select = cms.vstring('oneProng0Pi0', 
        'oneProng1Pi0', 
        'oneProng2Pi0', 
        'oneProngOther', 
        'threeProng0Pi0', 
        'threeProng1Pi0', 
        'threeProngOther', 
        'rare'),
    src = cms.InputTag("tauGenJets")
)


process.tauGenJetsSelectorElectrons = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    select = cms.vstring('electron'),
    src = cms.InputTag("tauGenJets")
)


process.tauGenJetsSelectorMuons = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    select = cms.vstring('muon'),
    src = cms.InputTag("tauGenJets")
)


process.demo = cms.EDAnalyzer("AcceptanceAnalyzer",
    electronSrc = cms.InputTag("tauGenJetsSelectorElectrons"),
    hadronSrc = cms.InputTag("tauGenJetsSelectorAllHadrons"),
    htxsRivetSrc = cms.InputTag("rivetProducerHTXS"),
    lheSrc = cms.InputTag("externalLHEProducer"),
    muonSrc = cms.InputTag("tauGenJetsSelectorMuons"),
    puSrc = cms.InputTag("slimmedAddPileupInfo")
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('ttree.root')
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.p = cms.Path(process.tauGenJets+process.tauGenJetsSelectorAllHadrons+process.tauGenJetsSelectorElectrons+process.tauGenJetsSelectorMuons+process.mergedGenParticles+process.myGenerator+process.rivetProducerHTXS+process.demo)


