def aavso_differential_photometry(instrument_mag, ref_star_intrument_mags, ref_star_ref_mags):
    """
    Return differential photometry for each star in the table `instrument_mag`
    assuming that the rows indicted by `reference_stars`, with
    magnitudes listed in `ref_star_mags`.

    Parameters
    ----------

    instrument_mag : array-like
        Instrumental magnitude for each of the sources on which photometry is
        to be performed.
    ref_star_intrument_mags : array-like
        Instrumental magnitude of each of the reference stars.
    ref_star_ref_mags : array-like
        Reference magnitudes of each of the reference stars.

    Returns
    -------

    diff_mag, diff_mag_err : array-like, same shape as `instrument_mag`
        Computed differential magnitude and error for each star in the
        `instrument_mag` array.
    """
    
