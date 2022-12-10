clc
close all;
clear all;
warning off;
%% Definition of lab parameters

% Parameters of the no lineal system
A = 10;
As = 1;
g = 9.8;
Q = 2;
k = As*sqrt(2*g);

IncH2=0.2;
IncQ=2;
% Definition of the operational point

x0_ini=[2*XX  XX]; %% Define h1 and h2 of the set-point

%% Exercices

%% 2.3 Reglas de sintonía sin tener en cuenta el nivel de robustez

K = XX; % Ganancia del proceso 
tau = XX; % Constante de tiempo del proceso
L = XX; % Retardo del proceso

P_tf = tf(XX,[XX XX],'InputDelay',L); %% Definir la función de transferencia del proceso 
tsim=60;
T = tau;
sim('ctrl_systems_2',tsim);

figure(1)
plot(time, model_proc, 'r', time, real_proc, 'g');
title('Model vs Real process')
legend('Lineal model', 'Real Process');
xlabel('Time')
ylabel('Level')
grid on

pause;
%% 2.3.1 Obtención de los parámetros del controlador

% PID tuning Ziegler-Nichols

Kp_zn=XX; %% Expresión del término de ganancia de Ziegler Nichols
Ti_zn=XX; %% Expresión del término de tiempo integral de Ziegler Nichols
Td_zn=XX; %% Expresión del término de tiempo derivativo de Ziegler Nichols

% PID tuning Servo

A=XX; B=XX; %% Constantes PID Kp servo
Kp_servo = XX; %% Expresión del término de ganancia Servo 

A=XX; B=XX;  %% Constantes PID Ti Servo
Ti_servo=XX; %% Expresión del término integral Servo

A=XX; B=XX; %% Constantes PID Td Servo
Td_servo=XX; %% Expresión del término derivativo Servo


% PID tuning Regulation

A=XX; B=XX; %% Constantes PID Kp regulación
Kp_regulation=XX; %% Expresión del término ganancia Regulación

A=XX; B=XX; %% Constantes PID Ti regulación
Ti_regulation=XX; %% Expresión del término integral Regulación

A=XX; B=XX; %% Constantes PID Td regulación
Td_regulation=XX; %% Expresión del término derivativo Regulación

pause;

%% 2.3.2 Simulación del sistema de control lineal

IncH2=XX; %% Cambio en referencia
IncQ=XX; %% Perturbación

tsim=60;

Kp = XX; %% ganancia Ziegler-Nichols
Ti = XX; %% tiempo integral Ziegler-Nichols
Td = XX; %% tiempo derivativo Ziegler-Nichols
sim('control_pid_lineal',tsim);

output_zn = y_lin; %% Salida del controlador Ziegler-Nichols
ref_zn = ref_lin; %% Referencia del controlador Ziegler-Nichols
perturbacion_zn = per_lin; %% Perturbación del controlador Ziegler-Nichols
cont_zn = controller_lin; %% Señal generada por el controlador Ziegler-Nichols
IAE_zn = IAE_lin; %% Vector de IAE, solo nos interesa el valor final
time_zn = time.signals.values;

Kp = XX; %% ganancia Servo
Ti = XX; %% tiempo integral Servo
Td = XX; %% tiempo derivativo Servo
sim('control_pid_lineal',tsim);

output_servo = y_lin; %% Salida del controlador Servo
ref_servo = ref_lin; %% Referencia del controlador Servo
perturbacion_servo = per_lin; %% Perturbación del controlador Servo
cont_servo = controller_lin; %% Señal generada por el controlador Servo
IAE_servo = IAE_lin; %% Vector de IAE, solo nos interesa el valor final
time_servo = time.signals.values;

Kp = XX; %% ganancia Regulación
Ti = XX; %% tiempo integral Regulación
Td = XX; %% tiempo derivativo Regulación
sim('control_pid_lineal',tsim);

