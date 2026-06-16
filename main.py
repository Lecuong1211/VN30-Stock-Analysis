import subprocess
import sys

scripts = [
    "src/data_download.py",
    "src/exploratory_analysis.py",
    "src/visualization.py",
    "src/financial_ratios.py"
]

for script in scripts:

    print("\n" + "=" * 50)
    print(f"Running {script}")
    print("=" * 50)

    result = subprocess.run(
        [sys.executable, script]
    )

    if result.returncode != 0:

        print(
            f"Error running {script}"
        )

        break

print("\nPROJECT COMPLETED")