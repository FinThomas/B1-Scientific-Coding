def get_action(self):
    e1 = self.error1
    e2 = self.error2
    controller = self.controller
    Kp = controller[0]
    Kd = controller[1]       #self.controller.Kp         #self.controller.Kd
    action = Kp*e1 + Kd*(e1 - e2)
    return action

