# Inverse-Diffusion-with-DPM-scheduler

This repository provides code to reproduce the experiments from the paper *Inverse Diffusion with DPM Scheduler*. It focuses on the inversion of diffusion models using solvers such as DDIM, DPM-Solver, and DPM-Solver++ with Align Your Steps (AYS). The project includes implementations for Stable Diffusion 1.5 and Stable Diffusion XL, facilitating image editing through latent inversion and prompt modification.

### Features

- **Inversion Methods**: Implementations of DDIM, DPM-Solver, and DPM-Solver++ with AYS.
- **Model Support**: Compatible with Stable Diffusion 1.5 and Stable Diffusion XL.
- **Image Editing Pipeline**: Generate images from prompts, invert them to latent space, modify prompts, and reconstruct edited images.
- **Reproducibility**: Scripts and configurations to replicate the experiments and results presented in the paper.

### Repository Structure

- `src/`: Core source code for inversion and sampling.
- `SD15/` and `SDXL/`: Model-specific configurations and scripts.
- `metrics/`: Evaluation metrics and tools.
- `FastSAM/`: Utilities for semantic segmentation and mask generation.

For detailed instructions and examples, please refer to the individual directories and scripts.

# ------------------------------
# Environment Setup Instructions
#
# 1. Make sure Python 3 is installed.
# 2. Create a virtual environment:
#      python3 -m venv research
# 3. Activate the environment:
#      source research/bin/activate    # Linux/Mac
#      research\Scripts\activate.bat   # Windows
# 4. Install dependencies from this file:
#      pip install -r requirements.txt
#
# After that, you can run the code within this environment.
# ------------------------------
