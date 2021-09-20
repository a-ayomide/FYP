#GUI classes for the application
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

#Window.size = (1200, 800)

#FUNCTION classes for the application
from app_functions import AmpFunctions, RoomDesign
from app_constants import AppConstants

class SelectableLabel(RecycleDataViewBehavior, Label):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        self.selected = True
        ''' Catch and handle the view changes '''
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        action = CAESD()
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            machine_data = """
        Machine Section: %s
        Machine Name: %s
        Machine Load: %s
        Machine Current: %sA
        Machine Current(fx): %sA
        Machine Cable Size: %smm2
        Machine Breaker Size: %sA
        Machine Cable Type: Armoured PVC Insulated Single Core Cable
        Machine Breaker Type: %s
            """ % (str(rv.data[index]['machine_section']),
            str(rv.data[index]['machine_name']),
            str(rv.data[index]['machine_load']),
            str(rv.data[index]['machine_amp']),
            str(rv.data[index]['machine_amp_gd']),
            str(rv.data[index]['cable_size']),
            str(rv.data[index]['breaker_size']),
            str(rv.data[index]['breaker_type']))
            action.popDisplays('Machine Details', machine_data)

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''

#Screens
class LaunchPage(Screen):
    pass

class CctvPage(Screen):
    dropManufacturer = ObjectProperty()
    dropModel = ObjectProperty()
    dropSensor = ObjectProperty()
    distFromCamera = ObjectProperty()
    sceneWidth = ObjectProperty()
    sceneHeight = ObjectProperty()
    sceneArea = ObjectProperty()
    focalLength = ObjectProperty()
    datastore = {
        'Manu_Model_pairs': [],
        'Manufacturer': '',
        'Model': '',
        'Sensor': '',
        'Distance': '',
        'Width': '',
        'Height': '',
        'Focal': '',
        'Area': ''
    }
    def selectedManufacturer(self):
        self.datastore['Manufacturer'] = self.dropManufacturer.text
        self.datastore['Manu_Model_pairs'] = AppConstants().manufacturerModels(self.dropManufacturer.text)
        self.dropModel.values = [i for i in self.datastore['Manu_Model_pairs'].keys()]
        pass
    def selectedModel(self):
        if self.dropModel.text != 'Model':
            self.datastore['Model'] = self.dropModel.text
            self.datastore['Sensor'] = self.datastore['Manu_Model_pairs'][self.dropModel.text]
            self.dropSensor.text = 'Sensor format: '+ self.datastore['Sensor']+'"'
            self.sensor_values = AppConstants().sensorsValues(self.datastore['Sensor'])
    def checkManufacturerModelSelected(self):
        if self.dropManufacturer.text != "" and self.dropModel.text != 'Model':
            return True
    def clearValues(self):
        if self.sceneWidth.text == '':
            self.sceneHeight.text = ''
            self.focalLength.text = ''
            self.sceneArea.text = ''
        elif self.sceneHeight.text == '':
            self.sceneWidth.text = ''
            self.focalLength.text = ''
            self.sceneArea.text = ''
    def calculateSceneDimensions(self, dimension, value):
        app = CAESD()
        if value != '':
            if self.checkManufacturerModelSelected():
                if self.distFromCamera.focus:
                    self.datastore['Distance'] = self.distFromCamera.text
                    if self.sceneWidth.text == '' or self.sceneHeight.text == '':
                        pass
                    else:
                        self.focalLength.text = str(round((float(self.sensor_values[0])*float(self.distFromCamera.text))/float(self.sceneWidth.text), 1))
                        self.sceneArea.text = str(round(float(self.sceneWidth.text)*float(self.sceneHeight.text), 2))
                elif self.sceneWidth.focus:
                    self.datastore['Height'] = ''
                    self.datastore['Width'] = self.sceneWidth.text
                    self.sceneHeight.text = str(round((float(self.sceneWidth.text)*float(self.sensor_values[1]))/float(self.sensor_values[0]), 1))
                    if self.distFromCamera.text != '':
                        self.focalLength.text = str(round((float(self.sensor_values[0])*float(self.distFromCamera.text))/float(self.sceneWidth.text), 1))
                    self.sceneArea.text = str(round(float(self.sceneWidth.text)*float(self.sceneHeight.text), 2))
                elif self.sceneHeight.focus:
                    self.datastore['Width'] = ''
                    self.datastore['Height'] = self.sceneHeight.text
                    self.sceneWidth.text = str(round((float(self.sceneHeight.text)*float(self.sensor_values[0]))/float(self.sensor_values[1]), 1))
                    if self.distFromCamera.text != '':
                        self.focalLength.text = str(round((float(self.sensor_values[1])*float(self.distFromCamera.text))/float(self.sceneHeight.text), 1))
                    self.sceneArea.text = str(round(float(self.sceneHeight.text)*float(self.sceneWidth.text), 2))
                else:
                    pass
            else:
                errorMessage = 'Please select the Model'
                app.popDisplays('Application Error', errorMessage)
        else:
            if self.distFromCamera.text == '':
                self.focalLength.text = ''
                self.clearValues()
            else:
                self.clearValues()

