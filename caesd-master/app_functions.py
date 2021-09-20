import math

#Namspace AmpFunctions
class AmpFunctions(object):
    def __init__(self, load, voltage, growth_factor, derating_factor):
        self.phase_root = math.sqrt(3)
        self.load = load*1000
        self.voltage = voltage
        self.growth_factor = growth_factor
        self.derating_factor = derating_factor

    def ampWithoutFutureExpansion(self):
        return round(self.load/(self.phase_root * self.voltage), 4)

    def ampWithFutureExpansion(self):
        #ampWithoutFutureExpansion = self.ampWithoutFutureExpansion()
        return round(self.ampWithoutFutureExpansion() * self.growth_factor * self.derating_factor, 4)

    def phaseRoot(self):
        return self.phase_root

#Namspace RoomDesign
class RoomDesign(object):
    def __init__(self, length, breadth, working_height, watt_m_sq, lamp_l, no_lumin, main_fac):
        self.length = length
        self.breadth = breadth
        self.working_height = working_height
        self.avg_lumin = watt_m_sq
        self.lamp_l = lamp_l
        self.no_lumin = no_lumin
        self.util_fac = ''
        self.main_fac = main_fac

    def roomArea(self):
        return round(self.length * self.breadth)

    def roomIndex(self):
        return round(self.roomArea() / (self.working_height * (self.length + self.breadth)), 4)

    def utilizationFactor(self):
        #returns a value corresponding to the calculated room index
        util_fac = ''
        if self.roomIndex() <= 0.74:
            util_fac = 'Not Applicable'
        elif 0.75 <= self.roomIndex() <= 0.99:
            util_fac = 0.48
        elif 1.00 <= self.roomIndex() <= 1.24:
            util_fac = 0.49
        elif 1.25 <= self.roomIndex() <= 1.49:
            util_fac = 0.55
        elif 1.50 <= self.roomIndex() <= 1.99:
            util_fac = 0.60
        elif 2.00 <= self.roomIndex() <= 2.49:
            util_fac = 0.66
        elif 2.50 <= self.roomIndex() <= 2.99:
            util_fac = 0.71
        elif 3.00 <= self.roomIndex() <= 3.99:
            util_fac = 0.75
        elif 4.00 <= self.roomIndex() <= 4.99:
            util_fac = 0.80
        elif self.roomIndex() >= 5.00:
            util_fac = 0.83
        return util_fac

    def roomLamps(self):
        self.util_fac = ''
        self.util_fac = self.utilizationFactor()
        if self.util_fac == "Not Applicable":
            room_lamps = round((self.avg_lumin * self.roomArea())/(self.lamp_l * self.no_lumin * self.main_fac))
        else:
            room_lamps = round((self.avg_lumin * self.roomArea())/(self.lamp_l * self.no_lumin * self.util_fac * self.main_fac))
        return room_lamps

    def possibleLampConfigurations(self):
        total_num_lamps = self.roomLamps()
        #least number of combinations
        n = 3
        #generate a list of all the possible numbers from 1 to n
        possible_facs = [i for i in range(1,total_num_lamps+1) if total_num_lamps%i == 0]
        #generate the list of multiplying factors
        multiply_facs = [[i, int(total_num_lamps/i)] for i in possible_facs]
        #m_facs = [str(i)+' by '+str(int(total_num_lamps/i)) for i in p_facs]
        f = int(round(len(multiply_facs)/2))
        div_facs = multiply_facs[0:f]
        if len(div_facs) < n:
            x_facs = [i for i in range(1,total_num_lamps) if (total_num_lamps-1)%i == 0]
            xmultiply_facs = [[i, int((total_num_lamps-1)/i)] for i in x_facs]
            for i in xmultiply_facs[0:int(round(len(xmultiply_facs)/2))]:
                div_facs.append(i)
        #reset all factors with 'x by y' format
        final_facs = [str(i[0])+' by '+str(i[1]) for i in div_facs]
        return ', '.join(final_facs)
