import FWCore.ParameterSet.Config as cms
multPhiCorr_Data_C_80X = cms.VPSet(
    cms.PSet(
      name=cms.string("hEtaPlus"),
      type=cms.int32(1),
      varType=cms.int32(2),
      etaMin=cms.double(0),
      etaMax=cms.double(2.7),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.000848849885835,-8.86329447901e-06),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00465271917288,7.35142139105e-06),
    ),
    cms.PSet(
      name=cms.string("hEtaMinus"),
      type=cms.int32(1),
      varType=cms.int32(2),
      etaMin=cms.double(-2.7),
      etaMax=cms.double(0),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.0142726045497,-7.46618789255e-06),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00514910317302,9.45437223289e-06),
    ),
    cms.PSet(
      name=cms.string("h0Barrel"),
      type=cms.int32(5),
      varType=cms.int32(2),
      etaMin=cms.double(-1.392),
      etaMax=cms.double(1.392),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.0080648622097,-0.000111304337719),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.0129203348783,-0.000503368612625),
    ),
    cms.PSet(
      name=cms.string("h0EndcapPlus"),
      type=cms.int32(5),
      varType=cms.int32(2),
      etaMin=cms.double(1.392),
      etaMax=cms.double(3),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.0153819922706,0.000213551622019),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.0156150365521,7.58783854029e-05),
    ),
    cms.PSet(
      name=cms.string("h0EndcapMinus"),
      type=cms.int32(5),
      varType=cms.int32(2),
      etaMin=cms.double(-3.0),
      etaMax=cms.double(-1.392),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.0101228754372,0.000457643226684),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.0385509076312,-0.000458881064531),
    ),
    cms.PSet(
      name=cms.string("gammaBarrel"),
      type=cms.int32(4),
      varType=cms.int32(2),
      etaMin=cms.double(-1.479),
      etaMax=cms.double(1.479),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.000122670736061,1.23127764828e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.000230293242338,-2.31630150591e-05),
    ),
    cms.PSet(
      name=cms.string("gammaEndcapPlus"),
      type=cms.int32(4),
      varType=cms.int32(2),
      etaMin=cms.double(1.479),
      etaMax=cms.double(3.0),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.00102846082009,0.000343772717275),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.00201795186883,0.000675291516226),
    ),
    cms.PSet(
      name=cms.string("gammaEndcapMinus"),
      type=cms.int32(4),
      varType=cms.int32(2),
      etaMin=cms.double(-3.0),
      etaMax=cms.double(-1.479),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.015150439143,9.80599913286e-06),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00464888773105,0.000199834264912),
    ),
    cms.PSet(
      name=cms.string("hHFPlus"),
      type=cms.int32(6),
      varType=cms.int32(2),
      etaMin=cms.double(2.901376),
      etaMax=cms.double(5.2),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.022678724802,-3.03492813073e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00311860175926,-1.04624242541e-05),
    ),
    cms.PSet(
      name=cms.string("hHFMinus"),
      type=cms.int32(6),
      varType=cms.int32(2),
      etaMin=cms.double(-5.2),
      etaMax=cms.double(-2.901376),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.0187652988149,-1.07443700902e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00169218219087,2.72211511301e-06),
    ),
    cms.PSet(
      name=cms.string("egammaHFPlus"),
      type=cms.int32(7),
      varType=cms.int32(2),
      etaMin=cms.double(2.901376),
      etaMax=cms.double(5.2),
      fx=cms.string("((x*(x<100)+100*(x>=100))*[p0]+pow((x*(x<100)+100*(x>=100)),2)*[p1])"),
      px=cms.vdouble(0.00224459916144,0.00036956400043),
      fy=cms.string("((x*(x<100)+100*(x>=100))*[p0]+pow((x*(x<100)+100*(x>=100)),2)*[p1])"),
      py=cms.vdouble(-0.0080729274481,4.18524240062e-05),
    ),
    cms.PSet(
      name=cms.string("egammaHFMinus"),
      type=cms.int32(7),
      varType=cms.int32(2),
      etaMin=cms.double(-5.2),
      etaMax=cms.double(-2.901376),
      fx=cms.string("((x*(x<100)+100*(x>=100))*[p0]+pow((x*(x<100)+100*(x>=100)),2)*[p1])"),
      px=cms.vdouble(0.00111059708605,-0.000222126328475),
      fy=cms.string("((x*(x<100)+100*(x>=100))*[p0]+pow((x*(x<100)+100*(x>=100)),2)*[p1])"),
      py=cms.vdouble(9.88549419407e-05,-1.97746508427e-05),
    ),
)
