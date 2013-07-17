void renameFolders(TString inputFile, TString outputFile, TString originalDirectory, TString newDirectory) 
{
  TFile f1(inputFile);
  TFile *f2 = new TFile(outputFile,"update");
  
  f1.cd(originalDirectory);
  TDirectory *old = gDirectory;
  old->ReadAll();
  
  f2->cd();
  f2->mkdir(newDirectory);
  f2->cd(newDirectory);
  old->GetList()->Write();
  f2->Close();
}
