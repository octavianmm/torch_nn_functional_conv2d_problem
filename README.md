# torch_nn_functional_conv2d_problem
Different output on ARM and x86_64 architectures for torch.nn.functional.conv2d
To run the script: python3 functional_conv2d_example.py
Already computed results available in results/ folder. Differences can be observed when performing a 2-way comparison between output_tensor_arm.txt and output_tensor_x86_64.txt.
The arm result was obtained on an NVIDIA Jetson Nano, Ubuntu 18.04.4 LTS, pytorch .
The x86_64 result was computed on an Intel i5-8250U, Ubuntu 18.04.4 LTS, pytorch 1.4.0.