output_regulacion = y_lin; %% Salida del controlador Regulación
ref_regulacion = ref_lin; %% Referencia del controlador Regulación
perturbacion_regulacion = per_lin; %% Perturbación del controlador Regulación
cont_regulacion = controller_lin; %% Señal generada por el controlador Regulación
IAE_regulacion = IAE_lin; %% Vector de IAE, solo nos interesa el valor final
time_regulacion = time.signals.values;

figure(2)
subplot(2,1,1)
plot(time_zn, ref_zn, 'k');
hold on
plot(time_zn, output_zn, 'r');
plot(time_servo, output_servo, 'b')
plot(time_regulacion, output_regulacion, 'g')
grid on

title('Tuning techniques comparison')
legend('Reference', 'Ziegler-Nichols', 'Servo', 'Regulation');
xlabel('Time')
ylabel('Level')

subplot(2,1,2)
plot(time_zn, cont_zn, 'r');
hold on
plot(time_servo, cont_servo, 'b');
plot(time_regulacion, cont_regulacion, 'g');
grid on

title('Output PID Controller')
legend('Ziegler-Nichols', 'Servo', 'Regulation');
xlabel('Time')
ylabel('Level')

pause;

%% 2.3.3 Simulación del sistema de control no-lineal

IncH2=XX; %% Cambio en referencia
IncQ=XX; %% Perturbación

tsim=60;

Kp = XX; %% ganancia Ziegler-Nichols
Ti = XX; %% tiempo integral Ziegler-Nichols
Td = XX; %% tiempo derivativo Ziegler-Nichols
sim('control_pid_nolineal',tsim);

output_zn_nolin = y_nolin.signals.values; %% Salida del controlador Ziegler-Nichols
ref_zn_nolin = ref_nolin.signals.values; %% Referencia del controlador Ziegler-Nichols
cont_zn_nolin = controller_nolin.signals.values; %% Señal generada por el controlador Ziegler-Nichols
IAE_zn_nolin = IAE_nolin; %% Vector de IAE, solo nos interesa el valor final
time_zn = ref_nolin.time;

Kp = XX; %% ganancia Servo
Ti = XX; %% tiempo integral Servo
Td = XX; %% tiempo derivativo Servo
sim('control_pid_nolineal',tsim);

output_servo_nolin = y_nolin.signals.values; %% Salida del controlador Servo
ref_servo_nolin = ref_nolin.signals.values; %% Referencia del controlador Servo
cont_servo_nolin = controller_nolin.signals.values; %% Señal generada por el controlador Servo
IAE_servo_nolin = IAE_nolin; %% Vector de IAE, solo nos interesa el valor final
time_servo = ref_nolin.time;

Kp = XX; %% ganancia Regulación
Ti = XX; %% tiempo integral Regulación
Td = XX; %% tiempo derivativo Regulación
sim('control_pid_nolineal',tsim);

output_regulacion_nolin = y_nolin.signals.values; %% Salida del controlador Regulación
ref_regulacion_nolin = ref_nolin.signals.values; %% Referencia del controlador Regulación
cont_regulacion_nolin = controller_nolin.signals.values; %% Señal generada por el controlador Regulación
IAE_regulacion_nolin = IAE_nolin; %% Vector de IAE, solo nos interesa el valor final
time_reg = ref_nolin.time;

figure(3)
subplot(2,1,1)
plot(time_servo, ref_servo_nolin, 'k');
hold on
plot(time_zn, output_zn_nolin, 'r');
plot(time_servo, output_servo_nolin, 'b')
plot(time_reg, output_regulacion_nolin, 'g')
grid on

title('Tuning techniques comparison - Nolineal')
legend('Reference', 'Ziegler-Nichols', 'Servo', 'Regulation');
xlabel('Time')
ylabel('Level')

subplot(2,1,2)
plot(time_zn, cont_zn_nolin, 'r');
hold on
plot(time_servo, cont_servo_nolin, 'b');
plot(time_reg, cont_regulacion_nolin, 'g');
grid on