class EarthingPage(Screen):
    pass

class PowerPage_one(Screen):
    numMachines = ObjectProperty()
    numSections = ObjectProperty()
    normalVoltage: ObjectProperty()
    utilityVoltage: ObjectProperty
    growthFactor: ObjectProperty()
    deratingFactor: ObjectProperty()
    loadingFactor: ObjectProperty()
    dispPowerOneError: ObjectProperty()
    buttAddMachines: ObjectProperty()
    def calculatePowerInputs(self, machines, sections):
        if machines:
            if sections:
                self.buttAddMachines.disabled = False
                PowerPage_two().powerdataApp(machines, sections, self.normalVoltage.text, self.utilityVoltage.text, self.growthFactor.text, self.deratingFactor.text)
            else:
                CAESD().displayInLabelMessage(self.dispPowerOneError, t='Please Indicate Number of Sections', i=True)
        else:
            CAESD().displayInLabelMessage(self.dispPowerOneError, t='Please Indicate Number of Machines', i=True)

class PowerPage_two(Screen):
    machineOutOfNum = ObjectProperty()
    machineNameName = ObjectProperty()
    machineNameInput = ObjectProperty()
    machineLoad = ObjectProperty
    machineFactor = ObjectProperty()
    dropSelectMachineSection = ObjectProperty()
    dispPowerTwoScreen = ObjectProperty()
    buttAddMachines = ObjectProperty()
    buttAllMachines = ObjectProperty()
    dropViewMachineSection = ObjectProperty()
    dispMachineListHeader = ObjectProperty()
    dispMachineScreen = ObjectProperty()

    num_of_machines_and_sections = []
    storageMachineData = []

    def addMachineParameters(self, machine_name, load, section_selected):
        if machine_name:
            if load:
                if section_selected != 'Select Machine Section':
                    CAESD().displayInLabelMessage(self.dispPowerTwoScreen, t='', i=True)
                    self.buttAllMachines.disabled = False
                    self.dropViewMachineSection.disabled = False
                    self.dispMachineListHeader.disabled = False
                    if int(self.getCurMachineNumber()) == int(self.num_of_machines_and_sections[0]):
                        self.machineListLabels()
                        self. displayPowerViewboard()
                        self.buttAddMachines.disabled = True
                        self.dropSelectMachineSection.disabled = True
                        out_message = "Complete!!! "+str(int(self.getCurMachineNumber()))+" out of "+str(self.num_of_machines_and_sections[0])+" machines added!"
                        CAESD().displayInLabelMessage(self.machineOutOfNum, t=out_message)
                    else:
                        self.machineListLabels()
                        self. displayPowerViewboard()
                        self.machineNameName.text = "Name for Machine "+str(int(self.getCurMachineNumber())+1)
                        self.machineNameInput.text = "Machine "+str(int(self.getCurMachineNumber()))
                        out_message =str(int(self.getCurMachineNumber())-1)+" out of "+str(self.num_of_machines_and_sections[0])+" machines added!"
                        CAESD().displayInLabelMessage(self.machineOutOfNum, t=out_message, c=[0,0,0,1])
                        self.machineLoad.text = ''
                        self.dropSelectMachineSection.text = 'Select Machine Section'
                else:
                    CAESD().displayInLabelMessage(self.dispPowerTwoScreen, t='Please Select A Machine Section', i=True)
            else:
                CAESD().displayInLabelMessage(self.dispPowerTwoScreen, t='Please Indicate Machine Load', i=True)
        else:
            CAESD().displayInLabelMessage(self.dispPowerTwoScreen, t='Please Indicate Machine Name', i=True)

    def powerdataApp(self, machines, sections, a, b, c, d):
        self.num_of_machines_and_sections.append(machines)
        self.num_of_machines_and_sections.append(sections)
        self.num_of_machines_and_sections.append([a,b,c,d])

    def getCurMachineNumber(self):
        return self.machineNameName.text.split(' ')[3]

    def selectMachineSection(self):
        values = []
        section_alt = [chr(i) for i in range(65,91)]
        for i in range(1, int(self.num_of_machines_and_sections[1])+1):
            values.append('Section  '+str(section_alt[i-1]))
        self.dropSelectMachineSection.values = values
        self.dropViewMachineSection.values = values
        #self.buttMachineSection.values = values

    def machineListLabels(self):
        ampCal = AmpFunctions(float(self.machineLoad.text),
                            float(self.num_of_machines_and_sections[2][0]),
                            float(self.num_of_machines_and_sections[2][2]),
                            float(self.num_of_machines_and_sections[2][3]))
        appCons = AppConstants()
        self.storageMachineData.insert(0, {  'machine_section': str(self.dropSelectMachineSection.text),
                                                'machine_name': str(self.machineNameInput.text),
                                                'machine_load': str(self.machineLoad.text),
                                                'machine_amp': str(ampCal.ampWithoutFutureExpansion()),
                                                'machine_amp_gd': str(ampCal.ampWithFutureExpansion()),
                                                'breaker_size': str(appCons.breakerSize(ampCal.ampWithFutureExpansion())),
                                                'cable_size': str(appCons.cableSize(ampCal.ampWithoutFutureExpansion())),
                                                'breaker_type': str(appCons.breakerType(appCons.breakerSize(ampCal.ampWithFutureExpansion())))})
        self.dispMachineScreen.data = self.storageMachineData

    def machineSectionLabels(self, sections, data):
        self.dispMachineSection.data = []
        values = []
        section_alt = [chr(i) for i in range(65,91)]
        for i in range(1, int(sections)+1):
            values.append('Section  '+str(section_alt[i-1]))
        values.reverse()
        for sect in values:
            section_data = []
            for row in data:
                if row['machine_section'] == sect:
                    section_data.append(row)
            formatted_data = ['Machine  | Load  |  Amp  |\n']+[i['machine_name']+'  |  '+i['machine_load']+'kVa  |  '+i['machine_amp']+'A  |  \n' for i in section_data]
            #section_header = 'Machine Name  | Machine Load  |\n'
            #formatted_data(section_header)

            self.dispMachineSection.data.insert(0, {'machine_section_name': str(sect), 'machine_section_data': str(''.join(formatted_data))})

    def displayPowerViewboard(self):
        ampCal = AmpFunctions(float(self.machineLoad.text),
                            float(self.num_of_machines_and_sections[2][0]),
                            float(self.num_of_machines_and_sections[2][2]),
                            float(self.num_of_machines_and_sections[2][3]))
        #Determine the total current
        all_currents = []
        for i in self.dispMachineScreen.data:
            all_currents.append(float(i['machine_amp']))
        t_current = round(sum(all_currents), 2)

        #Determine the transformer capacity
        p_current = (float(self.num_of_machines_and_sections[2][0]) * t_current)/float(self.num_of_machines_and_sections[2][1])
        t_capacity =  round((ampCal.phaseRoot() * float(self.num_of_machines_and_sections[2][1]) * p_current * 1)/1000, 2)
        power_viewboard_message = """
POWER VIEWBOARD
Total Current from Machines: %sA
Change Over Switch Capacity: 2500A
Transformer Capacity: %skVA
Generator Capacity: %skVA
        """ % (t_current, t_capacity, t_capacity)
        self.dispPowerTwoScreen.text = power_viewboard_message

    def displayPanelBoard(self, data_key):
        if data_key == 'All Machines':
            self.dispMachineScreen.data = self.storageMachineData
            #self.sectionViewboard.text = ''
        else:
            section_data = []
            self.dispMachineScreen.data = []
            for row in self.storageMachineData:
                if row['machine_section'] == data_key:
                    section_data.append(row)
                else:
                    self.dispMachineScreen.data = []
            self.dispMachineScreen.data = section_data

            if self.dispMachineScreen.data == []:
                out_message = 'NO MACHINE ADDED YET FOR '+data_key.upper()
                CAESD().displayInLabelMessage(self.dispPowerTwoScreen, t=out_message, c=[0,0,0,1])
            else:
                tot_load = 0
                tot_amp = 0
                tot_amp_gd = 0
                tot_breaker_size = 0
                #tot_cable_size = 0
                for i in self.dispMachineScreen.data:
                    tot_load += float(i['machine_load'])
                    tot_amp += float(i['machine_amp'])
                    tot_amp_gd += float(i['machine_amp_gd'])
                    tot_breaker_size += float(i['breaker_size'])
                    #tot_cable_size += float(i['cable_size'])
                data_summary = """
    SUMMARY FOR %s
    Number of Machines: %s
    Total Load: %skVA
    Total Current: %sA
    Total Current(fx): %sA
    Total Breaker Size: %sA
                """ % (data_key.upper(), len(self.dispMachineScreen.data), tot_load, round(tot_amp, 2), round(tot_amp_gd, 2), round(tot_breaker_size, 2))
                self.dispPowerTwoScreen.text = data_summary

