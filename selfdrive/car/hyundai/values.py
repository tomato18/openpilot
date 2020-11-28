from cereal import car
from selfdrive.car import dbc_dict
Ecu = car.CarParams.Ecu

# Steer torque limits
class SteerLimitParams:
  STEER_MAX = 384   # 409 is the max, 255 is stock
  STEER_DELTA_UP = 3
  STEER_DELTA_DOWN = 7
  STEER_DRIVER_ALLOWANCE = 50
  STEER_DRIVER_MULTIPLIER = 2
  STEER_DRIVER_FACTOR = 1

class CAR:
  # hyundai
  ELANTRA = "HYUNDAI ELANTRA LIMITED ULTIMATE 2017"
  ELANTRA_GT_I30 = "HYUNDAI I30 N LINE 2019 & GT 2018 DCT"
  GENESIS_G80 = "GENESIS G80 2017"
  GENESIS_G90 = "GENESIS G90 2017"
  HYUNDAI_GENESIS = "HYUNDAI GENESIS 2015-2016"
  KONA = "HYUNDAI KONA 2019"
  KONA_EV = "HYUNDAI KONA ELECTRIC 2019"
  KONA_HEV = "HYUNDAI KONA HEV 2019"
  SANTA_FE = "HYUNDAI SANTA FE LIMITED 2019"
  SANTA_FE_1 = "HYUNDAI SANTA FE has no scc"
  SONATA = "HYUNDAI SONATA 2020"
  SONATA_2019 = "HYUNDAI SONATA 2019"
  SONATA_H = "HYUNDAI SONATA HYBRID 2020"
  PALISADE = "HYUNDAI PALISADE 2020"
  IONIQ = "HYUNDAI IONIQ HYBRID PREMIUM 2017"
  IONIQ_EV_LTD = "HYUNDAI IONIQ ELECTRIC LIMITED 2019"
  GRANDEUR = "GRANDEUR IG 2017"
  GRANDEUR_HEV = "GRANDEUR IG HEV 2019"
  # kia
  KIA_FORTE = "KIA FORTE E 2018"
  KIA_OPTIMA = "KIA OPTIMA SX 2019 & 2016"
  KIA_OPTIMA_H = "KIA OPTIMA HYBRID 2017 & SPORTS 2019"
  KIA_SORENTO = "KIA SORENTO GT LINE 2018"
  KIA_STINGER = "KIA STINGER GT2 2018"
  KIA_NIRO_EV = "KIA NIRO EV 2020 PLATINUM"
  KIA_NIRO_HEV = "KIA NIRO HEV 2018"
  KIA_CEED = "KIA CEED 2019"
  KIA_SPORTAGE = "KIA SPORTAGE S 2020"
  KIA_CARDENZA = "KIA K7 2016-2019"
  KIA_CARDENZA_HEV = "KIA K7 HEV 2016-2019"
  
class Buttons:
  NONE = 0
  RES_ACCEL = 1
  SET_DECEL = 2
  GAP_DIST = 3
  CANCEL = 4

FINGERPRINTS = {
  # hyundai
  CAR.IONIQ: [{
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1173: 8, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1322: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
    }],
  CAR.KIA_CARDENZA_HEV: [{
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576: 8, 593: 8, 688: 5, 832: 8, 865: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1096: 8, 1102: 8, 1108: 8, 1136: 6, 1138: 5, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1210: 8, 1227: 8, 1265: 4, 1268: 8, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1343: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1379: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
    }],
}

