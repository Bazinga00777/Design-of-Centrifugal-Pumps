import math

class details():
    import math


    def __init__(self):
        self.suction_lift = "suction lift"


    def enter_details(self):
        self.suction_lift = int(input("Enter the suction lift(in m)[Hs]\n"))
        self.delivery_lift = int(input("Enter the delivery lift(in m)[Hd]\n"))
        self.length_suction= int(input("Enter the length of suction pipe(in m)[Ls]\n"))
        self.length_delivery = int(input("Enter the length of delivery pipe(in m)[Ld]\n"))
        self.discharge = int(input("Enter the discharge(in lpm)\n"))

    def act_discharge(self):
        self.actual_discharge = float( (self.discharge * 0.001 / 60) / 0.96)
        print("STEP 1 : Calculation of Actual Discharge")
        print(f"The actual discharge is {self.actual_discharge} m3/sec")

    def suc_del_pipe(self):
        self.suction_pipe = round(math.sqrt(self.actual_discharge * 4 / 3.14) * 1000,4 )
        self.delivery_pipe = round(math.sqrt((self.actual_discharge * 2) / 3.14) * 1000 ,4)
        print("STEP 2: Calculation of Inlet & Outlet pipe diameter")
        print(f"The diameter of suction pipe is {self.suction_pipe}mm")
        print(f"The diameter of delivery pipe is {self.delivery_pipe}mm")

    def suc_head(self):
        print("STEP 3 : Elimination of losses")
        self.suction_valve_head = 0.8 * 1
        self.suction_bend_head = 0.2 * 1
        self.suction_velocity_head = 1 / (2 * 9.8)
        self.suction_friction_head = ( 2 / 9.8 ) * (0.001 / self.suction_pipe) * 1000
        self.suction_head =  self.suction_lift + self.suction_friction_head + self.suction_bend_head + self.suction_valve_head + self.suction_velocity_head
        print(f"The suction head is {self.suction_head}m")



    def del_head(self):
        self.delivery_valve_head = 0.8 * 1
        self.delivery_bend_head = 0.2 * 1
        self.delivery_velocity_head = 1 / 9.8
        self.delivery_friction_head = ( 2 / 9.8 ) * (0.001 / self.delivery_pipe) * 10000000
        self.delivery_head = self.delivery_valve_head + self.delivery_bend_head + self . delivery_friction_head + self.delivery_velocity_head
        print(f"The delivery head is {self.delivery_head}m")

    def mano_head(self):
        self.manometric_head = self.suction_head + self.delivery_head
        print(f"The manometric head is {self.manometric_head}m")

    def NPSH(self):
        self.NPSH = 10.34 - self.manometric_head - 2.31
        print(f"The NPSH value is {self.NPSH}")
        print("Since the value is negative the centrifugal pump is not cavitation free")

    def motor_power(self):
        print("STEP 4 : Calculation of Motor Power")
        self.water_power = (1000 * self.actual_discharge * 9.81 * self.manometric_head) / 1000
        print("Considering Overall Efficiency as 80%")
        self.motor_power = self.water_power / 0.80
        print(f"The motor power is {self.motor_power} Kw")

    def specific_speed(self):
        print("STEP 5 : Selection of Specific Speed")
        self.specific_speed_960 = 960 * ( math.sqrt(self.actual_discharge) / (self.manometric_head ** (3/4)))
        print(f"Selecting N = 960 rpm, we get the specific speed as {self.specific_speed_960} rpm ")
        self.specific_speed_1440 = 1440 * (math.sqrt(self.actual_discharge) / (self.manometric_head ** (3/4)))
        print(f"Selecting N = 1440 rpm, we get the specific speed as {self.specific_speed_1440} rpm ")
        print("Selecting AC motor with power as 7.5 Kw")

    def des_of_imp(self):
        print("STEP 6 : Design of Impeller")
        self.u_2 = 1 * math.sqrt( 2 * 9.8 * self.manometric_head)
        self.d_2 = (self.u_2 * 60000) / (math.pi * 1440)
        print(f"The outside diameter of impeller is {self.d_2} mm")
        print("Considering Radial vane flow area")
        self.d_1 = self.d_2 / 4
        print(f"The inner diameter of impeller is {self.d_1} mm")

    def shroud_baseplate(self):
        print("STEP 7 : Design of Shroud and Baseplate")
        self.u_1 = math.pi * (self.d_1) * (1440 / 60000)
        self.β_1 = math.atan( 2 / self.u_1) * (180 / 3.14)
        print(f"The value of β1 is {self.β_1} degrees")
        self.Vw_2 = (self.manometric_head * 9.81) / self.u_2
        print(f"The value of Vw2 is {self.Vw_2} m/s")
        print("Calculation of flow velocity at exit")
        print("Considering High Specific speed, Ψ = 0.25")
        self.Vf_2 = 0.25 * math.sqrt( 2 * 9.81 * self.manometric_head)
        print(f"The value of Vf2 is {self.Vf_2} m/s")
        self.β_2 = math.atan(self.Vf_2 / (self.u_2 - self.Vw_2)) * (180 / 3.14)
        print(f"The value of β2 is {self.β_2} degrees")
        self.α_2 = math.atan(self.Vf_2 / self.Vw_2) * (180 / 3.14)
        print(f"The value of α2 is {self.α_2} degrees ")

    def number_of_shroud(self):
        print("STEP 7 : Calulation of number of shrouds")
        self.number_of_shroud = 6.5 * (self.d_2 + self.d_1) * math.degrees(math.sin (self.β_1 + self.β_2)/2) / (self.d_2 - self.d_1)
        print(self.number_of_shroud)

    def design_of_casing(self):
        print("STEP 9: Design of Casing")
        print("Considering Dd = 100")
        self.d_t = 0.8 * 100
        self.theta = 0
        for i in range(7):
            self.theta += 30
            self.d_θ = self.d_t *  math.sqrt(self.theta)









