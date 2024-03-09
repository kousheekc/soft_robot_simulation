function [shape] = FKM_BME(phi, theta, L)

kappa = (theta * pi)/(180 * L);
phi = phi * pi / 180;

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