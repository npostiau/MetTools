import FWCore.ParameterSet.Config as cms
multPhiCorr_Data_80X = cms.VPSet(
    cms.PSet(
      name=cms.string("hEtaPlus"),
      type=cms.int32(1),
      varType=cms.int32(0),
      etaMin=cms.double(0),
      etaMax=cms.double(2.7),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(4.82414557403e-05,-3.22287566414e-06),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(4.92636921261e-05,-3.27080237092e-06),
    ),
    cms.PSet(
      name=cms.string("hEtaMinus"),
      type=cms.int32(1),
      varType=cms.int32(0),
      etaMin=cms.double(-2.7),
      etaMax=cms.double(0),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.000598041052036,-3.98618348883e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(8.02883643356e-06,-5.4062067728e-07),
    ),
    cms.PSet(
      name=cms.string("h0Barrel"),
      type=cms.int32(5),
      varType=cms.int32(0),
      etaMin=cms.double(-1.392),
      etaMax=cms.double(1.392),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.00249041832347,-0.000996990556513),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00383619832307,-0.00153500005641),
    ),
    cms.PSet(
      name=cms.string("h0EndcapPlus"),
      type=cms.int32(5),
      varType=cms.int32(0),
      etaMin=cms.double(1.392),
      etaMax=cms.double(3),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.0015596541875,-0.000623788498067),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.00368583341269,0.00147439734346),
    ),
    cms.PSet(
      name=cms.string("h0EndcapMinus"),
      type=cms.int32(5),
      varType=cms.int32(0),
      etaMin=cms.double(-3.0),
      etaMax=cms.double(-1.392),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.00083701647833,0.000334905305443),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.00465282346592,0.00186106372912),
    ),
    cms.PSet(
      name=cms.string("gammaBarrel"),
      type=cms.int32(4),
      varType=cms.int32(0),
      etaMin=cms.double(-1.479),
      etaMax=cms.double(1.479),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(9.65210297735e-05,-9.66048369137e-06),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-3.89895140972e-05,3.95064848926e-06),
    ),
    cms.PSet(
      name=cms.string("gammaEndcapPlus"),
      type=cms.int32(4),
      varType=cms.int32(0),
      etaMin=cms.double(1.479),
      etaMax=cms.double(3.0),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.000600844080846,-0.000200304240073),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.00127931286197,0.000426496218681),
    ),
    cms.PSet(
      name=cms.string("gammaEndcapMinus"),
      type=cms.int32(4),
      varType=cms.int32(0),
      etaMin=cms.double(-3.0),
      etaMax=cms.double(-1.479),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.00099687418264,0.000332552504717),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-5.91610970401e-05,1.97383604799e-05),
    ),
    cms.PSet(
      name=cms.string("hHFPlus"),
      type=cms.int32(6),
      varType=cms.int32(0),
      etaMin=cms.double(2.901376),
      etaMax=cms.double(5.2),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.00942379669813,5.27047469034e-06),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00155562765723,2.25597261998e-06),
    ),
    cms.PSet(
      name=cms.string("hHFMinus"),
      type=cms.int32(6),
      varType=cms.int32(0),
      etaMin=cms.double(-5.2),
      etaMax=cms.double(-2.901376),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.000271591035289,5.4311907648e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-4.45253628997e-05,8.90492850332e-06),
    ),
    cms.PSet(
      name=cms.string("egammaHFPlus"),
      type=cms.int32(7),
      varType=cms.int32(0),
      etaMin=cms.double(2.901376),
      etaMax=cms.double(5.2),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.000266832143945,5.33663703791e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(6.65158044281e-05,-1.33026190645e-05),
    ),
    cms.PSet(
      name=cms.string("egammaHFMinus"),
      type=cms.int32(7),
      varType=cms.int32(0),
      etaMin=cms.double(-5.2),
      etaMax=cms.double(-2.901376),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(9.5187858459e-05,-1.90375963235e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(7.28374209815e-06,-1.45692410286e-06),
    ),
)