class IlluminationPage(Screen):
    lengthOfRoom = ObjectProperty()
    breadthOfRoom = ObjectProperty()
    workingHeight = ObjectProperty()
    wattMSq = ObjectProperty()
    lampL = ObjectProperty()
    numL = ObjectProperty()
    mainFac = ObjectProperty()
    dispIllumination = ObjectProperty()
    dispLampDistributions = ObjectProperty()
    def calculateLampsNeeded(self, length, breadth, w_height, watt_m_sq, lamp_l, no_lumin, main_fac):
        app = CAESD()
        if length and breadth and watt_m_sq and lamp_l:
            if lamp_l != 'Lamp lumen':
                if main_fac != 'Maintenance factor':
                    Ll = AppConstants().lampLumen(str(self.lampL.text))
                    room = RoomDesign(float(self.lengthOfRoom.text),
                                    float(self.breadthOfRoom.text),
                                    float(self.workingHeight.text),
                                    float(self.wattMSq.text),
                                    float(Ll),
                                    float(self.numL.text),
                                    float(self.mainFac.text))
                    message_illumination = """
Room Index Calculated at: %s \r
Total Number of lamps needed: %s
                        """ % (str(room.roomIndex()), str(room.roomLamps()))
                    lamp_dis = """
POSSIBLE COMBINATIONS OF LAMPS\r
%s
                    """ % str(room.possibleLampConfigurations())
                    app.displayInLabelMessage(self.dispIllumination, t=message_illumination, c=[0,0,0,1])
                    app.displayInLabelMessage(self.dispLampDistributions, t=lamp_dis, c=[0,0,0,1])
                else:
                    app.displayInLabelMessage(self.dispIllumination, t='Please select the maintenance factor', i=True)
            else:
                app.displayInLabelMessage(self.dispIllumination, t='Please choose the lamp lumen', i=True)
        else:
            app.displayInLabelMessage(self.dispIllumination, t='Missing Parameter/Input', i=True)

#Main Screen Manager
class CAESDApp(ScreenManager):
    pass

main_kv = Builder.load_file("main.kv")
class CAESD(App):
    def build(self):
        self.title = 'Computer Aided Electrical Services Design'
        self.background_color = 0,0,0,1
        return main_kv

    def displayInLabelMessage(self, obj, **kwargs):
        obj.color = 1, 0, 0, 1
        obj.italic = False
        if kwargs == {}:
            #Default error message
            obj.text = 'Attention: Application Message'
        else:
            for i in kwargs.keys():
                if i == 'text' or i == 't':
                    obj.text = kwargs[i]
                elif i == 'color' or i == 'c':
                    obj.color = kwargs[i]
                elif i == 'italic' or i == 'i':
                    obj.italic = kwargs[i]

    def popDisplays(self, title, message, hint=(.7, .45)):
        Popup(title=title, title_color=[1,1,1,1],
                content=Label(text=message),
                size_hint=hint,
                separator_color=[1,1,0,.6]).open()

if __name__ == '__main__':
    CAESD().run()
