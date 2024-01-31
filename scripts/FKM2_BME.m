function [shape] = FKM2_BME(phi, theta, L)

kappa = (theta * pi)./(180 * L);
phi = phi * pi / 180;

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