title('Output PID Controller - Nolineal system')
legend('Ziegler-Nichols', 'Servo', 'Regulation');
xlabel('Time')
ylabel('Level')

pause;
%% 2.3.4 Comparación de prestaciones

% Comparación con perturbación y salto en referencia a la vez

IncH2=XX;
IncQ=XX;

tsim=60;
sim('comparacion',tsim);

figure(4)
plot(time, ref+x0_ini(2), 'k')
hold on 
plot(time, y_l_zn + x0_ini(2), 'r')
plot(time, y_nl_zn, 'g')
title('Ziegler-Nichols PID controller')
legend('Reference','Lineal Model','No-linel model')
grid on

% Comparación solo con cambio en referencia
IncH2=XX; %% Cambio en referencia
IncQ=XX; %% Perturbación

tsim=60;
sim('comparacion',tsim);

IAE_l_reg = [IAE_l_zn(end) IAE_l_regulacion(end) IAE_l_servo(end)]; % Creación del vector de IAEs para los controladores del systema lineal
IAE_nl_reg = [IAE_nl_zn(end) IAE_nl_regulacion(end) IAE_nl_servo(end)]; % Creación del vector de IAEs para los controladores del systema no-lineal

disp('IAE solo con cambio en referencia')
disp(['IAE Ziegler-Nichols: ' 'Lineal model = ' num2str(IAE_l_zn(end)) ' No lineal model = ' num2str(IAE_nl_zn(end))])
disp(['IAE Regulacion: ' 'Lineal model = ' num2str(IAE_l_regulacion(end)) ' No lineal model = ' num2str(IAE_nl_regulacion(end))])
disp(['IAE Servo: ' 'Lineal model = ' num2str(IAE_l_servo(end)) ' No lineal model = ' num2str(IAE_nl_servo(end))])

% Comparación solo con perturbación
IncH2=XX; %% Cambio en referencia
IncQ=XX; %% Perturbación

tsim=60;
sim('comparacion',tsim);

% IAE

IAE_l_per = [IAE_l_zn(end) IAE_l_regulacion(end) IAE_l_servo(end)];
IAE_nl_per = [IAE_nl_zn(end) IAE_nl_regulacion(end) IAE_nl_servo(end)];

disp('IAE solo con perturbación')
disp(['IAE Ziegler-Nichols: ' 'Lineal model = ' num2str(IAE_l_zn(end)) ' No lineal model = ' num2str(IAE_nl_zn(end))])
disp(['IAE Regulacion: ' 'Lineal model = ' num2str(IAE_l_regulacion(end)) ' No lineal model = ' num2str(IAE_nl_regulacion(end))])
disp(['IAE Servo: ' 'Lineal model = ' num2str(IAE_l_servo(end)) ' No lineal model = ' num2str(IAE_nl_servo(end))])

%% 3.1 Obtencion de la robustez para las sintonías aplicadas

[Ms_zn, Ss_zn] = ms_basic_PID(XX, XX, XX, XX); %% Función del cálculo de Ms para Ziegler-Nichols
[Ms_servo, Ss_itaes] = ms_basic_PID(XX, XX, XX, XX); %% Función del cálculo de Ms para Servo
[Ms_regulacion, Ss_itaer] = ms_basic_PID(XX, XX, XX, XX); %% Función del cálculo de Ms para Regulacion

disp('Ms obtenidos')
disp(['Ms Ziegler-Nichols = ' num2str(XX)])
disp(['Ms Regulacion = ' num2str(XX)])
disp(['Ms Servo = ' num2str(XX)])


%% 3.2 Aplicacion de una regla de sintnia robusta - metodo Ms

alpha = XX; %% Valor de la alpha
beta_ctrl = 1; %% valor de la beta

tau0 = (XX/XX);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% PI %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PI regulation 

a0_reg16_pi0 = XX; %% a0 para PI regulacion Ms 1.6
a1_reg16_pi0 = XX; %% a1 para PI regulacion Ms 1.6
a2_reg16_pi0 = XX; %% a2 para PI regulacion Ms 1.6

