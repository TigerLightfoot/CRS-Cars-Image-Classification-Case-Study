# Data Instructions

This case study uses the CRS Cars Dataset from Meta-Album.

## Dataset Source

Dataset page: Meta-Album CRS Cars Dataset  
Dataset ID: CRS  
Domain: Vehicles  
Original source: Stanford Cars Dataset  
Task: Image classification  

## Dataset Versions

Meta-Album provides three CRS versions through OpenML:

- Micro version: OpenML ID 44245
- Mini version: OpenML ID 44289
- Extended version: OpenML ID 44323

For this case study, the Micro version is recommended because it is smaller and easier for a second-year student to run on a laptop.

## Downloading with OpenML

Install OpenML:

```bash
pip install openml

import openml

DATASET_ID = 44245  # Micro version

dataset = openml.datasets.get_dataset(
    DATASET_ID,
    download_data=True,
    download_all_files=True
)
```
Recommended Data Organization

Because this is an image classification problem, your final local folder should be organized by class.

```
print(dataset.name)

data/
  cars/
    train/
      class_1/
      class_2/
      class_3/
    test/
      class_1/
      class_2/
      class_3/
