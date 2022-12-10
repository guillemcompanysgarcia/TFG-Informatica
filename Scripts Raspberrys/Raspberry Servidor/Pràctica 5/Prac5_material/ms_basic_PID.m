function [ ms_basic, Ss_basic ] = ms_basic_PID(Kp, Ti, Td, Proc_tf)
%ms_basic_PID Function to compute the Ms parameter of the system
%   Kc = Proportional gain
%   Ti = Integrated time
%   Td = Derivative time
%   P = Process transfer function
    
    P = tf(1);
    I = tf(1, [Ti 0]);
    D = tf([Td 0],1);
    
    C = Kp*(P+I+D);
    
    Ss_basic = 1/(1+C*Proc_tf);
    [mag_basic ph_basic w_basic] = bode(Ss_basic);
    ms_basic = max(mag_basic);


end

