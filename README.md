# SA-DS

## Description

The SA-DS project is committed to automating AI accelerators by introducing a specialized dataset tailored for Deep Neural Network (DNN) Accelerators. This dataset consists of SCALA files used to generate Gemmini hardware accelerators. Due to GitHub policies, only the first 1000 data points are visible, but zip files with similar names contain the complete dataset. It encompasses file formats such as CSV and JSON, facilitating training, fine-tuning, and leveraging multi-short prompt inputs for Large Language Models (LLMs). For a comprehensive understanding of the SA-DS dataset, please refer to the following paper: [SA-DS](https://arxiv.org/abs/2404.10875).

## Getting Started

This section provides a quick start guide for utilizing the SA-DS dataset along with its associated configurations.

### Prerequisites

- Ensure Docker is installed on your system for this setup.

### Installation

#### Using Docker

1. **Pull the Docker Image**: Execute the following command to retrieve the required Docker image:

    ```bash
    sudo docker run -it --privileged deepakvungarala/sa_ds:v_1 bash
    ```

2. **Navigate to Gemmini Configurations**: Within the Docker container, navigate to the Gemmini configurations directory:

    ```bash
    cd chipyard/generators/gemmini/configs/
    ```

   In this directory, a Python script named `autogemm.py` can be found which is used to verify the data points in dataset.

3. **Replace Configuration Files**: Replace GemminiCustomConfigs.scala and GemminiDefaultConfigs.scala with the files provided in this repository.

#### Without Docker

### Prerequisites

- Set up GitHub by following the instructions in the following repository: [Gemmini](https://github.com/ucb-bar/gemmini.git).
  **Note**: Due to some issues, we cannot successfully clone the above repository. Hence, we opted for the Docker setup. The packages differ, and compiling the same code for a Git-cloned repository and Docker may not yield the expected results.

-After the GitHub repo is successfully cloned perform the following steps:

- Utilize the file `GeneratingSA_DS_with_title.py` in this repository to create the dataset for code corresponding to GitHub.

- **Replace Configuration Files**: Follow the same steps for file replacement as outlined for Docker users.

 

## Citation Information
If this dataset is used in any research, please use the following citation:
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

* SADS2024dataset.  A Dataset for Large Language Model-Driven AI Accelerator Generation. Mahmoud Nazzal, Deepak Vungarala, Mehrdad Morsali, Chao Zhang, Arnob Ghosh, Abdallah Khreishah, and Shaahin Angizi (2024). arXiv:2404.10875 [cs.AR] https://arxiv.org/abs/2404.10875 

