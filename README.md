# triton-ensemble

This project explores the implementation of model ensembles within the Triton Inference Server. It aims to enable seamless loading and execution of two or more models, along with the aggregation of their results.

## Usage

To run the project, follow these steps:

1. Clone the Repository:

   ```
   git clone https://github.com/luizvilasboas/triton-ensemble.git
   ```

   > **Note:** Git Large File Storage (LFS) is required for this repository. Install it using `git lfs install` before cloning.

2. Install Dependencies:

   ```
   cd triton-ensemble
   pip install -r requirements.txt
   ```

3. Build the Docker Image:

   ```
   docker build -t triton-inference-server .
   ```

4. Create a Container:

   ```
   bash server.sh
   ```

5. Run the Client:

   ```
   python3 main.py
   ```

## Contributing

If you're interested in contributing to this project, feel free to open a merge request. We welcome all forms of collaboration!

## License

This project is available under the [The Unlicense](https://github.com/luizvilasboas/triton-ensemble/blob/main/LICENSE). For more information, please see the LICENSE file.
