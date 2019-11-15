import FWCore.ParameterSet.Config as cms
multPhiCorr_Data_2018C = cms.VPSet(
    cms.PSet(
      name=cms.string("hEtaPlus"),
      type=cms.int32(1),
      varType=cms.int32(1),
      etaMin=cms.double(0),
      etaMax=cms.double(2.7),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(-0.319020192291,0.289753400074,0.000548844956799),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.237117800146,0.178884784641,0.000350082394684),
    ),
    cms.PSet(
      name=cms.string("hEtaMinus"),
      type=cms.int32(1),
      varType=cms.int32(1),
      etaMin=cms.double(-2.7),
      etaMax=cms.double(0),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(-0.324352655552,0.105707023818,0.00058379420455),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(0.128353079328,-0.00514201160596,0.000204277823589),
    ),
    cms.PSet(
      name=cms.string("h0Barrel"),
      type=cms.int32(5),
      varType=cms.int32(1),
      etaMin=cms.double(-1.392),
      etaMax=cms.double(1.392),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(-1.03276695319,-0.0167837535375,-6.80979503446e-05),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.0917061230738,0.00971095834587,-0.000142082296047),
    ),
    cms.PSet(
      name=cms.string("h0EndcapPlus"),
      type=cms.int32(5),
      varType=cms.int32(1),
      etaMin=cms.double(1.392),
      etaMax=cms.double(3),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(0.0364592635295,0.00561892959759,-0.000158441007711),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.0436021561897,-0.00266238498662,-2.61496724047e-05),
    ),
    cms.PSet(
      name=cms.string("h0EndcapMinus"),
      type=cms.int32(5),
      varType=cms.int32(1),
      etaMin=cms.double(-3.0),
      etaMax=cms.double(-1.392),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(0.310833533685,0.036817046609,-0.000250717068056),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.821181938796,-0.0598092986564,0.000322827946006),
    ),
    cms.PSet(
      name=cms.string("gammaBarrel"),
      type=cms.int32(4),
      varType=cms.int32(1),
      etaMin=cms.double(-1.479),
      etaMax=cms.double(1.479),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(0.127914534468,-0.00823650653211,-0.000145951172552),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.212287573016,0.0104038346212,-7.17989435234e-05),
    ),
    cms.PSet(
      name=cms.string("gammaEndcapPlus"),
      type=cms.int32(4),
      varType=cms.int32(1),
      etaMin=cms.double(1.479),
      etaMax=cms.double(3.0),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(-0.00856473544528,0.00100682961959,-3.25261967175e-05),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.0478486436756,-2.99007796033e-05,-0.000128454435137),
    ),
    cms.PSet(
      name=cms.string("gammaEndcapMinus"),
      type=cms.int32(4),
      varType=cms.int32(1),
      etaMin=cms.double(-3.0),
      etaMax=cms.double(-1.479),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(0.0585459716022,-0.000514801377615,6.011034959e-05),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.0840557112222,0.00321144908421,-0.000187266067533),
    ),
    cms.PSet(
      name=cms.string("hHFPlus"),
      type=cms.int32(6),
      varType=cms.int32(1),
      etaMin=cms.double(2.901376),
      etaMax=cms.double(5.2),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(0.131786402486,0.073798239646,4.61935674977e-05),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(0.0145456096004,0.034273091761,-0.000206590356404),
    ),
    cms.PSet(
      name=cms.string("hHFMinus"),
      type=cms.int32(6),
      varType=cms.int32(1),
      etaMin=cms.double(-5.2),
      etaMax=cms.double(-2.901376),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(-0.325928623356,0.131346148994,-0.000556002342306),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.0237442690985,-0.0414069808048,0.000397737789883),
    ),
    cms.PSet(
      name=cms.string("egammaHFPlus"),
      type=cms.int32(7),
      varType=cms.int32(1),
      etaMin=cms.double(2.901376),
      etaMax=cms.double(5.2),
      fx=cms.string("([p0]+(x*(x<100)+100*(x>=100))*[p1]+pow((x*(x<100)+100*(x>=100)),2)*[p2])"),
      px=cms.vdouble(0.234551721229,0.0179541919525,-0.000175787566765),
      fy=cms.string("([p0]+(x*(x<100)+100*(x>=100))*[p1]+pow((x*(x<100)+100*(x>=100)),2)*[p2])"),
      py=cms.vdouble(-0.0687230894194,-0.0171942927497,0.000201689345652),
    ),
    cms.PSet(
      name=cms.string("egammaHFMinus"),
      type=cms.int32(7),
      varType=cms.int32(1),
      etaMin=cms.double(-5.2),
      etaMax=cms.double(-2.901376),
      fx=cms.string("([p0]+(x*(x<100)+100*(x>=100))*[p1]+pow((x*(x<100)+100*(x>=100)),2)*[p2])"),
      px=cms.vdouble(0.380542547916,-0.0390333729263,0.000353007948753),
      fy=cms.string("([p0]+(x*(x<100)+100*(x>=100))*[p1]+pow((x*(x<100)+100*(x>=100)),2)*[p2])"),
      py=cms.vdouble(-0.0331470425428,0.0265303671532,-0.000320405884949),
    ),
)