"""Check that Python, TensorFlow and SciPy are installed correctly.

    python scripts/check_env.py
"""

import sys

ok = True
print(f"Python     {sys.version.split()[0]}")
if not (3, 10) <= sys.version_info[:2] <= (3, 13):
    print("  WARNING: TensorFlow 2.21 supports Python 3.10-3.13 only")
    ok = False

for name in ("numpy", "scipy", "yaml", "tensorflow"):
    try:
        module = __import__(name)
        print(f"{name:<10} {module.__version__}")
    except ImportError:
        print(f"{name:<10} NOT INSTALLED")
        ok = False

print("OK" if ok else "Fix the items above, then rerun.")
sys.exit(0 if ok else 1)
