function [shape] = IKM(phi0, theta0, l0, dx, dy, dz)
shape_init = FKM_BME(phi0, theta0, l0);

kappa0 = (theta0 * pi)/(180 * l0);

J = [(cos(phi0)*(cos(kappa0*l0) - 1))/kappa0^2 + (l0*sin(kappa0*l0)*cos(phi0))/kappa0,  (sin(phi0)*(cos(kappa0*l0) - 1))/kappa0, sin(kappa0*l0)*cos(phi0); 
     (sin(phi0)*(cos(kappa0*l0) - 1))/kappa0^2 + (l0*sin(kappa0*l0)*sin(phi0))/kappa0, -(cos(phi0)*(cos(kappa0*l0) - 1))/kappa0, sin(kappa0*l0)*sin(phi0); 
                                 (l0*cos(kappa0*l0))/kappa0 - sin(kappa0*l0)/kappa0^2,                                        0,           cos(kappa0*l0)];

d_change = inv(J) * [dx; dy; dz];

kappa = kappa0 + d_change(1);
phi = phi0 + d_change(2);
l = l0 + d_change(3);

% J2 = [(cos(phi0)*(cos(kappa0*l0) - 1))/kappa0^2 + (l0*sin(kappa0*l0)*cos(phi0))/kappa0,  (sin(phi0)*(cos(kappa0*l0) - 1))/kappa0; (sin(phi0)*(cos(kappa0*l0) - 1))/kappa0^2 + (l0*sin(kappa0*l0)*sin(phi0))/kappa0, -(cos(phi0)*(cos(kappa0*l0) - 1))/kappa0; (l0*cos(kappa0*l0))/kappa0 - sin(kappa0*l0)/kappa0^2,                                    0]
% d_change = pinv(J2) * [dx; dy; dz];
% 
% kappa = kappa0 + d_change(1);
% phi = phi0 + d_change(2);
% l = l0;

theta = (kappa * 180 * l) / pi;

shape_final = FKM_BME(phi, theta, l);

disp("Init pose");
disp(shape_init(end, :));
disp("Final pose");
disp(shape_final(end, :));
disp("Difference pose");
disp(shape_final(end, :) - shape_init(end, :));
end