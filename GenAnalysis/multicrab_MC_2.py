#multicrab

#from WMCore.Configuration import Configuration
#config = Configuration()
from CRABClient.UserUtilities import config
config = config() 
#if __name__ == '__main__':
from CRABAPI.RawCommand import crabCommand

def submit(config):
  res = crabCommand('submit', config = config)


dataset = {
  'GluGluHToTauTau' : '/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 

  }



name = 'SM_Htt_Mar06'
config.section_("General")
config.General.workArea = 'crab_'+name
config.General.transferOutputs = True
config.General.transferLogs = True
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['ggtree_mc.root'] 
config.section_("Data")

config.Data.publication = False
config.section_("Site")
config.section_("User")
config.section_("Debug")

config.Site.storageSite = 'T2_US_Wisconsin'

config.JobType.psetName = 'python/ConfFile_cfg.py'
#config.JobType.inputFiles = ['Fall17_17Nov2017_V4_MC.db','Fall17_17Nov2017_V4_MC_L2Relative_AK8PFchs.txt','Fall17_17Nov2017_V4_MC_L3Absolute_AK8PFchs.txt']
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'

#listOfSamples = [ 'embedded_B_etau','embedded_C_etau','embedded_D_etau','embedded_E_etau','embedded_F_etau','embedded_B_mutau','embedded_C_mutau','embedded_D_mutau','embedded_E_mutau','embedded_F_mutau']
#listOfSamples = [ 'DYJetsToLL_LO', 'DYJetsToLL_LOext', 'TTTo2L2Nu_powheg', 'TTToHadronic_powheg', 'TTToSemiLeptonic_powheg', 'VBFHToWWTo2L2Nu', 'WpWpJJ_QCD', 'WpWpJJ_EWK', 'GluGluHToWWTo2L2Nu', 'WZTo1L3Nu', 'WWTo2L2Nu_DoubleScattering', 'ZZTo2Q2Nu']

#listOfSamples = [ 'DY1JetsToLL' ,  'DY2JetsToLL' ,  'DY3JetsToLL' ,  'DY4JetsToLL' ]  
listOfSamples = [  'GluGluHToTauTau']

for sample in listOfSamples:  
  config.General.requestName = sample
  config.Data.inputDataset = dataset[sample]
  config.Data.unitsPerJob = 1
  config.Data.totalUnits = -1
  config.Data.outLFNDirBase = '/store/user/jmadhusu/'+name
  submit(config)
