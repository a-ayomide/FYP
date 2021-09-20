#Namespace AppConstants
class AppConstants(object):

    def manufacturerModels(self, model):
        #return the manufacturer manufacturerModels
        manufacturers = ['ABUS', 'ACTI', 'ActiveCam', 'Arecont', 'Avigilon', 'Axis',
        'Beward', 'BOLID', 'BOSCH', 'CONVISION', 'Dahua', 'Dallmeier', 'Digital Watchdog',
        'Divisat', 'DSSL', 'DVTEL', 'Eneo', 'EVS', 'Evidence', 'FLIR', 'GeoVison']
        pair_manufacturer_models = {
            'ABUS': {'﻿HDCC31500': '1/3', 'HDCC32501': '1/3', 'HDCC32560': '1/3', 'HDCC33500': '1/3', 'HDCC35500': '1/2.7',
                    'HDCC41500': '1/3', 'HDCC42501': '1/3', 'HDCC42560': '1/3', 'HDCC43500': '1/3', 'HDCC45500': '1/2.7',
                    'HDCC62500': '1/3', 'HDCC62550': '1/3'},
            'ACTI': {'A22': '1/1.8', 'A24': '1/1.8', 'A310': '1/3', 'A312': '1/2.7', 'A416': '1/3', 'A42': '1/1.8'},
            'ActiveCam': {'AC-D1020': '1/2.7', 'AC-D1120SWD': '1/2.7', 'AC-D1140': '1/3', 'AC-D1140S': '1/3', 'AC-D2101IR3': '1/4'},
            'Arecont': {'AV10005': '1/2.5', 'AV10115DNAIV1': '1/2.5', 'AV10005DN': '1/2.5', 'AV10115DNv1': '1/2.5', 'AV10115v1': '1/2.5'},
            'Avigilon': {'1.0-H3-B1': '1/3', '1.0-H3-B2': '1/2.7', '1.0-H3-B3': '1/2.7', '1.0-H3-D1': '1/2.7', '1.0-H3-D1-IR': '1/2.7'},
            'Axis': {'AXIS M1045-LW': '1/3', 'AXIS M1065-L': '1/3', 'AXIS M1065-LW': '1/3', 'AXIS M1124': '1/3', 'AXIS M1124 Barebone': '1/2.7'},
            'Beward': {'B1210DM': '1/4', 'B1210R': '1/4', 'B12C': '1/4', 'B12CR': '1/4', 'B12CRW': '1/4', 'B12CW': '1/4'},
            'BOLID': {'VCG-113': '1/4', 'VCG-120': '1/2.7', 'VCG-120-01': '1/2.7', 'VCG-122': '1/3', 'VCG—123': '1/2.7'},
            'BOSCH': {'MIC-7130': '1/3', 'MIC-7130-PB4': '1/3', 'MIC-7130-PG4': '1/3', 'MIC-7130-PW4': '1/3', 'MIC-7230': '1/3'},
            'CONVISION': {'CC-7233': '1/2.7', 'CC-7332': '1/2.7', 'CC-7333': '1/1.8', 'CC-7432': '1/2.7', 'CC7433': '1/1.8'},
            'Dahua': {'22204TNI': '1/2.7', '40212IC': '1/2.7', '40212TNI': '1/2.7', '42212TNI': '1/2.7', '42C212TNI': '1/2.7'},
            'Dallmeier': {'DDF4220HDV': '1/3', 'DDF4520HDV-DN': '1/3', 'DDF4620HDV-DN': '1/3', 'DDF4820HDV-DN': '1/2.5', 'DDF4920HDV-DN': '1/2.5'},
            'Digital Watchdog': {'DWC-MB421T1R': '1/2.7', 'DWC-MB44WiA': '1/3', 'DWC-MB45DiA': '1/1.8', 'DWC-MB721M4TIR': '1/2.7', 'DWC-MB721M8TIR': '1/2.7'},
            'Divisat': {'DVC-D29': '1/4', 'DVC-D292': '1/3.0', 'DVI-D111': '1/4', 'DVI-S121': '1/3.0', 'DVI-S111': '1/4'},
            'DSSL': {'AC-D1120SWD': '1/2.7', 'AC-D1140': '1/3', 'AC-D2123WDZIR6': '1/2.7', 'AC-D2163WDZIR5': '1/3.0', 'AC-D2183WDZIR5': '1/2.5'},
            'DVTEL': {'CB-3011-01-I': '1/3', 'CB-3012-01-I': '1/2.7', 'CB-6208-11-I': '1/1.7', 'CB-4251-00': '1/2.5', 'CB-4221-200': '1/1.7'},
            'Eneo': {'ICB-62M2712M0A': '1/2.7', 'IEB-54F0036M0A': '1/3', 'IEB-78M3611MAA': '1/2.5', 'IEB-73M2712MWA': '1/2.5', 'IED-54F0036MBA': '1/3'},
            'EVS': {'VEC-157-IP-N-2.8-12': '1/3', 'VEC-157-IP-N-5-50': '1/3', 'VEC-257-IP-N-2.8-12': '1/3', 'VEC-557-IP-N-12-40': '1/1.8', 'VES-257-IP-2.8-12-N': '1/3.0'},
            'Evidence': {'Apix-10ZBullet/ S2': '1/1.8', 'Apix-22ZBullet/ S2 SFP': '1/2.7', 'Apix—30ZDome/E3(II)': '1/1.7', 'Apix---Box/E12': '1/1.7', 'Apix – Box /M12 SFP': '1/1.7'},
            'FLIR': {'CB-3102': '1/2.7', 'CB—3304': '1/3.0', 'CB—3308': '1/2.5', 'CM-3102': '1/2.7', 'CM-6206': '1/1.8'},
            'GeoVison': {'EBD4700': '1/3', 'EDR2100-0F': '1/2.8', 'EFD1100-0F': '1/3', 'EFD2100-OF': '1/2.7', 'GV-ABL2702': '1/3'}
        }
        return pair_manufacturer_models[model]

    def sensorsValues(self, sensor):
        sensors_values = {
            #CCD Chip(“): [Horizontal, Vertical]
            '1': [12.8,	9.6],
            '2/3': [8.8, 6.6],
            '1/2': [6.4, 4.8],
            '1/3': [4.8, 3.6],
            '1/4': [3.2, 2.4],
            '1/6': [2.3, 1.73],
            '1/5': [2.8, 2.1],
            '1/3.6': [4.0, 3.0],
            '1/3.2': [4.536, 3.416],
            '1/2.7': [5.371, 4.035],
            '1/2.5': [5.760, 4.290],
            '1/1.8': [7.176, 5.391],
            '1/1.7': [7.6, 5.7]
        }
        return sensors_values[sensor]



    def cableSize(self, current_from_each_machine):
        #return the cable size from a set of defined constants
        cable_values = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95,
        120, 150, 185, 240, 300, 400]
        cable_ranges = [[0, 14], [15, 20], [21, 26], [27, 32], [33, 45],
        [46, 58], [59, 76], [77, 93], [94, 150], [151, 180], [181, 225],
        [226, 260], [261, 290], [291, 340], [341, 400], [401, 460], [461, 520]]
        for i in cable_ranges:
            if i[0] < current_from_each_machine <= i[1]:
                return cable_values[cable_ranges.index(i)]

    def breakerSize(self, current_from_each_machine):
        #return the breaker size from a set of defined constants
        breaker_values = [i for i in range(5, 705, 5)]
        breaker_ranges = [[i-5.5, i-0.5] for i in breaker_values]
        for i in breaker_ranges:
            if i[0] < current_from_each_machine <= i[1]:
                return breaker_values[breaker_ranges.index(i)]

    def breakerType(self, breaker_size):
        breaker_types = ['Miniature Circuit Breaker (MCB)', 'Molded Case Circuit Breaker (MCCB)']
        breaker_sizes = [[5, 100], [105, 2500]]
        for i in breaker_sizes:
            if i[0] <= breaker_size <= i[1]:
                return breaker_types[breaker_sizes.index(i)]


    def lampLumen(self, a):
        data = {
            'Thorn forceLED (120)': 120,
            'Thorn forceLED pro (137)': 137,
            'Tonic Gimbal (100)': 100,
            'HiPak proLED (135)': 135
        }
        return data[a]
