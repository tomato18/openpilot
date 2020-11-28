# flake8: noqa

from cereal import car
from selfdrive.car import dbc_dict
Ecu = car.CarParams.Ecu

# Steer torque limits
class SteerLimitParams:
  def __init__(self, CP):
    self.STEER_MAX = 384
    self.STEER_DELTA_UP = 3
    self.STEER_DELTA_DOWN = 7
    self.STEER_DRIVER_ALLOWANCE = 50
    self.STEER_DRIVER_MULTIPLIER = 2
    self.STEER_DRIVER_FACTOR = 1


class CAR:
  #HYUNDAI
  ELANTRA = "HYUNDAI ELANTRA LIMITED ULTIMATE 2017"
  ELANTRA_GT_I30 = "HYUNDAI I30 N LINE 2019 & GT 2018 DCT"
  HYUNDAI_GENESIS = "HYUNDAI GENESIS 2015-2016"
  IONIQ_HEV = "HYUNDAI IONIQ HYBRID PREMIUM 2018-2020"
  IONIQ_EV_LTD = "HYUNDAI IONIQ ELECTRIC LIMITED 2019"
  KONA = "HYUNDAI KONA 2020"
  KONA_EV = "HYUNDAI KONA ELECTRIC 2019"
  KONA_HEV = "HYUNDAI KONA HEV 2019"
  SANTA_FE_2017 = "HYUNDAI SANTA FE 2017"
  SANTA_FE = "HYUNDAI SANTA FE LIMITED 2019"
  SONATA = "HYUNDAI SONATA 2020"
  SONATA_2019 = "HYUNDAI SONATA 2019"
  SONATA_HEV_2019 = "HYUNDAI SONATA HEV 2019"
  SONATA_HEV = "HYUNDAI SONATA HYBRID 2020"
  PALISADE = "HYUNDAI PALISADE 2020"
  GRANDEUR = "GRANDEUR IG 2017"
  GRANDEUR_HEV = "GRANDEUR IG HEV 2019"
  VELOSTER = "HYUNDAI VELOSTER 2019"

  # GENESIS
  GENESIS_G70 = "GENESIS G70 2018"
  GENESIS_G80 = "GENESIS G80 2017-2020"
  GENESIS_G90 = "GENESIS G90 2017-2020"

  # KIA
  KIA_FORTE = "KIA FORTE E 2018"
  KIA_OPTIMA = "KIA OPTIMA SX 2019 & 2016"
  KIA_OPTIMA_HEV = "KIA OPTIMA HYBRID 2017 & SPORTS 2019"
  KIA_SORENTO = "KIA SORENTO GT LINE 2018"
  KIA_STINGER = "KIA STINGER GT2 2018"
  KIA_NIRO_EV = "KIA NIRO EV 2020 PLATINUM"
  KIA_NIRO_HEV = "KIA NIRO HEV 2018"
  KIA_CEED = "KIA CEED 2019"
  KIA_SPORTAGE = "KIA SPORTAGE S 2020"
  KIA_CADENZA = "KIA K7 2016-2019"
  KIA_CADENZA_HEV = "KIA K7 HEV 2016-2019"
  
class Buttons:
  NONE = 0
  RES_ACCEL = 1
  SET_DECEL = 2
  GAP_DIST = 3
  CANCEL = 4

FINGERPRINTS = {
  CAR.IONIQ_EV_LTD: [{
    127: 8, 304: 8, 320: 8, 339: 8,
  },
  {
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 7,
  }],
  CAR.IONIQ_HEV: [{
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1173: 8, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1322: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  }],
}

ECU_FINGERPRINT = {
  Ecu.fwdCamera: [832, 1156, 1191, 1342]
}

# Don't use these fingerprints for fingerprinting, they are still used for ECU detection
IGNORED_FINGERPRINTS = [CAR.IONIQ_HEV]

