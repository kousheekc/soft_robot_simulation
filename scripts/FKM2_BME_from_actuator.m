function [shape] = FKM2_BME_from_actuator(da, l1a, l2a, l3a, db, l1b, l2b, l3b)

La = (l1a + l2a + l3a)/3;
phia = atan((sqrt(3)*(l2a+l3a-2*l1a))/(3*(l2a-l3a)));
kappaa = (2*sqrt(l1a^2 + l2a^2 + l3a^2 - l1a*l2a - l1a*l3a - l2a*l3a))/(da * (l1a+l2a+l3a));

Lb = (l1b + l2b + l3b)/3;
phib = atan((sqrt(3)*(l2b+l3b-2*l1b))/(3*(l2b-l3b)));
kappab = (2*sqrt(l1b^2 + l2b^2 + l3b^2 - l1b*l2b - l1b*l3b - l2b*l3b))/(db * (l1b+l2b+l3b));

L = [La, Lb];
phi = [phia, phib];
kappa = [kappaa, kappab];

T01 = [];
T02 = [];
T12 = [];
n = 400;
p1 = [];
p2 = [];

for i=1:n
    s1=(i-1)*L(1)/(n-1);
    T01(:, :, i) = DH_BME(phi(1), kappa(1), s1);
    p1(i, :) = T01(1:3, 4, i);
end

for j=1:n
    s2=(j-1)*L(2)/(n-1);
    T12(:, :, j) = DH_BME(phi(2), kappa(2), s2);
    T02(:, :, j) = T01(:, :, n) * T12(:, :, j);
    p2(j, :) = T02(1:3, 4, j);
end

shape = [p1, p2];
figure(2);
ax = gca;
xlabel('x(m)');
ylabel('y(m)');
zlabel('z(m)');

title('Shape kinematics reconstruction: PCC approach');
hold on,
plot3(p1(:, 1), p1(:, 2), p1(:, 3), '.');
plot3(p2(:, 1), p2(:, 2), p2(:, 3), '.');
grid on,
ax.View = [-60 30];
end
