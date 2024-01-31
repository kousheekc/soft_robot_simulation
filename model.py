import numpy as np

class Model:
    def DH(self, phi, kappa, s):
        T = np.array([
            [np.cos(phi) * np.cos(kappa * s), -np.sin(phi), np.sin(kappa * s) * np.cos(phi), np.cos(phi) * (1 - np.cos(kappa * s)) / kappa],
            [np.sin(phi) * np.cos(kappa * s), np.cos(phi), np.sin(kappa * s) * np.sin(phi), np.sin(phi) * (1 - np.cos(kappa * s)) / kappa],
            [-np.sin(kappa * s), 0, np.cos(kappa * s), np.sin(kappa * s) / kappa],
            [0, 0, 0, 1]
        ])
        return T
    
    def FKM_actuators(self, d, l1, l2, l3):
        L = (l1 + l2 + l3) / 3
        phi = np.arctan((np.sqrt(3) * (l2 + l3 - 2 * l1)) / (3 * (l2 - l3)))
        kappa = (2 * np.sqrt(l1**2 + l2**2 + l3**2 - l1*l2 - l1*l3 - l2*l3)) / (d * (l1 + l2 + l3))

        phi = phi * np.pi / 180

        T = np.zeros((4, 4, 400))
        n = 400
        p = np.zeros((n, 3))

        for i in range(n):
            s = (i - 1) * L / (n - 1)
            T[:, :, i] = self.DH(phi, kappa, s)
            p[i, :] = T[0:3, 3, i]

        return p
