import FWCore.ParameterSet.Config as cms
multPhiCorr_MC_DY_80X = cms.VPSet(
    cms.PSet(
      name=cms.string("hEtaPlus"),
      type=cms.int32(1),
      varType=cms.int32(2),
      etaMin=cms.double(0),
      etaMax=cms.double(2.7),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.00400057331908,2.47680219008e-06),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00217115697144,-2.07024665769e-06),
    ),
    cms.PSet(
      name=cms.string("hEtaMinus"),
      type=cms.int32(1),
      varType=cms.int32(2),
      etaMin=cms.double(-2.7),
      etaMax=cms.double(0),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.0134442925479,2.33274568725e-06),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00187028199748,-2.88857060422e-06),
    ),
    cms.PSet(
      name=cms.string("h0Barrel"),
      type=cms.int32(5),
      varType=cms.int32(2),
      etaMin=cms.double(-1.392),
      etaMax=cms.double(1.392),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.0069313240261,4.73789212497e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.000166679715,-3.91400402057e-05),
    ),
    cms.PSet(
      name=cms.string("h0EndcapPlus"),
      type=cms.int32(5),
      varType=cms.int32(2),
      etaMin=cms.double(1.392),
      etaMax=cms.double(3),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.00556891891153,0.000100668501424),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00975132477255,-2.35379561602e-05),
    ),
    cms.PSet(
      name=cms.string("h0EndcapMinus"),
      type=cms.int32(5),
      varType=cms.int32(2),
      etaMin=cms.double(-3.0),
      etaMax=cms.double(-1.392),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.00285004155378,4.71826125363e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.0186737491992,-0.000124428352497),
    ),
    cms.PSet(
      name=cms.string("gammaBarrel"),
      type=cms.int32(4),
      varType=cms.int32(2),
      etaMin=cms.double(-1.479),
      etaMax=cms.double(1.479),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.00623515275697,3.53715609426e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00785296300166,-4.63561342524e-05),
    ),
    cms.PSet(
      name=cms.string("gammaEndcapPlus"),
      type=cms.int32(4),
      varType=cms.int32(2),
      etaMin=cms.double(1.479),
      etaMax=cms.double(3.0),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.00615185573354,4.21254502028e-05),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(0.00467233055908,6.79159586991e-05),
    ),
    cms.PSet(
      name=cms.string("gammaEndcapMinus"),
      type=cms.int32(4),
      varType=cms.int32(2),
      etaMin=cms.double(-3.0),
      etaMax=cms.double(-1.479),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.0173076475945,0.000158667036921),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.00219488065291,-5.54193473207e-05),
    ),
    cms.PSet(
      name=cms.string("hHFPlus"),
      type=cms.int32(6),
      varType=cms.int32(2),
      etaMin=cms.double(2.901376),
      etaMax=cms.double(5.2),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(-0.000777943507103,-8.63566155857e-06),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.00383640115266,1.72862293643e-06),
    ),
    cms.PSet(
      name=cms.string("hHFMinus"),
      type=cms.int32(6),
      varType=cms.int32(2),
      etaMin=cms.double(-5.2),
      etaMax=cms.double(-2.901376),
      fx=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      px=cms.vdouble(0.00125730229373,2.86569542043e-07),
      fy=cms.string("(x*[p0]+pow(x,2)*[p1])"),
      py=cms.vdouble(-0.00188554965324,-4.78978809735e-07),
    ),
    cms.PSet(
      name=cms.string("egammaHFPlus"),
      type=cms.int32(7),
      varType=cms.int32(2),
      etaMin=cms.double(2.901376),
      etaMax=cms.double(5.2),
      fx=cms.string("((x*(x<100)+100*(x>=100))*[p0]+pow((x*(x<100)+100*(x>=100)),2)*[p1])"),
      px=cms.vdouble(-0.00704851144624,0.000215182880512),
      fy=cms.string("((x*(x<100)+100*(x>=100))*[p0]+pow((x*(x<100)+100*(x>=100)),2)*[p1])"),
      py=cms.vdouble(-0.00236319151202,0.000118154745266),
    ),
    cms.PSet(
      name=cms.string("egammaHFMinus"),
      type=cms.int32(7),
      varType=cms.int32(2),
      etaMin=cms.double(-5.2),
      etaMax=cms.double(-2.901376),
      fx=cms.string("((x*(x<100)+100*(x>=100))*[p0]+pow((x*(x<100)+100*(x>=100)),2)*[p1])"),
      px=cms.vdouble(-0.0037556296941,-8.6578662186e-05),
      fy=cms.string("((x*(x<100)+100*(x>=100))*[p0]+pow((x*(x<100)+100*(x>=100)),2)*[p1])"),
      py=cms.vdouble(-0.00339217998023,8.11368195477e-05),
    ),
)
