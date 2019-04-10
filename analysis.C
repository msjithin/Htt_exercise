/// make ttree.root first 
/// cmsRun GenAnalysis/python/ConfFile_cfg.py
///
/// execute this file using runAnalyzer.sh
/// bash runAnalyzer.sh
/// gStyle->SetPaintTextFormat("4.2f") for setting text format



#define analysis_cxx
#include "analysis.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include "TH1F.h"
#include <iostream>
#include <bitset>
#include <climits>
#include <cstring>
#include "Math/Minimizer.h"
#include "Math/Factory.h"
#include "Math/Functor.h"
#include "TStopwatch.h"
#include <algorithm>
#include <vector>
#include <iterator>
#include <list>
#include <set>
#include "TMath.h" //M_PI is in TMath
#include "TRandom3.h"
#include <TLorentzVector.h>
using namespace std;
int main(int argc, const char* argv[])
{

  std::string SampleName = argv[5];

  Long64_t maxEvents = atof(argv[3]);
  if (maxEvents < -1LL)
    {
      std::cout<<"Please enter a valid value for maxEvents (parameter 3)."<<std::endl;
      return 1;
    }
  int reportEvery = atof(argv[4]);
  if (reportEvery < 1)
    {
      std::cout<<"Please enter a valid value for reportEvery (parameter 4) "<<std::endl;
      return 1;
    }
  //std::string SampleName = argv[5];
  analysis t(argv[1],argv[2]);
  t.Loop(maxEvents,reportEvery, SampleName);
  return 0;
}

void analysis::Loop(Long64_t maxEvents, int reportEvery, string SampleName)
{
//   In a ROOT session, you can do:
//      root> .L analysis.C
//      root> analysis t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;
   TString sample = TString(SampleName);
   
   float dRbins[8]={0,0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
   float pTbins[9] = {0, 100,  200,  300, 500, 700, 900, 1100, 1300};
   TH1F *hist_deltaR = new TH1F("hist_deltaR", "delta_R_binned", 7,dRbins);
   TH1F *hist_higgsPt= new TH1F("hist_higgspt", "higgsPt_binned", 8,pTbins);
   TH2F *hist_dr_Hpt = new TH2F ("dR_HiggsPt", "dR vs higgsPt", 8,pTbins,7,dRbins);
   TH2F *hist_dr_Hpt_j1 = new TH2F ("dR_HiggsPt_1jet", "dR vs higgsPt , njets >=1", 8,pTbins,7,dRbins);
   TH2F *hist_dr_Hpt_j2 = new TH2F ("dR_HiggsPt_2jet", "dR vs higgsPt , njets >=2", 8,pTbins,7,dRbins);
   
      
   Long64_t nentries = fChain->GetEntries();
   std::cout<<"Coming in: "<<std::endl;
   std::cout<<"nentries:"<<nentries<<std::endl;

   float ngen = nentries;
   float luminosity = 100000; // in pb-1  
   float xs = 44.14*0.0627; 
   float weight=luminosity*xs/ngen; // luminosity & xs weighting
   //TH1F *h_higgsPt = new TH1F("h_higgsPt", "Higgs Pt", 10, 0, 1000);
   std::cout<<"weight =  "<< weight<<std::endl;

   //std::cout<< "This works Line 80 in .c file" << endl;
   Long64_t nbytes = 0, nb = 0;
   Long64_t nentriesToCheck = nentries;
   if (maxEvents != -1LL && nentries > maxEvents)
     nentriesToCheck = maxEvents;
   //std::cout<< "This works Line 85 in .c file" << endl;
   for (Long64_t jentry=0; jentry<nentriesToCheck;jentry++) {
     // std::cout<< "This works Line 87 in .c file" << endl;
     
      Long64_t ientry = LoadTree(jentry);
      //std::cout<< "This works Line 90 in .c file" << endl;

      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      //if (Cut(ientry) < 0) continue;
      if (deltaR_inc > 0)
	{
	  hist_higgsPt->Fill(higgsPt, weight);
	  hist_deltaR->Fill(deltaR_inc, weight);
	  hist_dr_Hpt->Fill(higgsPt, deltaR_inc, weight);
	  if (nJets >= 1)
	    {
	      hist_dr_Hpt_j1->Fill(higgsPt, deltaR_inc, weight);
	    }
	  if (nJets >= 2)
	    {
	      hist_dr_Hpt_j2->Fill(higgsPt, deltaR_inc, weight);
	    }
	  
	}
      //std::cout<< "This works Line 94 in .c file" << endl;
      if (jentry%reportEvery == 0)
	{
	  std::cout<<"Finished entry "<<jentry<<"/"<<(nentriesToCheck-1)<<std::endl;
	}
   }
      
   hist_deltaR->GetXaxis()->SetTitle("delta R");
   hist_higgsPt->GetXaxis()->SetTitle("Higgs pt [GeV]");
   hist_dr_Hpt->GetXaxis()->SetTitle("Higgs pt [GeV]");
   hist_dr_Hpt->GetYaxis()->SetTitle("delta R");
 
   hist_dr_Hpt_j1->GetXaxis()->SetTitle("Higgs pt [GeV]");
   hist_dr_Hpt_j1->GetYaxis()->SetTitle("delta R");
   
   hist_dr_Hpt_j2->GetXaxis()->SetTitle("Higgs pt [GeV]");
   hist_dr_Hpt_j2->GetYaxis()->SetTitle("delta R");   


}
void analysis::BookHistos(const char* file2)
{
  fileName = new TFile(file2, "RECREATE");
  //tree = new TTree("ADD","ADD");
  //tree->Branch("event_","std::vector<unsigned int>",&event_);
  //tree->Branch("event_info","std::vector<double>",&event_info);
  fileName->cd();

}