a0_reg20_pi0 = XX; %% a0 para PI regulacion Ms 2.0
a1_reg20_pi0 = XX; %% a1 para PI regulacion Ms 2.0
a2_reg20_pi0 = XX; %% a2 para PI regulacion Ms 2.0
 
b0_reg_pi0 = XX; %% b0 para PI regulacion
b1_reg_pi0 = XX; %% b1 para PI regulacion
b2_reg_pi0 = XX; %% b2 para PI regulacion

% PI Servo 

a0_ser16_pi0 = XX; %% a0 para PI servo Ms 1.6
a1_ser16_pi0 = XX; %% a1 para PI servo Ms 1.6
a2_ser16_pi0 = XX; %% a2 para PI servo Ms 1.6

a0_ser18_pi0 = XX; %% a0 para PI servo Ms 1.8
a1_ser18_pi0 = XX; %% a1 para PI servo Ms 1.8
a2_ser18_pi0 = XX; %% a2 para PI servo Ms 1.8

b0_ser_pi0 = XX; %% b0 para PI servo
b1_ser_pi0 = XX; %% b1 para PI servo
b2_ser_pi0 = XX; %% b2 para PI servo
b3_ser_pi0 = XX; %% b3 para PI servo

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% PID %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% PID regulation 

a0_reg16_pid0 = XX; %% a0 para PID regulacion Ms 1.6
a1_reg16_pid0 = XX; %% a1 para PID regulacion Ms 1.6 
a2_reg16_pid0 = XX; %% a2 para PID regulacion Ms 1.6

a0_reg20_pid0 = XX; %% a0 para PID regulacion Ms 2.0
a1_reg20_pid0 = XX; %% a1 para PID regulacion Ms 2.0
a2_reg20_pid0 = XX; %% a2 para PID regulacion Ms 2.0

b0_reg_pid0 = XX; %% b0 para PID regulacion
b1_reg_pid0 = XX; %% b1 para PID regulacion
b2_reg_pid0 = XX; %% b2 para PID regulacion

c0_reg_pid0 = XX; %% c0 para PID regulacion
c1_reg_pid0 = XX; %% c1 para PID regulacion
c2_reg_pid0 = XX; %% c2 para PID regulacion

% PID Servo 

a0_ser16_pid0 = XX; %% a0 para PID servo Ms 1.6
a1_ser16_pid0 = XX; %% a0 para PID servo Ms 1.6
a2_ser16_pid0 = XX; %% a0 para PID servo Ms 1.6

a0_ser20_pid0 = XX; %% a0 para PID servo Ms 2.0
a1_ser20_pid0 = XX; %% a0 para PID servo Ms 1.6
a2_ser20_pid0 = XX; %% a0 para PID servo Ms 1.6

b0_ser_pid0 = XX; %% b0 para PID servo
b1_ser_pid0 = XX; %% b1 para PID servo
b2_ser_pid0 = XX; %% b2 para PID servo
b3_ser_pid0 = XX; %% b3 para PID servo

c0_ser_pid0 = XX; %% c0 para PID servo
c1_ser_pid0 = XX; %% c1 para PID servo
c2_ser_pid0 = XX; %% c2 para PID servo

%%%%%%%%%%%%%%%%%%%%%%%%%%%% Controllers %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Implementacion de los controladores 
% Importante!!!!! Utilitzad las variables que se han definido justo arriba

% PI Regulation Ms = 1.6

K_pi_reg16 =  XX;

Ti_pi_reg16 = XX;

Td_pi_reg16 = XX;

% PI Regulation Ms = 2.0

K_pi_reg20 =  XX;

Ti_pi_reg20 = XX;

Td_pi_reg20 = XX;

% PI Servo Ms = 1.6

K_pi_ser16 =  XX;

Ti_pi_ser16 = XX;

Td_pi_ser16 = XX;

