# This code is used to develop the SA-DS dataset.
import itertools
import re
import os

def generate_configurations(input_file, output_file_prefix, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    mesh_sizes = [2, 4, 8, 16, 32, 64]
    boolean_options = [True, False]
    dataflow_options = ["OS", "WS", "BOTH"]
    acc_types = [32, 16]
    spatial_array_output_types = [8, 10, 16, 20]

    with open(input_file, 'r') as f:
        file_contents = f.read()

    for mesh_size in mesh_sizes:
        for has_training_convs, has_max_pool, has_nonlinear_activations, \
            has_dw_convs, has_normalizations, has_first_layer_optimizations in itertools.product(boolean_options, repeat=6):
            for dataflow in dataflow_options:
                for acc_type, spatial_array_output in itertools.product(acc_types, spatial_array_output_types):
                    new_contents = file_contents
                    # Adjustments for dynamic values
                    new_contents = re.sub(r"tileRows = \d+", "tileRows = 1", new_contents)
                    new_contents = re.sub(r"tileColumns = \d+", "tileColumns = 1", new_contents)
                    new_contents = re.sub(r"meshRows = \d+", f"meshRows = {mesh_size}", new_contents)
                    new_contents = re.sub(r"meshColumns = \d+", f"meshColumns = {mesh_size}", new_contents)
                    new_contents = re.sub(r"dataflow = Dataflow\.\w+", f"dataflow = Dataflow.{dataflow}", new_contents)
                    new_contents = re.sub(r"has_training_convs = \w+", f"has_training_convs = {str(has_training_convs).lower()}", new_contents)
                    new_contents = re.sub(r"has_max_pool = \w+", f"has_max_pool = {str(has_max_pool).lower()}", new_contents)
                    new_contents = re.sub(r"has_nonlinear_activations = \w+", f"has_nonlinear_activations = {str(has_nonlinear_activations).lower()}", new_contents)
                    new_contents = re.sub(r"has_dw_convs = \w+", f"has_dw_convs = {str(has_dw_convs).lower()}", new_contents)
                    new_contents = re.sub(r"has_normalizations = \w+", f"has_normalizations = {str(has_normalizations).lower()}", new_contents)
                    new_contents = re.sub(r"has_first_layer_optimizations = \w+", f"has_first_layer_optimizations = {str(has_first_layer_optimizations).lower()}", new_contents)
                    new_contents = re.sub(r"accType = SInt\(\d+\.W\)", f"accType = SInt({acc_type}.W)", new_contents)
                    new_contents = re.sub(r"spatialArrayOutputType = SInt\(\d+\.W\)", f"spatialArrayOutputType = SInt({spatial_array_output}.W)", new_contents)

                    # Construct the output file path to include the directory
                    output_file_path = os.path.join(output_directory, f"{output_file_prefix}_{mesh_size}_{str(has_training_convs).lower()}_{str(has_max_pool).lower()}_{str(has_nonlinear_activations).lower()}_{str(has_dw_convs).lower()}_{str(has_normalizations).lower()}_{str(has_first_layer_optimizations).lower()}_{dataflow}_{acc_type}_{spatial_array_output}.scala")
                                       
                    with open(output_file_path, 'w') as f:
                        f.write(new_contents)

# Example usage
input_file = "newgemm.scala"
output_file_prefix = "dataset"
output_directory = "SA_DS"  # Specify your desired directory here
generate_configurations(input_file, output_file_prefix, output_directory)
