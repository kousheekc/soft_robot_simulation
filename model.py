import numpy as np

class Model:
    def __init__(self, d1, d2, init_pos):
        self.d1 = d1
        self.d2 = d2

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
        p1, p2 = self.FKM2_actuators(self.d1, self.d2, self.current_pos["l1a"], self.current_pos["l1b"], self.current_pos["l1c"], self.current_pos["l2a"], self.current_pos["l2b"], self.current_pos["l2c"])
        return p1, p2

    def DH(self, phi, kappa, s):
        T = np.array([
            [np.cos(phi) * np.cos(kappa * s), -np.sin(phi), np.sin(kappa * s) * np.cos(phi), np.cos(phi) * (1 - np.cos(kappa * s)) / kappa],
            [np.sin(phi) * np.cos(kappa * s), np.cos(phi), np.sin(kappa * s) * np.sin(phi), np.sin(phi) * (1 - np.cos(kappa * s)) / kappa],
            [-np.sin(kappa * s), 0, np.cos(kappa * s), np.sin(kappa * s) / kappa],
            [0, 0, 0, 1]
        ])
        return T
    
    def FKM_actuators(self, d, l1, l2, l3):
        n = 400
        T = np.empty((n, 4, 4))
        p = np.empty((n, 3))

        if (l1 == l2 == l3):
            p = np.array([
                [0, 0, 0],
                [0, 0, l1]
            ])
        else:
            L = (l1 + l2 + l3) / 3
            phi = np.arctan2(np.sqrt(3) * (l2 + l3 - 2 * l1) , 3 * (l2 - l3))
            kappa = (2 * np.sqrt(l1**2 + l2**2 + l3**2 - l1*l2 - l1*l3 - l2*l3)) / (d * (l1 + l2 + l3))

            for i in range(n):
                s = (i - 1) * L / (n - 1)
                T[i, :, :] = self.DH(phi, kappa, s)
                p[i, :] = T[i, :3, 3]

        return p
    
    def FKM2_actuators(self, d1, d2, l1a, l1b, l1c, l2a, l2b, l2c):
        n = 400
        T01 = np.zeros((n, 4, 4))
        T02 = np.empty((n, 4, 4))
        T12 = np.empty((n, 4, 4))
        p1 = np.empty((n, 3))
        p2 = np.empty((n, 3))

        L1 = (l1a + l1b + l1c) / 3
        phi1 = np.arctan2(np.sqrt(3) * (l1b + l1c - 2 * l1a), 3 * (l1b - l1c))
        kappa1 = (2 * np.sqrt(l1a**2 + l1b**2 + l1c**2 - l1a * l1b - l1a * l1c - l1b * l1c)) / (d1 * (l1a + l1b + l1c))

        for i in range(n):
            s1 = (i - 1) * L1 / (n - 1)
            T01[i, :, :] = self.DH(phi1, kappa1, s1)
            p1[i, :] = T01[i, :3, 3]

        L2 = (l2a + l2b + l2c) / 3
        phi2 = np.arctan2(np.sqrt(3) * (l2b + l2c - 2 * l2a), 3 * (l2b - l2c))
        kappa2 = (2 * np.sqrt(l2a**2 + l2b**2 + l2c**2 - l2a * l2b - l2a * l2c - l2b * l2c)) / (d2 * (l2a + l2b + l2c))

        for j in range(n):
            s2 = (j - 1) * L2 / (n - 1)
            T12[j, :, :] = self.DH(phi2, kappa2, s2)
            T02[j, :, :] = np.dot(T01[n-1, :, :], T12[j, :, :])
            p2[j, :] = T02[j, :3, 3]

        return p1, p2
