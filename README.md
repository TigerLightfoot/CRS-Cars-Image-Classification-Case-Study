###Fine-Grained Car Model Classification Case Study

### DS 4002 CS3 Case Study  
### Created by Tiger Lightfoot

## Project Overview

This repository contains a DS 4002 case study built around the CRS Cars Dataset from Meta-Album. The project asks students to explore whether computer vision can classify car models from images and to think carefully about what makes fine-grained image classification difficult.

The CRS Cars Dataset is based on the Stanford Cars Dataset and contains images of different car models. In the full dataset, there are 196 vehicle classes. The Meta-Album version provides preprocessed 128x128 RGB images and offers smaller versions through OpenML, which makes the dataset more manageable for student projects.

This case study is designed for a second-year UVA student with some Python experience but limited background in computer vision. The goal is not to build a perfect model. The goal is to practice creating a clear, reproducible image classification workflow and explaining the strengths and limitations of the results.

## Scenario

Imagine you are working with a small transportation analytics company that wants to test whether a computer vision model can identify car models from images. The company does not need a perfect commercial system yet. Instead, they want a first analysis that explains whether this task is realistic, what makes it difficult, and what kind of model performance is possible using a smaller image dataset.

Your job is to act as the data scientist on this project. You will organize the data, train or evaluate a classification model, measure performance, and explain what your results mean.

## Research Question

**Can a machine learning model accurately classify car models from images, and what limitations appear when the vehicle classes are visually similar?**

## Dataset

This project uses the CRS Cars Dataset from Meta-Album.

Key details:

- Dataset name: CRS Cars Dataset
- Domain: Vehicles
- Task type: Image classification
- Original source: Stanford Cars Dataset
- Full dataset classes: 196 car model classes
- Image format: RGB images
- Image size: 128x128 pixels in the Meta-Album version
- Access: OpenML through Meta-Album

Recommended version for this case study:

- **Micro version:** smaller and easiest to run
- **Mini version:** more complete but still manageable
- **Extended version:** larger and better for advanced students

For this assignment, the Micro version is recommended because it is more realistic for a second-year student working on a laptop.

## Repository Contents

```text
CRS-Cars-Image-Classification-Case-Study/
├── README.md
├── docs/
│   ├── CS3_Hook_Cars_Image_Classification.md
│   └── CS3_Rubric_Cars_Image_Classification.md
├── materials/
│   ├── references.md
│   └── source_notes.md
├── data/
│   └── README.md
├── code/
│   ├── starter_model.py
│   └── evaluation_template.py
├── requirements.txt
└── .gitignore
