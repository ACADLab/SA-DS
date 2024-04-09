SA-DS
Description
SA-DS is a project that introduces a comprehensive dataset tailored for DNN-Accelerators, marking a significant stride towards automating DNN (AI) Accelerators. This dataset is designed to support the training, fine-tuning, and employment of multi-short prompt inputs for Large Language Models (LLMs).

Within the SA-DS folder, users will discover .scala files delineating the configurations for each Gemmini unit. The folder SA_DS_json includes the dataset in JSON format, offering detailed descriptions and source code for all configurations. Likewise, SA_DS_csv contains the dataset in CSV format, with dataset_SA_DS_all.csv aggregating all samples into a single file.

Installation
Prerequisites
Docker must be installed on your machine.
With Docker
To deploy this repository via Docker, execute the following command:
Copy code
sudo docker run -it --privileged simonguoziruiberkeley/gemmini_mlsys_22:v1.10 bash
Within the Docker container, navigate to the Gemmini configurations directory:
Copy code
cd chipyard/generators/gemmini/configs/
Replace GemminiCustomConfigs.scala and GemminiDefaultConfigs.scala with the corresponding files found in this repository.

Without Docker
For users opting not to use Docker:

Follow the setup instructions at [Gemmini]([url](https://github.com/ucb-bar/gemmini.git)
Proceed with the same file replacement steps as mentioned above for Docker users.
Usage
This repository supports signed integer data types for DNN-Accelerator configurations, with potential future expansions to accommodate float, complex, and other data types as per DNN requirements.

Contributing
Contributions to extend the dataset's compatibility with different data types are warmly welcomed. To contribute, please:

Fork the repository.
Create your feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -am 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a Pull Request.
