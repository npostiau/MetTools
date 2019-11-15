import FWCore.ParameterSet.Config as cms
multPhiCorr_Data_2017C = cms.VPSet(
    cms.PSet(
      name=cms.string("hEtaPlus"),
      type=cms.int32(1),
      varType=cms.int32(1),
      etaMin=cms.double(0),
      etaMax=cms.double(2.7),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(0.511533424469,-0.252575887229,-0.000170051326454),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.037513388451,0.177756808034,0.00182955763168),
    ),
    cms.PSet(
      name=cms.string("hEtaMinus"),
      type=cms.int32(1),
      varType=cms.int32(1),
      etaMin=cms.double(-2.7),
      etaMax=cms.double(0),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(0.140495255347,-0.048832483311,0.000348727148456),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.215368354058,0.0366554675416,-0.000408731955873),
    ),
    cms.PSet(
      name=cms.string("h0Barrel"),
      type=cms.int32(5),
      varType=cms.int32(1),
      etaMin=cms.double(-1.392),
      etaMax=cms.double(1.392),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(-0.20790343266,0.00593645741697,5.89576298851e-05),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.0295798864,-0.00842418092032,7.86846805826e-05),
    ),
    cms.PSet(
      name=cms.string("h0EndcapPlus"),
      type=cms.int32(5),
      varType=cms.int32(1),
      etaMin=cms.double(1.392),
      etaMax=cms.double(3),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(0.416411608064,0.0119526389737,0.000140569911604),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.616941333818,0.000193690974622,-0.00027818908841),
    ),
    cms.PSet(
      name=cms.string("h0EndcapMinus"),
      type=cms.int32(5),
      varType=cms.int32(1),
      etaMin=cms.double(-3.0),
      etaMax=cms.double(-1.392),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(-0.116581902313,0.0568965213825,-0.000215399222255),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(0.0901706023508,0.00346422785655,5.4584893659e-05),
    ),
    cms.PSet(
      name=cms.string("gammaBarrel"),
      type=cms.int32(4),
      varType=cms.int32(1),
      etaMin=cms.double(-1.479),
      etaMax=cms.double(1.479),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(0.0402115587669,-0.00215227767202,9.83927666193e-05),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.0796442929682,0.00843438452468,-5.23175561204e-05),
    ),
    cms.PSet(
      name=cms.string("gammaEndcapPlus"),
      type=cms.int32(4),
      varType=cms.int32(1),
      etaMin=cms.double(1.479),
      etaMax=cms.double(3.0),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(-0.0712947916791,0.00815744608564,-0.000356382851739),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.0278832721458,0.00404123868834,-0.000312350708555),
    ),
    cms.PSet(
      name=cms.string("gammaEndcapMinus"),
      type=cms.int32(4),
      varType=cms.int32(1),
      etaMin=cms.double(-3.0),
      etaMax=cms.double(-1.479),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(-0.0323880308842,0.00279041667415,-6.50680084974e-05),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.0344942651691,0.00510176081483,-0.000167176325358),
    ),
    cms.PSet(
      name=cms.string("hHFPlus"),
      type=cms.int32(6),
      varType=cms.int32(1),
      etaMin=cms.double(2.901376),
      etaMax=cms.double(5.2),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(0.159504701489,-0.00531761993634,0.000266581043888),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(-0.00242672814258,0.0558843418675,-0.000365678486664),
    ),
    cms.PSet(
      name=cms.string("hHFMinus"),
      type=cms.int32(6),
      varType=cms.int32(1),
      etaMin=cms.double(-5.2),
      etaMax=cms.double(-2.901376),
      fx=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      px=cms.vdouble(-0.350140822362,0.0878020625577,-0.00035715937605),
      fy=cms.string("([p0]+x*[p1]+pow(x,2)*[p2])"),
      py=cms.vdouble(0.0301815769153,-0.0367613347622,0.00020315716528),
    ),
    cms.PSet(
      name=cms.string("egammaHFPlus"),
      type=cms.int32(7),
      varType=cms.int32(1),
      etaMin=cms.double(2.901376),
      etaMax=cms.double(5.2),
      fx=cms.string("([p0]+(x*(x<100)+100*(x>=100))*[p1]+pow((x*(x<100)+100*(x>=100)),2)*[p2])"),
      px=cms.vdouble(0.0479404265604,0.0273784320026,-0.000219189414884),
      fy=cms.string("([p0]+(x*(x<100)+100*(x>=100))*[p1]+pow((x*(x<100)+100*(x>=100)),2)*[p2])"),
      py=cms.vdouble(0.0140517882008,-0.0211028505362,0.000233922382889),
    ),
    cms.PSet(
      name=cms.string("egammaHFMinus"),
      type=cms.int32(7),
      varType=cms.int32(1),
      etaMin=cms.double(-5.2),
      etaMax=cms.double(-2.901376),
      fx=cms.string("([p0]+(x*(x<100)+100*(x>=100))*[p1]+pow((x*(x<100)+100*(x>=100)),2)*[p2])"),
      px=cms.vdouble(0.286388679758,-0.0281052909227,0.000201120437806),
      fy=cms.string("([p0]+(x*(x<100)+100*(x>=100))*[p1]+pow((x*(x<100)+100*(x>=100)),2)*[p2])"),
      py=cms.vdouble(-0.0451281047561,0.0286482608816,-0.000351933174186),
    ),
)