# SA-DS

## Description

This project SA-DS focuses on automating AI acclerators by introducing a domain focused dataset tailored for DNN (AI)-Accelerators. This dataset is consists of SCALA files that are used to generate Gemmini hardware accelerators, contains file formats that designed to support the training, fine-tuning, and employment of multi-short prompt inputs for Large Language Models (LLMs). For an complete understanding of the project's objectives and methodologies, we recommend reviewing our paper available at [this link](archive-link).

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
