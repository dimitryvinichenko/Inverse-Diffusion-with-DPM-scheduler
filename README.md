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

-----------------------------------------------------------------------------
Environment Setup Instructions

To reproduce the Python environment used for this project, please follow the steps below:

1. Ensure Python 3.x is installed on your system.

2. Create a new virtual environment named 'research':
   ```
   python3 -m venv research
   ```

4. Activate the virtual environment:

   ```
   source research/bin/activate
   ```


5. Install all required packages from this file:
   ```
   pip install -r requirements.txt
   ```


Once these steps are completed, the environment will be configured identically
to the one used during development and testing.


