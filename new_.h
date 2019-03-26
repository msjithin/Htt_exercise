//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Tue Mar 26 06:20:58 2019 by ROOT version 6.10/09
// from TTree Ntuple/My Analyzer Ntuple
// found on file: ttree.root
//////////////////////////////////////////////////////////

#ifndef new__h
#define new__h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class new_ {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Float_t         run;
   Float_t         lumi;
   Double_t        eventD;
   Float_t         genMass;
   Float_t         ETauPass;
   Float_t         ETauD;
   Float_t         MuTauPass;
   Float_t         MuTauD;
   Float_t         EMuPass;
   Float_t         EMuD;
   Float_t         TauTauPass;
   Float_t         TauTau4030Pass;
   Float_t         TauTauD;
   Float_t         MuMuPass;
   Float_t         MuMuD;
   Float_t         threeLeptons;
   Float_t         nLooseTaus;
   Float_t         nLooseElec;
   Float_t         nLooseMu;
   Float_t         nTruePU;
   Float_t         tauPt1;
   Float_t         tauPt2;
   Float_t         tauPt3;
   Float_t         tauEta1;
   Float_t         tauEta2;
   Float_t         tauEta3;
   Float_t         tauPhi1;
   Float_t         tauPhi2;
   Float_t         tauPhi3;
   Float_t         d_phi;
   Float_t         d_eta;
   Float_t         higgsPt;
   Float_t         deltaR_inc;
   Float_t         deltaR_et;
   Float_t         deltaR_et_1;
   Float_t         deltaR_et_2;
   Float_t         deltaR_et_3;
   Float_t         deltaR_mt;
   Float_t         deltaR_mt_1;
   Float_t         deltaR_mt_2;
   Float_t         deltaR_mt_3;
   Float_t         deltaR_tt;
   Float_t         deltaR_tt_1;
   Float_t         deltaR_tt_2;
   Float_t         deltaR_tt_3;
   Float_t         deltaR_em;
   Float_t         deltaR_em_1;
   Float_t         deltaR_em_2;
   Float_t         deltaR_em_3;
   Float_t         higgsPt;
   Float_t         higgsPt_et;
   Float_t         higgsPt_et_1;
   Float_t         higgsPt_et_2;
   Float_t         higgsPt_et_3;
   Float_t         higgsPt_mt;
   Float_t         higgsPt_mt_1;
   Float_t         higgsPt_mt_2;
   Float_t         higgsPt_mt_3;
   Float_t         higgsPt_tt;
   Float_t         higgsPt_tt_1;
   Float_t         higgsPt_tt_2;
   Float_t         higgsPt_tt_3;
   Float_t         higgsPt_em;
   Float_t         higgsPt_em_1;
   Float_t         higgsPt_em_2;
   Float_t         higgsPt_em_3;
   Int_t           nTau;
   Int_t           nJets;
   Int_t           nJets30;
   Float_t         JetPt;
   Int_t           nMuTau;
   Int_t           nETau;
   Int_t           nHTau;
   Int_t           nEMu;

   // List of branches
   TBranch        *b_run;   //!
   TBranch        *b_lumi;   //!
   TBranch        *b_eventD;   //!
   TBranch        *b_genMass;   //!
   TBranch        *b_ETauPass;   //!
   TBranch        *b_ETauD;   //!
   TBranch        *b_MuTauPass;   //!
   TBranch        *b_MuTauD;   //!
   TBranch        *b_EMuPass;   //!
   TBranch        *b_EMuD;   //!
   TBranch        *b_TauTauPass;   //!
   TBranch        *b_TauTau4030Pass;   //!
   TBranch        *b_TauTauD;   //!
   TBranch        *b_MuMuPass;   //!
   TBranch        *b_MuMuD;   //!
   TBranch        *b_threeLeptons;   //!
   TBranch        *b_nLooseTaus;   //!
   TBranch        *b_nLooseElec;   //!
   TBranch        *b_nLooseMu;   //!
   TBranch        *b_nTruePU;   //!
   TBranch        *b_tauPt1;   //!
   TBranch        *b_tauPt2;   //!
   TBranch        *b_tauPt3;   //!
   TBranch        *b_tauEta1;   //!
   TBranch        *b_tauEta2;   //!
   TBranch        *b_tauEta3;   //!
   TBranch        *b_tauPhi1;   //!
   TBranch        *b_tauPhi2;   //!
   TBranch        *b_tauPhi3;   //!
   TBranch        *b_d_phi;   //!
   TBranch        *b_d_eta;   //!
   TBranch        *b_higgsPt;   //!
   TBranch        *b_deltaR_inc;   //!
   TBranch        *b_deltaR_et;   //!
   TBranch        *b_deltaR_et_1;   //!
   TBranch        *b_deltaR_et_2;   //!
   TBranch        *b_deltaR_et_3;   //!
   TBranch        *b_deltaR_mt;   //!
   TBranch        *b_deltaR_mt_1;   //!
   TBranch        *b_deltaR_mt_2;   //!
   TBranch        *b_deltaR_mt_3;   //!
   TBranch        *b_deltaR_tt;   //!
   TBranch        *b_deltaR_tt_1;   //!
   TBranch        *b_deltaR_tt_2;   //!
   TBranch        *b_deltaR_tt_3;   //!
   TBranch        *b_deltaR_em;   //!
   TBranch        *b_deltaR_em_1;   //!
   TBranch        *b_deltaR_em_2;   //!
   TBranch        *b_deltaR_em_3;   //!
   TBranch        *b_higgsPt;   //!
   TBranch        *b_higgsPt_et;   //!
   TBranch        *b_higgsPt_et_1;   //!
   TBranch        *b_higgsPt_et_2;   //!
   TBranch        *b_higgsPt_et_3;   //!
   TBranch        *b_higgsPt_mt;   //!
   TBranch        *b_higgsPt_mt_1;   //!
   TBranch        *b_higgsPt_mt_2;   //!
   TBranch        *b_higgsPt_mt_3;   //!
   TBranch        *b_higgsPt_tt;   //!
   TBranch        *b_higgsPt_tt_1;   //!
   TBranch        *b_higgsPt_tt_2;   //!
   TBranch        *b_higgsPt_tt_3;   //!
   TBranch        *b_higgsPt_em;   //!
   TBranch        *b_higgsPt_em_1;   //!
   TBranch        *b_higgsPt_em_2;   //!
   TBranch        *b_higgsPt_em_3;   //!
   TBranch        *b_nTau;   //!
   TBranch        *b_nJets;   //!
   TBranch        *b_nJets30;   //!
   TBranch        *b_JetPt;   //!
   TBranch        *b_nMuTau;   //!
   TBranch        *b_nETau;   //!
   TBranch        *b_nHTau;   //!
   TBranch        *b_nEMu;   //!

   new_(TTree *tree=0);
   virtual ~new_();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef new__cxx
