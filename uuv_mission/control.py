def get_action(self):
    e1 = self.error1
    e2 = self.error2
    Kp = 5           #self.controller.Kp
    Kd = 5          #self.controller.Kd
    action = Kp*e1 + Kd*(e1 - e2)
    return action

