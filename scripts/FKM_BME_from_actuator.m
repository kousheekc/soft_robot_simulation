function [shape] = FKM_BME_from_actuator(d, l1, l2, l3)
L = (l1 + l2 + l3)/3;
phi = atan((sqrt(3)*(l2+l3-2*l1))/(3*(l2-l3)));
kappa = (2*sqrt(l1^2 + l2^2 + l3^2 - l1*l2 - l1*l3 - l2*l3))/(d * (l1+l2+l3));

T = [];
n = 400;
p = [];

for i=1:n
    s=(i-1)*L/(n-1);
    T(:, :, i) = DH_BME(phi, kappa, s);
    p(i, :) = T(1:3, 4, i);
end

shape = p;
figure(1);
ax = gca;
xlabel('x(m)');
ylabel('y(m)');
zlabel('z(m)');

axis equal;

title('Shape kinematics reconstruction: PCC approach');
hold on,
plot3(p(:, 1), p(:, 2), p(:, 3), '.');
grid on,
ax.View = [-60 30];
end