ECU_FINGERPRINT = {
  Ecu.fwdCamera: [832, 1156, 1191, 1342]
}
FW_VERSIONS = {
  CAR.SONATA: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00DN8_ SCC FHCUP      1.00 1.00 99110-L0000         ',
      b'\xf1\x00DN8_ SCC F-CU-      1.00 1.00 99110-L0000         ',
    ],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x8758910-L0100\xf1\x00DN ESC \x06 104\x19\x08\x01 58910-L0100\xf1\xa01.04'],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x87391162M003\xf1\xa0000F'],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x8756310L0010\x00\xf1\x00DN8 MDPS C 1.00 1.01 56310L0010\x00 4DNAC101\xf1\xa01.01',
      b'\xf1\x8756310-L0010\xf1\x00DN8 MDPS C 1.00 1.01 56310-L0010 4DNAC101\xf1\xa01.01',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00DN8 MFC  AT USA LHD 1.00 1.00 99211-L0000 190716',
      b'\xf1\x00DN8 MFC  AT USA LHD 1.00 1.01 99211-L0000 191016',
    ],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x00bcsh8p54  U903\x00\x00\x00\x00\x00\x00SDN8T16NB0z{\xd4v'],
  },
  CAR.SANTA_FE: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00TM__ SCC F-CUP      1.00 1.02 99110-S2000         \xf1\xa01.02'],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x00TM ESC \x02 100\x18\x030 58910-S2600\xf1\xa01.00',],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x81606EA051\x00\x00\x00\x00\x00\x00\x00\x00'],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409'],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00TM  MFC  AT USA LHD 1.00 1.00 99211-S2000 180409'],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x87SBJWAA6562474GG0ffvgeTeFx\x88\x97\x88ww\x87www\x87w\x84o\xfa\xff\x87fO\xff\xc2 \xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM2G24NS1\x00\x00\x00\x00'],
  },
  CAR.KIA_STINGER: {
    (Ecu.fwdRadar, 0x7d0, None): [ b'\xf1\x00CK__ SCC F_CUP      1.00 1.01 96400-J5100         \xf1\xa01.01'],
    (Ecu.engine, 0x7e0, None): [ b'\xf1\x81640E0051\x00\x00\x00\x00\x00\x00\x00\x00',],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00CK  MDPS R 1.00 1.04 57700-J5420 4C4VL104'],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00CK  MFC  AT USA LHD 1.00 1.03 95740-J5000 170822'],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x87VDHLG17118862DK2\x8awWwgu\x96wVfUVwv\x97xWvfvUTGTx\x87o\xff\xc9\xed\xf1\x81E21\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E21\x00\x00\x00\x00\x00\x00\x00SCK0T33NB0\x88\xa2\xe6\xf0'],
  },
  CAR.KIA_OPTIMA_H: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00DEhe SCC H-CUP      1.01 1.02 96400-G5100         ',],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x816H6F4051\x00\x00\x00\x00\x00\x00\x00\x00',],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00DE  MDPS C 1.00 1.09 56310G5301\x00 4DEHC109',],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00DEP MFC  AT USA LHD 1.00 1.01 95740-G5010 170424',],
    (Ecu.transmission, 0x7e1, None): [b"\xf1\x816U3J2051\x00\x00\xf1\x006U3H0_C2\x00\x006U3J2051\x00\x00PDE0G16NS2\xf4'\\\x91",],
  },
  CAR.PALISADE: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00LX2_ SCC FHCUP      1.00 1.04 99110-S8100         \xf1\xa01.04',],
    (Ecu.esp, 0x7d1, None): [
      b'\xf1\x00LX ESC \x0b 102\x19\x05\x07 58910-S8330',
      b'\xf1\x00LX ESC \v 102\x19\x05\a 58910-S8330\xf1\xa01.02',
    ],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x81640J0051\x00\x00\x00\x00\x00\x00\x00\x00',],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00LX2 MDPS C 1.00 1.03 56310-S8020 4LXDC103',],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00LX2 MFC  AT USA LHD 1.00 1.03 99211-S8100 190125',],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x87LDKVBN424201KF26\xba\xaa\x9a\xa9\x99\x99\x89\x98\x89\x99\xa8\x99\x88\x99\x98\x89\x88\x99\xa8\x89v\x7f\xf7\xffwf_\xffq\xa6\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB2\xafL]\xe7',],
  },
  CAR.KIA_NIRO_EV: {
    (Ecu.fwdRadar, 0x7D0, None): [
      b'\xf1\x00DEev SCC F-CUP      1.00 1.03 96400-Q4100         \xf1\xa01.03',
      b'\xf1\x00DEev SCC F-CUP      1.00 1.00 99110-Q4000         \xf1\xa01.00',      
    ],
    (Ecu.esp, 0x7D1, None): [
      b'\xf1\xa01.06',
      b'\xf1\xa01.07',      
    ],
    (Ecu.eps, 0x7D4, None): [
      b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4000\x00 4DEEC105',
      b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4100\x00 4DEEC105',
    ],
    (Ecu.fwdCamera, 0x7C4, None): [
      b'\xf1\x00DEE MFC  AT USA LHD 1.00 1.03 95740-Q4000 180821',
      b'\xf1\x00DEE MFC  AT EUR LHD 1.00 1.00 99211-Q4000 191211',
    ],
  },
  CAR.KONA_EV: {
    (Ecu.fwdRadar, 0x7D0, None): [b'\xf1\x00OSev SCC FNCUP      1.00 1.01 99110-K4000        \xf1\xa01.01'],
    (Ecu.esp, 0x7D1, None): [b'\xf1\xa02.06'],
    (Ecu.eps, 0x7D4, None): [b'\xf1\x00OS  MDPS C 1.00 1.04 56310K4000\x00 4OEDC104'],
    (Ecu.fwdCamera, 0x7C4, None): [b'\xf1\x00OSE LKAS AT KOR LHD 1.00 1.00 95740-K4100 W40'],
  },
}

