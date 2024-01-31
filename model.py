import numpy as np

class Model:
    def __init__(self, d, init_pos):
        self.d = d
        self.current_pos = {
            "l1a": init_pos[0],
            "l1b": init_pos[1],
            "l1c": init_pos[2],
            "l2a": init_pos[3],
            "l2b": init_pos[4],
            "l2c": init_pos[5],
        }

    def update(self, axis, new_val):
        self.current_pos[axis] = new_val
        p = self.FKM_actuators(self.d, self.current_pos["l1a"], self.current_pos["l1b"], self.current_pos["l1c"])
        return p

    def DH(self, phi, kappa, s):
        T = np.array([
            [np.cos(phi) * np.cos(kappa * s), -np.sin(phi), np.sin(kappa * s) * np.cos(phi), np.cos(phi) * (1 - np.cos(kappa * s)) / kappa],
            [np.sin(phi) * np.cos(kappa * s), np.cos(phi), np.sin(kappa * s) * np.sin(phi), np.sin(phi) * (1 - np.cos(kappa * s)) / kappa],
            [-np.sin(kappa * s), 0, np.cos(kappa * s), np.sin(kappa * s) / kappa],
            [0, 0, 0, 1]
        ])
        return T
    
    def FKM_actuators(self, d, l1, l2, l3):
        if (l1 == l2 == l3):
            p = np.array([
                [0, 0, 0],
                [0, 0, l1]
            ])
        else:
            L = (l1 + l2 + l3) / 3
            phi = np.arctan2(np.sqrt(3) * (l2 + l3 - 2 * l1) , 3 * (l2 - l3))
            kappa = (2 * np.sqrt(l1**2 + l2**2 + l3**2 - l1*l2 - l1*l3 - l2*l3)) / (d * (l1 + l2 + l3))

            T = np.zeros((4, 4, 400))
            n = 400
            p = np.zeros((n, 3))

            for i in range(n):
                s = (i - 1) * L / (n - 1)
                T[:, :, i] = self.DH(phi, kappa, s)
                p[i, :] = T[0:3, 3, i]

        return p