FW_VERSIONS = {
  CAR.SONATA: {
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x8756310L0010\x00\xf1\x00DN8 MDPS C 1.00 1.01 56310L0010\x00 4DNAC101\xf1\xa01.01',
      b'\xf1\x8756310-L0010\xf1\x00DN8 MDPS C 1.00 1.01 56310-L0010 4DNAC101\xf1\xa01.01',
    ],
  },
  CAR.SONATA_HEV: {
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x8756310-L5500\xf1\x00DN8 MDPS C 1.00 1.02 56310-L5500 4DNHC102\xf1\xa01.02',
    ],
  },
  CAR.SANTA_FE: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409'],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x81606EA051\x00\x00\x00\x00\x00\x00\x00\x00'],
  },
  CAR.KIA_STINGER: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00CK  MDPS R 1.00 1.04 57700-J5420 4C4VL104'],
  },
  CAR.KIA_OPTIMA_HEV: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00DE  MDPS C 1.00 1.09 56310G5301\x00 4DEHC109',],
  },
  CAR.PALISADE: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00LX2 MDPS C 1.00 1.03 56310-S8020 4LXDC103',],
  },
  CAR.VELOSTER: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00JSL MDPS C 1.00 1.03 56340-J3000 8308', ],
  },
  CAR.KIA_NIRO_EV: {
    (Ecu.eps, 0x7D4, None): [
      b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4000\x00 4DEEC105',
      b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4100\x00 4DEEC105',
    ],
  },
  CAR.KONA_EV: {
    (Ecu.eps, 0x7D4, None): [
      b'\xf1\x00OS  MDPS C 1.00 1.04 56310K4000\x00 4OEDC104',
      b'\xf1\x00OS  MDPS C 1.00 1.04 56310K4050\x00 4OEDC104',
    ],

  },
  CAR.IONIQ_HEV: {
    (Ecu.eps, 0x7D4, None): [
      b'\xf1\x00AE  MDPS C 1.00 1.07 56310/G2301 4AEHC107',
      b'\xf1\x00AE  MDPS C 1.00 1.01 56310/G2310 4APHC101',
    ],
  },
  CAR.IONIQ_EV_LTD: {
    (Ecu.eps, 0x7D4, None): [
      b'\xf1\x00AE  MDPS C 1.00 1.01 56310/G7560 4APEC101',
    ],
  },
  CAR.GENESIS_G70: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00IK__ SCC F-CUP      1.00 1.02 96400-G9100         \xf1\xa01.02', ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x81640F0051\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\xf1\x81640L0051\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x00IK  MDPS R 1.00 1.06 57700-G9420 4I4VL106', 
      b'\xf1\x00IK  MDPS R 1.00 1.08 57700-G9220 4I2VL108',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00IK  MFC  AT USA LHD 1.00 1.01 95740-G9000 170920', ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x87VDJLT17895112DN4\x88fVf\x99\x88\x88\x88\x87fVe\x88vhwwUFU\x97eFex\x99 \xff\xb7\x82\xf1\x81E25\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E25\x00\x00\x00\x00\x00\x00\x00SIK0T33NB2\x11\x1am\xda',
      b'\xf1\x87VCJLP18488832DN3\x88uXf\x88vgf\x97eVe\x98fhw\x88eWevUEUgu\xff\xfbW\xf1\x81E25\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E25\x00\x00\x00\x00\x00\x00\x00SIK0T33NB4\xecE\xefL',
    ],
  },
  CAR.KONA: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00OS  MDPS C 1.00 1.05 56310J9030\x00 4OSDC105', ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00OS  MDPS C 1.00 1.05 56310/J9030 4OSDC105', ],
  },
  CAR.KIA_OPTIMA: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409'],
    (Ecu.engine, 0x7e0, None): [b'\x01TJFAJNU06F201H03'],
  },  
}

CHECKSUM = {
  "crc8": [CAR.SANTA_FE, CAR.SONATA, CAR.SONATA_HEV, CAR.PALISADE],
  "6B": [CAR.KIA_SORENTO, CAR.HYUNDAI_GENESIS],
}

FEATURES = {
  # which message has the gear
  "use_cluster_gears": set([CAR.Ioniq_HEV, CAR.SANTA_FE_2017, CAR.ELANTRA, CAR.KONA, CAR.ELANTRA_GT_I30, CAR.KIA_CADENZA, CAR.KIA_NIRO_HEV, CAR.GRANDEUR]),
  "use_tcu_gears": set([CAR.KIA_OPTIMA, CAR.SONATA_2019, CAR.VELOSTER]),

  # send LFA MFA message for new HKG models
  "send_lfa_mfa": set([CAR.SONATA, CAR.PALISADE, CAR.SONATA_HEV, CAR.SANTA_FE, CAR.KIA_NIRO_EV, CAR.KONA_EV, CAR.KONA,
                       CAR.KONA_HEV, CAR.IONIQ_HEV, CAR.IONIQ_EV_LTD]),

  "allow_high_steer": set([CAR.KONA, CAR.KONA_EV, CAR.KONA_HEV, CAR.KIA_NIRO_EV]),
}

ELEC_VEH = set([CAR.IONIQ_EV_LTD, CAR.KONA_EV, CAR.KIA_NIRO_EV])

HYBRID_VEH = set([CAR.KIA_OPTIMA_HEV, CAR.SONATA_HEV_2019, CAR.SONATA_HEV, CAR.IONIQ_HEV, CAR.KIA_CADENZA_HEV, CAR.GRANDEUR_HEV, CAR.KIA_NIRO_HEV, CAR.KONA_HEV])

DBC = {
  CAR.ELANTRA: dbc_dict('hyundai_kia_generic', None),
  CAR.ELANTRA_GT_I30: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G70: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G80: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G90: dbc_dict('hyundai_kia_generic', None),
  CAR.HYUNDAI_GENESIS: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.IONIQ_EV_LTD: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.SANTA_FE_2017: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTA_FE: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.SONATA_2019: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_HEV_2019: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.GRANDEUR: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.PALISADE: dbc_dict('hyundai_kia_generic', None),
  CAR.VELOSTER: dbc_dict('hyundai_kia_generic', None),

  CAR.KIA_FORTE: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_OPTIMA: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_OPTIMA_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.KIA_SORENTO: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_STINGER: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_SPORTAGE: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_CEED: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_NIRO_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_NIRO_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.KIA_CADENZA: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_CADENZA_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
}

STEER_THRESHOLD = 150