CHECKSUM = {
  "crc8": [CAR.SANTA_FE, CAR.SANTA_FE_1, CAR.SONATA, CAR.PALISADE, CAR.SONATA_H],
  "6B": [CAR.KIA_SORENTO, CAR.HYUNDAI_GENESIS],
}

FEATURES = {
  # Use Cluster for Gear Selection, rather than Transmission
  "use_cluster_gears": [CAR.IONIQ, CAR.ELANTRA, CAR.KONA, CAR.ELANTRA_GT_I30, CAR.KIA_CARDENZA, CAR.KIA_NIRO_HEV, CAR.GRANDEUR],     
  # Use TCU Message for Gear Selection
  "use_tcu_gears": [CAR.KIA_OPTIMA, CAR.SONATA_2019],                                    
  # Use E_GEAR Message for Gear Selection
  "use_elect_gears": [CAR.KIA_OPTIMA_H, CAR.IONIQ_EV_LTD, CAR.KONA_EV, CAR.SONATA_H, CAR.KIA_NIRO_EV, CAR.KIA_CARDENZA_HEV, CAR.GRANDEUR_HEV],
  # Use E_EMS11 Message for Gas and Brake for Hybrid/ELectric
  "use_elect_ems": [CAR.SONATA_H, CAR.IONIQ_EV_LTD, CAR.KIA_NIRO_EV, CAR.KONA_EV],
  # send LFA MFA message for new HKG models
  "send_lfa_mfa": [CAR.SONATA, CAR.PALISADE, CAR.SONATA_H, CAR.SANTA_FE, CAR.KIA_NIRO_EV],
  "has_scc13": [], 
  "has_scc14": [], 
}

DBC = {
  CAR.ELANTRA: dbc_dict('hyundai_kia_generic', None),
  CAR.ELANTRA_GT_I30: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G80: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G90: dbc_dict('hyundai_kia_generic', None),
  CAR.HYUNDAI_GENESIS: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_EV_LTD: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTA_FE: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTA_FE_1: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_H: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_2019: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.PALISADE: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_FORTE: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_OPTIMA: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_OPTIMA_H: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_SORENTO: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_STINGER: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_SPORTAGE: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_CEED: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_NIRO_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_NIRO_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_CARDENZA: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_CARDENZA_HEV: dbc_dict('hyundai_kia_generic', None),
}

STEER_THRESHOLD = 150
