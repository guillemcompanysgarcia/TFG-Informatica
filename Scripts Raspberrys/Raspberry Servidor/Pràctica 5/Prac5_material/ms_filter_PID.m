function [ ms_filter, Ss_filter ] = ms_filter_PID(Kc, Ti, Td, alpha, beta, Proc_tf)
%ms_basic_PID Function to compute the Ms parameter of the system
%   Kc = Proportional gain
%   Ti = Integrated time
%   Td = Derivative time
%   P = Process transfer function
    
    % Set-point
    Pr = tf(beta);
    Ir = tf(1, [Ti 0]);
    
    % Feedback
    Py = tf(1);
    Iy = tf(1,[Ti 0]);
    Dy = tf([Td 0], [alpha*Td 1]);
    
    Cr = Kc*(Pr+Ir);
    Cy = Kc*(Py+Iy+Dy);
    
    Ss_filter = 1/(1+Cy*Proc_tf);
    [mag_filter ph_filter w_filter] = bode(Ss_filter);
    ms_filter = max(mag_filter);


end

