import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(10000)

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        #'file:/afs/cern.ch/work/t/truggles/Z_to_tautau/dyjets_76x.root'
        #'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall15MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/002ABFCA-A0B9-E511-B9BA-0CC47A57CD6A.root',
        
        #'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/6A62DE01-E641-E811-AFF1-008CFAC94038.root',
        #'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/70000/DA1BE8CB-5444-E811-BDBF-0025905A48FC.root',
        
        #'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/70000/0C335F78-5644-E811-B6E5-0CC47A7452DA.root',
#        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/D84ED2D3-5B42-E811-B73B-0CC47A745294.root',
#        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/FE4D4DD9-5B42-E811-A066-0CC47A4D76B6.root',
        #'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/DCCA61BA-2B21-E911-94C7-44A842CFD667.root'
        
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/763A7921-EF20-E911-BD8B-44A842CF05B2.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/C46A701F-EF20-E911-A144-44A842CFD5F2.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/EE5A0F69-0521-E911-86C3-44A842CFD626.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/60B64277-0521-E911-9706-B499BAAC0A22.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/70B2A1A3-0E21-E911-B957-44A842CFD5CB.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/280C50A7-0E21-E911-A214-484D7E8DF085.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/20301EA9-0E21-E911-93F9-44A842CFD64D.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/82DCC89F-1321-E911-83E9-44A842CFD64D.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/0604D195-1421-E911-A3BD-6C3BE5B59210.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/46CE51F5-1A21-E911-BC47-44A842CFD64D.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/D4018420-1A21-E911-9C8B-6C3BE5B59210.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/D24C64BB-2321-E911-949A-6C3BE5B5A038.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/A0BAD3A1-2321-E911-AABD-B499BAAC04E6.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/3C01C018-2921-E911-B992-B499BAAC04E6.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/DCCA61BA-2B21-E911-94C7-44A842CFD667.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/D0BA83B1-3D21-E911-A905-484D7E8DF051.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/A03AC4B7-3D21-E911-A4E0-44A842CFD64D.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/0A52B0C2-3D21-E911-BC74-D8D385B0EE2E.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/524C7FB6-3D21-E911-A54D-44A842CF05BF.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/ECF531F6-3E21-E911-AA18-44A842CF05D9.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/406470FA-3E21-E911-9F96-001CC4A61C52.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/94429AEE-3E21-E911-AAE9-44A842CFC97E.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/8CE664B6-3D21-E911-9CF0-484D7E8DF0FA.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/047009D4-3D21-E911-9727-6C3BE5B541F8.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/BA70ABEA-4121-E911-8AF6-484D7E8DF051.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/7AF95723-4621-E911-86DF-484D7E8DF051.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/6CBDE5C4-4721-E911-B941-44A842CFC9F3.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/98A92539-4E21-E911-9A17-44A842CFD60C.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/E6C9C69A-4B21-E911-A92C-B499BAAC0658.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/1292CBA1-5021-E911-B3DB-B499BAAC0658.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/A0554F70-5721-E911-A9D8-44A842CFD5D8.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/7E2573F9-5B21-E911-A92B-44A842CFD5D8.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/EE054650-5A21-E911-9646-484D7E8DF0D3.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/D695C2E9-6221-E911-8B8B-001CC47BEE5E.root',
        'file:root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/GluGluHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/10000/F8E1F88F-3022-E911-AEF0-44A842CFCA1A.root'
    )
)
#process.genJets = cms.EDProducer(
#    "FastjetJetProducer",
#    GenJetParameters,
#    AnomalousCellParameters,
#    jetAlgorithm = cms.string("AntiKt"),
#    rParam       = cms.double(0.4)
#)


process.tauGenJets = cms.EDProducer(
    "TauGenJetProducer",
    GenParticles =  cms.InputTag('prunedGenParticles'),
    includeNeutrinos = cms.bool( False ),
    verbose = cms.untracked.bool( False )
    )

process.tauGenJetsSelectorAllHadrons = cms.EDFilter("TauGenJetDecayModeSelector",
     src = cms.InputTag("tauGenJets"),
     select = cms.vstring('oneProng0Pi0', 
                          'oneProng1Pi0', 
                          'oneProng2Pi0', 
                          'oneProngOther',
                          'threeProng0Pi0', 
                          'threeProng1Pi0', 
                          'threeProngOther', 
                          'rare'),
     filter = cms.bool(False)
)

process.tauGenJetsSelectorElectrons = cms.EDFilter("TauGenJetDecayModeSelector",
     src = cms.InputTag("tauGenJets"),
     select = cms.vstring('electron'), 
     filter = cms.bool(False)
)

process.tauGenJetsSelectorMuons = cms.EDFilter("TauGenJetDecayModeSelector",
     src = cms.InputTag("tauGenJets"),
     select = cms.vstring('muon'), 
     filter = cms.bool(False)
)



process.rivetProducerHTXS = cms.EDProducer('HTXSRivetProducer',
  HepMCCollection = cms.InputTag('myGenerator','unsmeared'),
  LHERunInfo = cms.InputTag('externalLHEProducer'),
  #ProductionMode = cms.string('GGF'),
  ProductionMode = cms.string('AUTO'),
)



#MINIAOD

process.mergedGenParticles = cms.EDProducer("MergedGenParticleProducer",
    inputPruned = cms.InputTag("prunedGenParticles"),
    inputPacked = cms.InputTag("packedGenParticles"),
)

process.myGenerator = cms.EDProducer("GenParticles2HepMCConverter",
    genParticles = cms.InputTag("mergedGenParticles"),
    genEventInfo = cms.InputTag("generator"),
    signalParticlePdgIds = cms.vint32(25), ## for the Higgs analysis
)



#process.load("GeneratorInterface.RivetInterface.genParticles2HepMC_cff")
#process.rivetProducerHTXS = cms.EDProducer('HTXSRivetProducer',
#                                           HepMCCollection = cms.InputTag('myGenerator','unsmeared'),
#                                           LHERunInfo = cms.InputTag('externalLHEProducer'),
#                                           ProductionMode = cms.string('AUTO'),
#)

process.load("SM_Htt.GenAnalysis.CfiFile_cfi")
#process.load("GenAnalysis.AcceptanceAnalyzer.CfiFile_cfi")
process.demo = cms.EDAnalyzer('AcceptanceAnalyzer',
    hadronSrc = cms.InputTag('tauGenJetsSelectorAllHadrons'),
    electronSrc = cms.InputTag('tauGenJetsSelectorElectrons'),
    muonSrc = cms.InputTag('tauGenJetsSelectorMuons'),
    puSrc = cms.InputTag('slimmedAddPileupInfo'),
    htxsRivetSrc = cms.InputTag('rivetProducerHTXS'),
    lheSrc = cms.InputTag('externalLHEProducer')
)

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('ttree.root')
                                   )


#process.out = cms.OutputModule("PoolOutputModule",
#    fileName = cms.untracked.string('myOutputFile.root')
#    ,outputCommands = cms.untracked.vstring('drop *',
#      #"keep *_myProducerLabel_*_*",
#      #"keep *_slimmedMuons_*_*",
#      "keep *_*_*_Demo",
#        )
#)

process.p = cms.Path(process.tauGenJets*
#            process.genJets*
            process.tauGenJetsSelectorAllHadrons*
            process.tauGenJetsSelectorElectrons*
            process.tauGenJetsSelectorMuons*
            process.mergedGenParticles*
            process.myGenerator*
            process.rivetProducerHTXS*
            process.demo)

#process.e = cms.EndPath(process.out)
