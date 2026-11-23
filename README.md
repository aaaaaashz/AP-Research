# Multi-Signal Metabolic State Classification on Edge Hardware

AP Research project (solo, fully computational).

**Research question.** To what extent does combining pH, dissolved oxygen (DO) and
lactate improve classification of mammalian cell metabolic states compared with any
single signal, and does that advantage survive INT8 compression on a Raspberry Pi 4?

## Current stage (due Nov 9, 2026)

- [ ] Set up VS Code and GitHub repository
- [ ] Install TensorFlow and SciPy
- [ ] Confirm parameters and class boundaries (`configs/`)

## Layout

```
configs/
  base.yaml          simulation settings + class boundaries
  generator.yaml     ODE parameters per serum condition (placeholders until fitted)
  scenarios/         (later)
data/raw/naciri2008/ digitised reference curves
scripts/check_env.py checks the TensorFlow / SciPy install
src/apres/           (later)
tests/               (later)
```

## Setup

TensorFlow 2.21 supports Python 3.10–3.13 (not 3.14), so use a 3.13 virtual environment:

```powershell
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/check_env.py
```

## Still to confirm

- Class boundary mapping for the 0.3 / 0.7 thresholds (methods draft Table 3).
- ODE parameters per serum condition (fit to digitised Naciri 2008 Figs 3b, 4b).
- DO uptake term: constant vs substrate-limited (needed for the late DO rise in Fig 3b).
- DO starting value: Naciri CHO DO starts near 78–80 %, not 100 %.

## References

- Naciri M, Kuystermans D, Al-Rubeai M (2008). Monitoring pH and dissolved oxygen in
  mammalian cell culture using optical sensors. *Cytotechnology* 57:245–250.
  doi:10.1007/s10616-008-9160-1
