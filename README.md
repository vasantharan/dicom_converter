# dicom_converter

Convert DICOM files to JPEG format using Python.

## Installation

You can install `dicom_converter` using `pip`:

```bash
pip install dicom_converter
```

## Usage
```bash
from dicom_converter import converter

# Specify input and output paths
folder_path = "/path/to/input_files"
output_path = "/path/to/output_files"

# Convert DICOM to JPEG
converter.convert(folder_path, output_path)
```
## Dependencies
1. pydicom
2. Pillow
```bash
pip install pydicom Pillow
```

## Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (git checkout -b feature/new-feature)
3. Commit your changes (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature/new-feature)
5. Create a pull request


## License
License: Apache 2.0
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Acknowledgments
Thanks to the contributors of pydicom and Pillow.

## Author
Vasantharan K
