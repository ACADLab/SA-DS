import itertools
import re
import os
import subprocess  # For better control over subprocesses

def generate_and_verify_configurations(input_file):
    mesh_sizes = [2, 4, 8, 16, 32, 64]
    boolean_options = [True, False]
    dataflow_options = ["OS", "WS", "BOTH"]
    acc_types = [32, 16]
    spatial_array_output_types = [8, 10, 16, 20]
    build_command = "./scripts/build-verilator.sh"  # Command for verification

    # Back up the original file content
    with open(input_file, 'r') as f:
        original_contents = f.read()

    try:
        for mesh_size in mesh_sizes:
            for has_training_convs, has_max_pool, has_nonlinear_activations, \
                has_dw_convs, has_normalizations, has_first_layer_optimizations in itertools.product(boolean_options, repeat=6):
                for dataflow in dataflow_options:
                    for acc_type, spatial_array_output in itertools.product(acc_types, spatial_array_output_types):
                        new_contents = original_contents  # Start with original contents for each iteration
                        
                        # Modifications for dynamic values, similar to previous version
                        # (Omitted for brevity, insert modifications here)

                        # Directly overwrite the input file with new configurations
                        with open(input_file, 'w') as f:
                            f.write(new_contents)
                        
                        # Execute the build command and wait for it to complete
                        result = subprocess.run(build_command, shell=True)
                        if result.returncode != 0:
                            print(f"Build failed for configuration: {mesh_size} {dataflow} {acc_type} {spatial_array_output}")
                            break  # Optional: break if a build fails, or continue to the next config

    finally:
        # Restore the original file content
        with open(input_file, 'w') as f:
            f.write(original_contents)

# Example usage
input_file_path = "/root/chipyard/generators/gemmini/configs/GemminiDefaultConfigs.scala"
generate_and_verify_configurations(input_file_path)