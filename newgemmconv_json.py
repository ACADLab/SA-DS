import os
import json
import re

# Define the directory containing the Scala source code files
source_code_dir = "SA_DS"  # Update this path as needed
json_output_dir = "SA_DS_json"  # Name of the directory to save JSON files

# Function from Program 2 to analyze filenames and generate descriptions
def analyze_filename(filename):
    parts = filename.split('.')[0].split('_')
    systolic_array = parts[1]
    features = parts[2:-3]  # Adjust to exclude the last 3 parts (bit_support, spatial_array_bits, "BOTH")
    bit_support, spatial_array_bits = parts[-2], parts[-1]

    message = f"This is a {systolic_array} systolic arrayed gemmini "

    feature_messages = ["training convolutions", "max pool", "nonlinear activation", 
                        "dw_convs", "normalizations", "first_layer_optimizations"]

    for i, has_feature in enumerate(features):
        feature_state = "does not have" if has_feature.lower() == "false" else "has"
        message += f"{feature_state} {feature_messages[i]}, "

    if "BOTH" in filename:
        message += "consists of option BOTH, supports TPU and NVDLA making it robust for any type of dataflow model implementation, "
    if "WS" in filename:
        message += "supports Weight Stationary NVDLA like (less-area) dataflow,"
    if "OS" in filename:
        message += "supports Output Stationary (more area) dataflow, "

    # Handle bit_support and spatial_array_bits with predefined messages
    bit_support_message = {"16": "it has accumulation type supporting 16 signed integer bits, ",
                           "32": "it has accumulation type supporting 32 signed integer bits, "}
    spatial_array_output_message = {"8": "it has a spatial array output supporting 8 bit Signed integer, ",
                                    "10": "it has a spatial array output supporting 10 bit Signed integer, ",
                                    "16": "it has a spatial array output supporting 16 bit Signed integer, ",
                                    "20": "it has a spatial array output supporting 20 bit Signed integer, "}
    message += bit_support_message.get(bit_support, "")
    message += spatial_array_output_message.get(spatial_array_bits, "")

    # Application mapping based on the systolic array size
    applications = {
        # Applications mapping...
        2: "Applications: Ultra-low Power Sensor Fusion Analyzing very minimal sensor data (e.g., single-axis accelerometer, photodiode) for pattern recognition tasks within extremely power-constrained devices.Extremely Tiny Networks: Consider: Linear Classifiers and Regressors: Tasks with readily separable inputs and simple decision boundaries might work with very shallow or single-layer networks.Ultra-Quantized Networks: Aggressive quantization to 1-bit or 2-bit weights could greatly increase computation density, allowing for small but meaningful networks.",
        4: "Applications: Object detection applications on low-power edge devices, Voice command recognition on smart home devices",  
        8: "Applications: Audio processing pipelines on wearables, Real-time image classification on smartphones",  
        16:"Applications: Image Classification: Small, highly quantized models like MobileNetV1, SqueezeNet, or heavily pruned versions of larger CNNs. Real-time Signal Processing: Models for keyword spotting, simple gesture recognition from small sensor arrays.",
        32:"Applications: Moderate Image Tasks: Models like MobileNetV2, ShuffleNet, potentially less aggressively quantized ResNet. Sensor/NLP Tasks: If data dimensionality isn't extreme, RNNs/LSTMs for time-series or small text-based models.",
        64:"Applications: Larger CNNs: Potentially ResNet18, some VGG variants. Quantization or pruning would likely still be beneficial. More Complex Tasks: Handling multimodal sensor fusion, less niche deep learning architectures outside simple CNNs.",
    }

    systolic_array_size = int(parts[1].replace('x', ''))
    application_message = applications.get(systolic_array_size, "Applications: ... (Add default applications here)")
    message += application_message

    return message

# Ensure the source code directory exists
if not os.path.isdir(source_code_dir):
    print(f"Directory {source_code_dir} does not exist.")
else:
    # Create the output directory if it doesn't exist
    if not os.path.exists(json_output_dir):
        os.makedirs(json_output_dir)

    # Sort the files to maintain order
    files = sorted([file for file in os.listdir(source_code_dir) if file.endswith(".scala")])

    # Process each file
    for i, filename in enumerate(files):
        # Generate description using Program 2's logic
        description = analyze_filename(filename)

        # Read the source code
        with open(os.path.join(source_code_dir, filename), 'r') as source_file:
            source_code = source_file.read()

        # Prepare JSON content
        json_content = {
            "description": description,
            "source_code": source_code
        }

        # Define JSON file path
        json_file_name = os.path.splitext(filename)[0] + ".json"
        json_file_path = os.path.join(json_output_dir, json_file_name)

        # Write JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(json_content, json_file, indent=4)

    print(f"Processed {len(files)} source code files and saved them in the '{json_output_dir}' directory.")
