import FWCore.ParameterSet.Config as cms
multPhiCorr_Data_EF_80X = cms.VPSet(
    cms.PSet(
      name=cms.string("hEtaPlus"),
      type=cms.int32(1),
      varType=cms.int32(0),
      etaMin=cms.double(0),
      etaMax=cms.double(2.7),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(5.32984802882e-05,-3.55548669815e-06),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.000318766675788,2.12230042625e-05),
    ),
    cms.PSet(
      name=cms.string("hEtaMinus"),
      type=cms.int32(1),
      varType=cms.int32(0),
      etaMin=cms.double(-2.7),
      etaMax=cms.double(0),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.00572243017616,-2.03320999207e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00556390549008,-1.27880027303e-06),
    ),
    cms.PSet(
      name=cms.string("h0Barrel"),
      type=cms.int32(5),
      varType=cms.int32(0),
      etaMin=cms.double(-1.392),
      etaMax=cms.double(1.392),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.0191890179765,-0.00156213933249),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.0303903328275,-0.0011447638828),
    ),
    cms.PSet(
      name=cms.string("h0EndcapPlus"),
      type=cms.int32(5),
      varType=cms.int32(0),
      etaMin=cms.double(1.392),
      etaMax=cms.double(3),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.0106624321937,-0.0003388448181),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.00757600941703,0.00140831795337),
    ),
    cms.PSet(
      name=cms.string("h0EndcapMinus"),
      type=cms.int32(5),
      varType=cms.int32(0),
      etaMin=cms.double(-3.0),
      etaMax=cms.double(-1.392),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.0156930065152,0.00107092819344),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.0503885128569,-0.00090725019983),
    ),
    cms.PSet(
      name=cms.string("gammaBarrel"),
      type=cms.int32(4),
      varType=cms.int32(0),
      etaMin=cms.double(-1.479),
      etaMax=cms.double(1.479),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(5.65199777331e-05,-5.61277831857e-06),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.000142815630488,-1.42889386184e-05),
    ),
    cms.PSet(
      name=cms.string("gammaEndcapPlus"),
      type=cms.int32(4),
      varType=cms.int32(0),
      etaMin=cms.double(1.479),
      etaMax=cms.double(3.0),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.000122999913907,4.16482368093e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.000974256878937,0.000324811194485),
    ),
    cms.PSet(
      name=cms.string("gammaEndcapMinus"),
      type=cms.int32(4),
      varType=cms.int32(0),
      etaMin=cms.double(-3.0),
      etaMax=cms.double(-1.479),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.00783698429928,-9.52501638665e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00589632397919,-0.00024439990635),
    ),
    cms.PSet(
      name=cms.string("hHFPlus"),
      type=cms.int32(6),
      varType=cms.int32(0),
      etaMin=cms.double(2.901376),
      etaMax=cms.double(5.2),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.00563779091834,2.87761562312e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00672935206246,-2.46945973914e-05),
    ),
    cms.PSet(
      name=cms.string("hHFMinus"),
      type=cms.int32(6),
      varType=cms.int32(0),
      etaMin=cms.double(-5.2),
      etaMax=cms.double(-2.901376),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.00031698238382,6.34255105138e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-4.05593109467e-05,8.14285756273e-06),
    ),
    cms.PSet(
      name=cms.string("egammaHFPlus"),
      type=cms.int32(7),
      varType=cms.int32(0),
      etaMin=cms.double(2.901376),
      etaMax=cms.double(5.2),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.010351189266,-1.47863230619e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.0113329508723,-0.000100878485059),
    ),
    cms.PSet(
      name=cms.string("egammaHFMinus"),
      type=cms.int32(7),
      varType=cms.int32(0),
      etaMin=cms.double(-5.2),
      etaMax=cms.double(-2.901376),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.0141463646933,6.89171837054e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.011960623818,9.79602637631e-05),
    ),
)