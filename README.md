# SA-DS

## Description

This project SA-DS focuses on automating AI acclerators by introducing a domain focused dataset tailored for DNN (AI)-Accelerators. This dataset is consists of SCALA files that are used to generate Gemmini hardware accelerators, contains file formats that designed to support the training, fine-tuning, and employment of multi-short prompt inputs for Large Language Models (LLMs). Please refer to the following paper for a general introduction of the SA-DS data-set: [SA-DS](https://arxiv.org/abs/2404.10875).

## Getting Started

This section provides a quick start guide to using the SA-DS dataset and associated configurations.

### Prerequisites

- Docker installed on your machine for Docker-based setup.

### Installation

#### With Docker

1. **Pull the Docker Image**: Run the following command to pull the required Docker image:

```bash
sudo docker run -it --privileged simonguoziruiberkeley/gemmini_mlsys_22:v1.10 bash
```
2. **Navigate to Gemmini Configurations**: Inside the Docker container, move to the Gemmini configurations directory:
   ```bash
   cd chipyard/generators/gemmini/configs/
   ```
3. **Replace Configuration Files**: Replace GemminiCustomConfigs.scala and GemminiDefaultConfigs.scala with the files provided in this repository.
#### Without Docker
   ### Prerequisites
- Setup GitHub make sure to follow the steps mentioned in the following repo [Gemmini](https://github.com/ucb-bar/gemmini.git).
- **Replace Configuration Files**: Follow the same file replacement steps as outlined for Docker users.

## Acknowledgments
## Citation Information
If this dataset is used in any research please use the citation below.
``` bash
@misc{SADS2024dataset,
      title={A Dataset for Large Language Model-Driven AI Accelerator Generation},
      author={Mahmoud Nazzal and Deepak Vungarala and Mehrdad Morsali and Chao Zhang and Arnob Ghosh and Abdallah Khreishah and Shaahin Angizi},
      year={2024},
      eprint={2404.10875},
      archivePrefix={arXiv},
      primaryClass={cs.AR}
}
```

