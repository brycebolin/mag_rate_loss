def mag_rate_loss(V, omega_deg_day, telescope):
 '''
 Provides the correction to the bias efficiency calculation due to trailing losses as a function of V magnitude
 and rate of motion.
 V is a float value of the V magnitude of object, omega is a float value of the rate of motion in radians/day
 as a float, telescope is a string value, either G96 or 703.
 Adapted from Eqn. 1 from Zavodny et al. 2008 using values
 input is V, V mag, omega_deg_day, rate of motion in degrees per day and the telescope as a string 703 or G96.
 normalized to the average Main Belt rate of mb_rate ~0.2 degrees/day.
 Valid for G96 for objects with V<15 moving slower than ~9 degs/day.
 Valid for 703 for objects with V<20 moving slower than ~10 degs/day.
 Note that this is not an absolute estiamte of the survey bias function.
 Must be used as a multiplicative correction factor e.g.:
 bias_efficiency_with_trailing_loss_correction = bias_efficiency_without_trailing_loss_correction *
 mag_rate_loss(V, omega, telescope)
 '''
 if telescope == 'G96':
    fN = np.array([ 1.00001,     1.00026,   1.00005,    1.00008,    1.00008,    1.00014,    1.00030,   1.00178,   1.00358 ])
    fa = np.array([ 0.000207922, 0.0163587, 0.00180970, 0.00318065, 0.00347024, 0.00669746, 0.0181274, 0.355975, 63.7594])
    fb = np.array([ 0.916735,    0.490216,  0.778955,   0.704542,   0.687700,   0.613175,   0.498605,  0.162735,  0.00188665])

    if V <= 15.8:
        Vobs = (0.066147* V**2) - (0.798776 * V) + 12.059343
    else:
        Vobs = (0.953161 * V) + 0.849415

 if telescope == '703':
    fN = np.array([ 1.00001,    1.00001,     1.00000,     1.00000,     1.00001,    1.00010,   1.00037,  1.00080,     1.00067])
    fa = np.array([ 0.00172047, 1.44477,     2.34770e-08, 1.63705e-06, 0.00104255, 0.0312772, 0.178731, 0.975056,  174.383])
    fb = np.array([ 0.371139,   0.000384786, 1.78856,     1.32051,     0.557442,   0.278400,  0.187526, 0.0778586,   0.000381091])

    if V <= 15.6:
        Vobs = (0.053214* V**2) - (0.492498 * V) + 10.385527
    else:
        Vobs = (0.925866 * V) + 1.337756



 iv_pre_round = Vobs - 13.0
 iv = int(np.floor(iv_pre_round))#iv is an index for several arrays describing the parameters of Eqn. 1 from Zavodny et al. 2008  and must be an integer. We therefore must floor the value and change type from float to int so that it can be used as an array index.
 if iv > 8:
    iv = 8
 if iv <0:
    iv = 0

 cor = fN[iv] * ( ( 1.0 + fa[iv] ) - fa[iv] * np.exp( fb[iv] * ( omega_deg_day - 0.2 ) ) )
 if cor < 0.0:
    cor = 0
 return cor
