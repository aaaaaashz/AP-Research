# Digitised Naciri et al. (2008) curves

Source: Naciri M, Kuystermans D, Al-Rubeai M (2008). Monitoring pH and dissolved
oxygen in mammalian cell culture using optical sensors. *Cytotechnology* 57:245–250.
doi:10.1007/s10616-008-9160-1

Digitise with WebPlotDigitizer (CHO panels only, one CSV per serum condition):

| File                     | Figure | y-axis               |
|--------------------------|--------|----------------------|
| `do_<cond>.csv`          | 3b     | DO, % air saturation |
| `ph_<cond>.csv`          | 4b     | pH                   |
| `cells_<cond>.csv` (opt) | 1b     | cells ×10⁵/mL        |

`<cond>` is one of `5pct`, `2p5pct`, `1pct`, `0pct`. Columns: `time_h,value`.

Record the WebPlotDigitizer version, the axis calibration points and the date here.
