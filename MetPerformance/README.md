Copy the sample files from:

/eos/cms/store/cmst3/user/dalfonso/MET/DY_phys14.root
/eos/cms/store/cmst3/user/dalfonso/MET/GJet_Ntuple_AllHt.root


#### How to run scriptcompare 

```bash
.L scriptcompare.C
scriptcompare("input1.root" ,"input2.root", "pfmet")
```

For this test input1.root=input2.root=DY_phys14.root

This will produce the comparison plot for the pfmet variables in the file1.root and file2.root

In principle the histogram with the comparison will be saved in the current working directory. This can be changed at the end of the script.


#### How to run metresolution 

To run it standalone
```bash
.L metresolution.C+
metresolution("input.root","variable1","variable2", false)
```
This generates the sigma(variable1) vs the variable2 plots in a tgraph. It also generates the png with the result of the fits per bin so that one can inspect them easily.
If the last option of the funcion is set to true, it will also generate a plot showing the chi2 for all the fits.

If variable1 is uparaqt or upararawqt and variable2 is qt, it will generate the scale plots.

To run all the plots in one shot:
```bash
.L runmetresolution.C
metresolution("input.root")
```


##### How to run comparetgraphs.C

This script uses as input the X_tgraph.root file generated by metresolution. To run it standalone:

```bash
.L comparetgraphs.C+
comparetgraphs("X_tgraph.root")
```

For the moment only compares type1 met and raw met. It will be more general in the future.

To run all the comparison in one shot:

```bash
.L runcomparetgraphs.C
runcomparetgraphs("X_tgraph.root")
```