new_::new_(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("ttree.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("ttree.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("ttree.root:/demo/events");
      dir->GetObject("Ntuple",tree);

   }
   Init(tree);
}

new_::~new_()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t new_::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t new_::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void new_::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("run", &run, &b_run);
   fChain->SetBranchAddress("lumi", &lumi, &b_lumi);
   fChain->SetBranchAddress("eventD", &eventD, &b_eventD);
   fChain->SetBranchAddress("genMass", &genMass, &b_genMass);
   fChain->SetBranchAddress("ETauPass", &ETauPass, &b_ETauPass);
   fChain->SetBranchAddress("ETauD", &ETauD, &b_ETauD);
   fChain->SetBranchAddress("MuTauPass", &MuTauPass, &b_MuTauPass);
   fChain->SetBranchAddress("MuTauD", &MuTauD, &b_MuTauD);
   fChain->SetBranchAddress("EMuPass", &EMuPass, &b_EMuPass);
   fChain->SetBranchAddress("EMuD", &EMuD, &b_EMuD);
   fChain->SetBranchAddress("TauTauPass", &TauTauPass, &b_TauTauPass);
   fChain->SetBranchAddress("TauTau4030Pass", &TauTau4030Pass, &b_TauTau4030Pass);
   fChain->SetBranchAddress("TauTauD", &TauTauD, &b_TauTauD);
   fChain->SetBranchAddress("MuMuPass", &MuMuPass, &b_MuMuPass);
   fChain->SetBranchAddress("MuMuD", &MuMuD, &b_MuMuD);
   fChain->SetBranchAddress("threeLeptons", &threeLeptons, &b_threeLeptons);
   fChain->SetBranchAddress("nLooseTaus", &nLooseTaus, &b_nLooseTaus);
   fChain->SetBranchAddress("nLooseElec", &nLooseElec, &b_nLooseElec);
   fChain->SetBranchAddress("nLooseMu", &nLooseMu, &b_nLooseMu);
   fChain->SetBranchAddress("nTruePU", &nTruePU, &b_nTruePU);
   fChain->SetBranchAddress("tauPt1", &tauPt1, &b_tauPt1);
   fChain->SetBranchAddress("tauPt2", &tauPt2, &b_tauPt2);
   fChain->SetBranchAddress("tauPt3", &tauPt3, &b_tauPt3);
   fChain->SetBranchAddress("tauEta1", &tauEta1, &b_tauEta1);
   fChain->SetBranchAddress("tauEta2", &tauEta2, &b_tauEta2);
   fChain->SetBranchAddress("tauEta3", &tauEta3, &b_tauEta3);
   fChain->SetBranchAddress("tauPhi1", &tauPhi1, &b_tauPhi1);
   fChain->SetBranchAddress("tauPhi2", &tauPhi2, &b_tauPhi2);
   fChain->SetBranchAddress("tauPhi3", &tauPhi3, &b_tauPhi3);
   fChain->SetBranchAddress("d_phi", &d_phi, &b_d_phi);
   fChain->SetBranchAddress("d_eta", &d_eta, &b_d_eta);
   fChain->SetBranchAddress("higgsPt", &higgsPt, &b_higgsPt);
   fChain->SetBranchAddress("deltaR_inc", &deltaR_inc, &b_deltaR_inc);
   fChain->SetBranchAddress("deltaR_et", &deltaR_et, &b_deltaR_et);
   fChain->SetBranchAddress("deltaR_et_1", &deltaR_et_1, &b_deltaR_et_1);
   fChain->SetBranchAddress("deltaR_et_2", &deltaR_et_2, &b_deltaR_et_2);
   fChain->SetBranchAddress("deltaR_et_3", &deltaR_et_3, &b_deltaR_et_3);
   fChain->SetBranchAddress("deltaR_mt", &deltaR_mt, &b_deltaR_mt);
   fChain->SetBranchAddress("deltaR_mt_1", &deltaR_mt_1, &b_deltaR_mt_1);
   fChain->SetBranchAddress("deltaR_mt_2", &deltaR_mt_2, &b_deltaR_mt_2);
   fChain->SetBranchAddress("deltaR_mt_3", &deltaR_mt_3, &b_deltaR_mt_3);
   fChain->SetBranchAddress("deltaR_tt", &deltaR_tt, &b_deltaR_tt);
   fChain->SetBranchAddress("deltaR_tt_1", &deltaR_tt_1, &b_deltaR_tt_1);
   fChain->SetBranchAddress("deltaR_tt_2", &deltaR_tt_2, &b_deltaR_tt_2);
   fChain->SetBranchAddress("deltaR_tt_3", &deltaR_tt_3, &b_deltaR_tt_3);
   fChain->SetBranchAddress("deltaR_em", &deltaR_em, &b_deltaR_em);
   fChain->SetBranchAddress("deltaR_em_1", &deltaR_em_1, &b_deltaR_em_1);
   fChain->SetBranchAddress("deltaR_em_2", &deltaR_em_2, &b_deltaR_em_2);
   fChain->SetBranchAddress("deltaR_em_3", &deltaR_em_3, &b_deltaR_em_3);
