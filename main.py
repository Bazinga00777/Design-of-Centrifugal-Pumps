import math
from details import details

details = details()



input_details = details.enter_details()
theoretical_discharge = details.act_discharge()
suc_del_pipe = details.suc_del_pipe()
suc_head = details.suc_head()
del_head = details.del_head()
mano_head = details.mano_head()
Npsh = details.NPSH()
motor_power = details.motor_power()
specfic_speed = details.specific_speed()
design_of_impeller = details.des_of_imp()
shroud_baseplate = details.shroud_baseplate()
number_of_shroud = details.number_of_shroud()
design_of_casing = details.design_of_casing()

