import inputs
import time
import numpy as np
import matplotlib.pyplot as plt

pads = inputs.devices.gamepads

if len(pads) == 0:
    raise Exception("Couldn't find any Gamepads!")

t_end = time.time() + 2
x = []
while time.time() < t_end:
    events = inputs.get_gamepad()
    for event in events:
        x_hat = event.state
        # if x_hat > 7000                     :
        # x.append(x_hat)
        print('??????????????????????')
        # print(event.ev_type)
        # print(2)
        # print(event.code)
        # print(3)
        # print(event.state)
        print(type(event))
        print('########################')
x = np.array(x)
plt.plot(np.arange(x.shape[0]), x)
plt.show()