//    fChain->SetBranchAddress("higgsPt", &higgsPt, &b_higgsPt);
   fChain->SetBranchAddress("higgsPt_et", &higgsPt_et, &b_higgsPt_et);
   fChain->SetBranchAddress("higgsPt_et_1", &higgsPt_et_1, &b_higgsPt_et_1);
   fChain->SetBranchAddress("higgsPt_et_2", &higgsPt_et_2, &b_higgsPt_et_2);
   fChain->SetBranchAddress("higgsPt_et_3", &higgsPt_et_3, &b_higgsPt_et_3);
   fChain->SetBranchAddress("higgsPt_mt", &higgsPt_mt, &b_higgsPt_mt);
   fChain->SetBranchAddress("higgsPt_mt_1", &higgsPt_mt_1, &b_higgsPt_mt_1);
   fChain->SetBranchAddress("higgsPt_mt_2", &higgsPt_mt_2, &b_higgsPt_mt_2);
   fChain->SetBranchAddress("higgsPt_mt_3", &higgsPt_mt_3, &b_higgsPt_mt_3);
   fChain->SetBranchAddress("higgsPt_tt", &higgsPt_tt, &b_higgsPt_tt);
   fChain->SetBranchAddress("higgsPt_tt_1", &higgsPt_tt_1, &b_higgsPt_tt_1);
   fChain->SetBranchAddress("higgsPt_tt_2", &higgsPt_tt_2, &b_higgsPt_tt_2);
   fChain->SetBranchAddress("higgsPt_tt_3", &higgsPt_tt_3, &b_higgsPt_tt_3);
   fChain->SetBranchAddress("higgsPt_em", &higgsPt_em, &b_higgsPt_em);
   fChain->SetBranchAddress("higgsPt_em_1", &higgsPt_em_1, &b_higgsPt_em_1);
   fChain->SetBranchAddress("higgsPt_em_2", &higgsPt_em_2, &b_higgsPt_em_2);
   fChain->SetBranchAddress("higgsPt_em_3", &higgsPt_em_3, &b_higgsPt_em_3);
   fChain->SetBranchAddress("nTau", &nTau, &b_nTau);
   fChain->SetBranchAddress("nJets", &nJets, &b_nJets);
   fChain->SetBranchAddress("nJets30", &nJets30, &b_nJets30);
   fChain->SetBranchAddress("JetPt", &JetPt, &b_JetPt);
   fChain->SetBranchAddress("nMuTau", &nMuTau, &b_nMuTau);
   fChain->SetBranchAddress("nETau", &nETau, &b_nETau);
   fChain->SetBranchAddress("nHTau", &nHTau, &b_nHTau);
   fChain->SetBranchAddress("nEMu", &nEMu, &b_nEMu);
   Notify();
}

Bool_t new_::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void new_::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t new_::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef new__cxx
