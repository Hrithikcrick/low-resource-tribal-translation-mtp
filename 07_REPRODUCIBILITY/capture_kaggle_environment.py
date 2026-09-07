import sys
import subprocess
import platform

import torch


with open(
    "KAGGLE_ENVIRONMENT.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "Python:\n"
        + sys.version
        + "\n\n"
    )

    f.write(
        "Platform:\n"
        + platform.platform()
        + "\n\n"
    )

    f.write(
        "PyTorch:\n"
        + str(torch.__version__)
        + "\n\n"
    )

    f.write(
        "CUDA:\n"
        + str(torch.version.cuda)
        + "\n\n"
    )

    f.write(
        "GPU count:\n"
        + str(torch.cuda.device_count())
        + "\n\n"
    )

    for i in range(
        torch.cuda.device_count()
    ):

        f.write(
            f"GPU {i}: "
            + torch.cuda.get_device_name(i)
            + "\n"
        )


freeze = subprocess.check_output(
    [
        sys.executable,
        "-m",
        "pip",
        "freeze"
    ],
    text=True
)


with open(
    "pip_freeze.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        freeze
    )


print(
    "Created KAGGLE_ENVIRONMENT.txt"
)

print(
    "Created pip_freeze.txt"
)