% PI Servo Ms = 1.8

K_pi_ser18 =  XX;

Ti_pi_ser18 = XX;

Td_pi_ser18 = XX;

% Defining PID Controllers

% PID Regulation Ms = 1.6
K_pid_reg16 =  XX;

Ti_pid_reg16 = XX;

Td_pid_reg16 = XX;

% PID Regulation Ms = 2.0
K_pid_reg20 =  XX;

Ti_pid_reg20 = XX;

Td_pid_reg20 = XX;

% PID Servo Ms = 1.6
K_pid_ser16 =  XX;

Ti_pid_ser16 = XX;

Td_pid_ser16 = XX;

% PID Servo Ms = 2.0
K_pid_ser20 =  XX;

Ti_pid_ser20 = XX;

Td_pid_ser20 = XX;

% Vectores donde se guardan los parámetros encontrados
kp_vect = [K_pi_reg16 K_pi_reg20 K_pi_ser16 K_pi_ser18 K_pid_reg16 K_pid_reg20 K_pid_ser16 K_pid_ser20];
ti_vect = [Ti_pi_reg16 Ti_pi_reg20 Ti_pi_ser16 Ti_pi_ser18 Ti_pid_reg16 Ti_pid_reg20 Ti_pid_ser16 Ti_pid_ser20];
td_vect = [Td_pi_reg16 Td_pi_reg20 Td_pi_ser16 Td_pi_ser18 Td_pid_reg16 Td_pid_reg20 Td_pid_ser16 Td_pid_ser20];

% Obtención del Ms del método uSORT

IAE_lin_reg_usort = [];
IAE_lin_ser_usort = [];

IAE_nolin_reg_usort = [];
IAE_nolin_ser_usort = [];

Ms_usort = [];

for i = 1:length(kp_vect)
   
    Kp_filter = kp_vect(i);
    Ti_filter = ti_vect(i);
    Td_filter = td_vect(i);
    
    [ms_usort_aux, Ss_usort] = ms_filter_PID(XX, XX, XX, alpha, beta_ctrl, P_tf);

    Ms_usort = [Ms_usort ms_usort_aux];
    
    % Regulation (solo aplicamos perturbacion)
    IncH2=XX;
    IncQ=XX;
    
    t_sim = 60;
    sim('control_ms', t_sim);
    set_param('control_ms','MaxConsecutiveZCsMsg','none');

    IAE_lin_reg_usort = [IAE_lin_reg_usort IAE_lineal_filter(end)]; 
    IAE_nolin_reg_usort = [IAE_nolin_reg_usort IAE_nolineal_filter(end)]; 
    
    % Servo (solo aplicacioms cambio en referencia)
    IncH2=XX;
    IncQ=XX;
    
    t_sim = 60;
    sim('control_ms', t_sim);
    set_param('control_ms','MaxConsecutiveZCsMsg','none');

    IAE_lin_ser_usort = [IAE_lin_ser_usort IAE_lineal_filter(end)]; 
    IAE_nolin_ser_usort = [IAE_nolin_ser_usort IAE_nolineal_filter(end)]; 
    
    

end
%% 3.3 Consideración de un segundo grado de libertad para la sintonía en regulación

% PI Ms = 2.0
d0_20_pi = XX; %% d0 PI Ms 2.0
d1_20_pi = XX; %% d1 PI Ms 2.0
d2_20_pi = XX; %% d2 PI Ms 2.0

% PI Ms = 1.8
d0_18_pi = XX; %% d0 PI Ms 1.8
d1_18_pi = XX; %% d1 PI Ms 1.8
d2_18_pi = XX; %% d2 PI Ms 1.8

% PI Ms = 1.6
d0_16_pi = XX; %% d0 PI Ms 1.6
d1_16_pi = XX; %% d1 PI Ms 1.6
d2_16_pi = XX; %% d2 PI Ms 1.6

