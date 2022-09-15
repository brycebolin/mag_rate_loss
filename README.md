 Provides the correction to the bias efficiency calculation due to trailing losses as a function of V magnitude
 and rate of motion.
 
 V is a float value of the V magnitude of object, omega is a float value of the rate of motion in radians/day
 as a float, telescope is a string value, either G96 or 703.
 
 Adapted from Eqn. 1 from Zavodny et al. 2008.
 
 input is V, V mag, omega_deg_day, rate of motion in degrees per day and the telescope as a string 703 or G96.
 
 normalized to the average Main Belt rate of mb_rate ~0.2 degrees/day.
 
 Valid for G96 for objects with V<15 moving slower than ~9 degs/day.
 
 Valid for 703 for objects with V<20 moving slower than ~10 degs/day.
 
 Note that this is not an absolute estiamte of the survey bias function.
 
 Must be used as a multiplicative correction factor e.g.:
 
 bias_efficiency_with_trailing_loss_correction = bias_efficiency_without_trailing_loss_correction *
 mag_rate_loss(V, omega, telescope)
