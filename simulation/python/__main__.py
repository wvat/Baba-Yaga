import numpy as np
import matplotlib.pyplot as plt
import control as ctl

def main():
    # define parameters
    mh = 0.5 # upper chassis com
    ml = 1.5 # lower chassis com (centered on wheel axis)
    r = 0 # TODO unused in this version
    L = 1
    d1 = 0.01
    d2 = 0.01
    g = 9.82

    # create state-space model
    A = np.array([[0, 0, 1, 0],
                 [0, 0, 0, 1], 
                 [0,  g*(mh/ml), -d1/ml, -d2/(L*ml)],
                 [0, g*(ml+mh)/(L*ml), -d1/(L*ml), -d2*(ml+mh)/(L**2 * ml * mh)]])
    B = np.array([0, 0, 1/ml, 1/(L*ml)])
    C = np.array([0, 1, 0, 0])
    D = 0

    sys = ctl.StateSpace(A,B.T,C,D)

    # plot functions
    sys.display()
#    sys.eigplot()

    # design controller


if __name__ == "__main__":
    main()
    