% PID Ms = 2.0
d0_20_pid = XX; %% d0 PID Ms 2.0
d1_20_pid = XX; %% d1 PID Ms 2.0
d2_20_pid = XX; %% d2 PID Ms 2.0

% PID Ms = 1.8
d0_18_pid = XX; %% d0 PID Ms 1.8
d1_18_pid = XX; %% d1 PID Ms 1.8
d2_18_pid = XX; %% d2 PID Ms 1.8

% PID Ms = 1.6
d0_16_pid = XX; %% d0 PID Ms 1.6
d1_16_pid = XX; %% d1 PID Ms 1.6
d2_16_pid = XX; %% d2 PID Ms 1.6

beta_pi_20 = XX; %% Calculo beta para PI y Ms 2.0
beta_pi_18 = XX; %% Calculo beta para PI y Ms 1.8
beta_pi_16 = XX; %% Calculo beta para PI y Ms 1.6

beta_pid_20 = XX; %% Calculo beta para PID y Ms 2.0
beta_pid_16 = XX; %% Calculo beta para PID y Ms 1.6

% Vector de betas obtenidas
beta_vect = [beta_pi_16 beta_pi_20 beta_pi_16 beta_pi_18 beta_pid_16 beta_pid_20 beta_pid_16 beta_pid_20];

% Simulación de los sistemas con las betas obtenidas anteriormente

IAE_lin_reg_beta = [];
IAE_lin_ser_beta = [];

IAE_nolin_reg_beta = [];
IAE_nolin_ser_beta = [];


Ms_beta = [];

for i = 1:length(kp_vect)
   
    Kp_filter = kp_vect(i);
    Ti_filter = ti_vect(i);
    Td_filter = td_vect(i);
    beta_ctrl = beta_vect(i);
    
    [ms_beta_aux, Ss_beta] = ms_filter_PID(XX, XX, XX, alpha, beta_ctrl, P_tf);
    
    Ms_beta = [Ms_beta ms_beta_aux];
    
    % Regulation (solo aplicamos perturbacion)
    IncH2=XX; %% Cambio en referencia
    IncQ=XX; %% Perturbacion
    
    t_sim = 60;
    sim('control_ms', t_sim);
    set_param('control_ms','MaxConsecutiveZCsMsg','none');

    IAE_lin_reg_beta = [IAE_lin_reg_beta IAE_lineal_filter(end)]; 
    IAE_nolin_reg_beta = [IAE_nolin_reg_beta IAE_nolineal_filter(end)]; 
    
    % Servo (solo aplicamos cambio en referencia)
    IncH2=XX; % Cambio en referencia
    IncQ=XX; % Perturbacion
    
    t_sim = 60;
    sim('control_ms', t_sim);
    set_param('control_ms','MaxConsecutiveZCsMsg','none');

    IAE_lin_ser_beta = [IAE_lin_ser_beta IAE_lineal_filter(end)]; 
    IAE_nolin_ser_beta = [IAE_nolin_ser_beta IAE_nolineal_filter(end)]; 
    
    

end

%% Elección del mejor controlador

IncH2=XX;
IncQ=XX;

Kp_filter = XX;
Ti_filter = XX;
Td_filter = XX;

beta_ctrl = XX;

t_sim = 60;
sim('control_ms', t_sim);
set_param('control_ms','MaxConsecutiveZCsMsg','none');


figure(6)
ax1 = subplot(2,1,1);
ax2 = subplot(2,1,2);
plot(ax1, time, y_nl_filter, 'r')
hold(ax1, 'on') 
plot(ax1, time, ref+x0_ini(2), 'b--')
ylabel(ax1, 'Level')
xlabel(ax1, 'Time')
title(ax1, 'No-Lineal system behaviour')
legend(ax1, 'Output', 'Reference')
grid(ax1, 'on')

controller_nl_filter(502) = 0;
plot(ax2, time, controller_nl_filter, 'k')
xlabel(ax2, 'Time')
title(ax2, 'Controller No-Lineal system behaviour')
grid(ax2, 'on')

