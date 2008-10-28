#ifndef UTIL
#define UTIL
#include <utility> 
#endif

#ifndef MAP
#define MAP
#include <map>
#endif

#ifndef VECTOR
#define VECTOR
#include <vector>
#endif


{
  string MyDirectory = "/afs/cern.ch/user/s/stoyan/CSCEff/CMSSW_2_1_9/src/RecoLocalMuon/CSCEfficiency/test/";
  string MySubDirectory = "./";
  //string MyFileName = "endCap1_ME31_MC.root";
  //string MyFileName = "endCap1_ME31.root";
  string MyFileName = "endCap2_ME41.root";
  string MyFullPath;
  char *file_name;

  MyFullPath =  MyDirectory +  MySubDirectory + MyFileName;
  file_name = MyFullPath.c_str();
  TFile *f1=
    (TFile*)gROOT->GetListOfFiles()->FindObject(file_name);
  if (!f1){
    TFile *f1 = new TFile(file_name);
  }


  // All files in a vector
  std::vector< TFile * > DataFiles;
  DataFiles.push_back(f1);
  //string mytitle;
  //char *MyTitle;


  // default
  TCanvas *c2 = new TCanvas("c2", "canvas 2",16,30,700,500);
  //gStyle->SetOptStat(1110);
  gStyle->SetOptStat(0);
  gStyle->SetTitleW(0.65);
  gStyle->SetTitleH(0.08);
  gStyle->SetStatW(0.25);
  gStyle->SetStatH(0.2);
  gStyle->SetHistFillStyle(1001);
  //gStyle->SetOptStat(100);

  gStyle->SetLineColor(1);
  gStyle->SetHistFillStyle(1001);
  gStyle->SetHistFillColor(51);
  gStyle->SetHistLineWidth(2);
  gStyle->SetHistLineColor(4);
  gStyle->SetFrameFillColor(4000);
  gStyle->SetTitleW(0.45);
  gStyle->SetTitleH(0.07);
  gStyle->SetStatW(0.25);
  gStyle->SetStatH(0.2);
  //gPad->SetFillColor(4000);
  //gStyle->SetHistFillStyle(5101);
  gStyle->SetErrorX(0);
  c2->SetFillStyle(0);
  c2->SetGrid();
  gPad->SetFillColor(0);

  TH1F *data_p1;
  //std::vector <TH1F *> data_D1;
  string histo_1, histo_2, histo_3;

  // Choose what to plot
  int efficiencyType;
  std::string theEfficiencyType;
  cout<<"Choose which efficiency to plot.\n";
  cout<<"Type a number...\n";
  cout<<"   LCTs = 1; Strip = 2; WireGroup = 3; Rechit = 4; Rechit_good = 5; 
   Rechit_inSegment= 6;Segment = 7;  Attachment = 8; Rechit(simhit based) = 9\n";
  cin>>efficiencyType;
  //cin.ignore();
  // Plots...
  // user
  std::string tmp;
  int FirstChamber = 1;
  int LastChamber = 36;
  char *title = "CSC";
  char *name = "CSC";
  switch (efficiencyType){
  case 1:
    // LCTs
    theEfficiencyType = "LCTs";
    title = "LCT efficiency per chamber;Chamber # ;efficiency";
    break;
  case 2:
    // Strip
    theEfficiencyType = "Strips";
    title = "Strip efficiency per chamber;Chamber # ;efficiency";
    break;
  case 3:
    // WireGroup
    theEfficiencyType = "WireGroups";
    title = "WireGroup efficiency per chamber;Chamber # ;efficiency";
    break;
  case 4:
    // Rechit
    theEfficiencyType = "Rechits";
    title = "RecHit efficiency per chamber;Chamber # ;efficiency";
    name = "FINAL_Rechit_Efficiency_perChamber";
    break;
  case 5:
    // Rechit good
    theEfficiencyType = "Rechits_good";
    title = "RecHit efficiency (in a sensitive area) per chamber;Chamber # ;efficiency";
    name = "FINAL_Rechit_good_Efficiency_perChamber";
    break;
  case 6:
    // Rechit_inSegment
    theEfficiencyType = "Rechits_inSegment";
    title = "RecHit efficiency (in segment) per chamber;Chamber # ;efficiency";
    name = "FINAL_Rechit_inSegment_Efficiency_perChamber";
    break;
  case 7:
    // Segment
    theEfficiencyType = "Segments";
    title = "Segment efficiency  per chamber;Chamber # ;efficiency";
    name = "FINAL_Segment_Efficiency_perChamber";
    break;
  case 8:
    // Attachment
    theEfficiencyType = "Attachment";
    title = "Attachment efficiency  per chamber;Chamber # ;efficiency";
    name = "FINAL_Attachment_Efficiency_perChamber";
    break;
  case 9:
    // SimRechit
    theEfficiencyType = "SimRechit";
    title = "Rechit (simhit based: nLayer_RH/nLayer_SH) efficiency  per chamber;Chamber # ;efficiency";
    break;
/*
  case 9:
    // SimRechit_each
    theEfficiencyType = "SimRechit_each";
    title = "Rechit (per simhit) efficiency  per chamber;Chamber # ;efficiency";
     break;
    */
  default:
    break;
  }
  cout<<"Plotting "<<theEfficiencyType.c_str() <<" efficiency"<<endl;
  TH1F histo      = TH1F("histo",title,LastChamber-FirstChamber+1,float(FirstChamber)-0.5,float(LastChamber)+0.5);
  TH1F histo_denom      = TH1F("histo_denom",title,LastChamber-FirstChamber+1,float(FirstChamber)-0.5,float(LastChamber)+0.5);
  for(int iCh = FirstChamber;iCh<LastChamber+1;iCh++){
    tmp = Form("Chamber_%d/Efficient",iCh)+theEfficiencyType;  
    histo_1 = Form("_Ch%d",iCh);
    if(7==efficiencyType){
      tmp = Form("AllChambers/Efficient");
      histo_1 = Form("Segments");
    }
    else if(8==efficiencyType){
      tmp = Form("Chamber_%d/InefficientSingleHits",iCh);
      histo_1 = Form("_Ch%d",iCh);
    }
    else if(9==efficiencyType){
      tmp = Form("Chamber_%d/Sim_Rechits",iCh);
      histo_1 = Form("_Ch%d",iCh);
    }
    histo_1 = tmp + histo_1; 
    char *histo_full = histo_1.c_str();
    std::cout<<histo_full<<std::endl;
    data_p1=(TH1F*)(*(DataFiles[0]))->Get(histo_full);

    const int min = 2;
    const int max = 7;
    int reference = 9;
    if(6==efficiencyType){
      reference = 10;
    }
    float effS =    data_p1->Integral(min,max);   
    float allS = 6.*data_p1->GetBinContent(reference);   
    if(7==efficiencyType){
      histo_3 = Form("AllChambers/AllSegments");
      char *histo_full3 = histo_3.c_str();
      std::cout<<histo_full3<<std::endl;
      TH1F * data_p3 =(TH1F*)(*(DataFiles[0]))->Get(histo_full3);
      allS =  data_p3->GetBinContent(iCh);
      effS =  data_p1->GetBinContent(iCh);
    }
    else if(8==efficiencyType){
      histo_3 = Form("Chamber_%d/AllSingleHits_Ch%d",iCh,iCh);
      char *histo_full3 = histo_3.c_str();
      std::cout<<histo_full3<<std::endl;
      TH1F * data_p3 =(TH1F*)(*(DataFiles[0]))->Get(histo_full3);
      allS =  data_p3->Integral(min,max);
      effS = allS-effS;
    }
    else if(9==efficiencyType){
     histo_3 = Form("Chamber_%d/Sim_Simhits_Ch%d",iCh,iCh);
      char *histo_full3 = histo_3.c_str();
      std::cout<<histo_full3<<std::endl;
      TH1F * data_p3 =(TH1F*)(*(DataFiles[0]))->Get(histo_full3);
      allS =  data_p3->Integral(min,max);     
    }

    histo->SetBinContent(iCh,effS);
    histo_denom->SetBinContent(iCh,allS);
      //
    /*
    data_p1->Fit("pol0","Q");
    TF1 *fit = data_p1->GetFunction("pol0");
    float param = fit->GetParameter(0);
    float error = fit->GetParError(0);
    histo->SetBinContent(LastChamber-iCh+1,param); 
    histo->SetBinError(LastChamber-iCh+1,error); 
    */
  }
  //histo->SetMarkerStyle(21);
  //histo->SetMarkerColor(kBlue);
  //histo->SetLineColor(kBlue);
  //histo->Draw();
  int  chRange = LastChamber-FirstChamber+1;
  TGraphAsymmErrors* g_eff = new TGraphAsymmErrors(chRange);
  const TH1F *h_const = (TH1F*)histo->Clone("hnew");
  const TH1F *hd_const = (TH1F*)histo_denom->Clone("hnew2");
  g_eff->BayesDivide(h_const,hd_const);
  //g_eff->BayesDivide(histo,histo_denom);
  g_eff->SetTitle(title);
  g_eff->SetName(name);
  g_eff->Draw("ap*");
}
