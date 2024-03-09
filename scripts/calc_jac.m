syms phi kappa l

f = [(cos(phi)*(1-cos(kappa*l)))/kappa;
     (sin(phi)*(1-cos(kappa*l)))/kappa;
     sin(kappa*l)/kappa];

J = jacobian(f, [kappa, phi, l])

