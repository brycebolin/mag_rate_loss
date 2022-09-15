Provides the correction to the bias efficiency calculation due to trailing losses as a function of V magnitude and rate of motion.


Adapted from Zavodny et al. 2008.


The function is normalized to the average Main Belt rate of mb_rate = 0.004 radians/day or 0.23 degrees/day


V is a float value of the V magnitude of object, omega is a float value of the rate of motion in radians/day as a float, telescope is a string value, either G96 or 703


used as a multiplicative correction factor e.g.: bias_efficiency_with_trailing_loss_correction = bias_efficiency_without_trailing_loss_correction * mag_rate_loss(V, omega, telescope)
