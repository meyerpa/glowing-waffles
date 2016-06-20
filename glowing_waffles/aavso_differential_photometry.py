import numpy as np

def aavso_differential_photometry(instrument_mag, ref_star_instrument_mags, 
            ref_star_ref_mags):
    """
    Return differential photometry for each star in the table `instrument_mag`
    assuming that the rows indicted by `reference_stars`, with
    magnitudes listed in `ref_star_mags`.

    Parameters
    ----------

    instrument_mag : numpy.ndarray
        Instrumental magnitude for each of the sources on which photometry is
        to be performed.
    ref_star_instrument_mags : numpy.ndarray
        Instrumental magnitude of each of the reference stars.
    ref_star_ref_mags : numpy.ndarray
        Reference magnitudes of each of the reference stars.
        
    Returns
    -------

    diff_mag, diff_mag_err : array-like, same shape as `instrument_mag`
        Computed differential magnitude and error for each star in the
        `instrument_mag` array.
    """
    
    # ensure numpy arrays are the same dimensions
    if (instrument_mag.shape != ref_star_instrument_mags or ref_star_instrument_mags != ref_star_ref_mags):
        raise ValueError('numpy array dimension mismatch')
    
    # note: mag1 - mag2 = -2.5 log10 (flux1/flux2)
    differential_mag = instrument_mag - ref_star_instrument_mags
    standardized_mag = differential_mag + ref_star_ref_mags
    
    return standardized_mag
    
