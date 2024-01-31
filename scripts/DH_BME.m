function [T] = DH_BME(phi, kappa, s)

T = [cos(phi)*cos(kappa*s), -sin(phi), sin(kappa*s)*cos(phi), cos(phi)*(1-cos(kappa*s))/kappa;
     sin(phi)*cos(kappa*s), cos(phi), sin(kappa*s)*sin(phi), sin(phi)*(1-cos(kappa*s))/kappa;
     -sin(kappa*s), 0, cos(kappa*s), sin(kappa*s)/kappa;
     0, 0, 0, 1];
end