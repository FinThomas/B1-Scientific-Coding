def get_action(self):
    e1 = self.error1
    e2 = self.error2
    Kp = 0.15         #self.controller.Kp
    Kd = 0.6          #self.controller.Kd
    action = Kp*e1 + Kd*(e1 - e2)
    return action

