# CS3 Rubric: Fine-Grained Car Model Classification

**DS 4002 Case Study Assignment**  
**Target Audience:** 2nd-Year UVA Student  
**Topic:** Image classification using the CRS Cars Dataset

## General Description

In this case study, you will investigate whether a computer vision model can classify car models from images. You will use the CRS Cars Dataset from Meta-Album, which is based on the Stanford Cars Dataset. Your task is to organize the data, build a basic image classification model, evaluate performance, and explain the results in a clear case study report.

This project is designed for a second-year UVA student with some Python experience, but not necessarily deep experience in computer vision. The main goal is not to build the most advanced model possible. The goal is to practice turning a real-world visual classification problem into a reproducible data science workflow.

## Learning Goals

By completing this case study, you will practice how to:

- Frame a real-world image classification problem.
- Work with an existing image dataset.
- Organize image data for modeling.
- Train or evaluate a baseline classification model.
- Interpret accuracy, precision, recall, F1-score, and confusion matrices.
- Explain why fine-grained classification is difficult.
- Communicate limitations responsibly.

## Required Deliverables

Students must submit:

1. **Case Study Report**  
   A 4–6 page report explaining the problem, data, methods, results, and limitations.

2. **GitHub Repository**  
   A clean repository with code, setup instructions, data instructions, and outputs.

3. **Model Evaluation**  
   At minimum, include accuracy and one class-level evaluation method such as precision, recall, F1-score, or a confusion matrix.

4. **Limitations Section**  
   Discuss what your model does well, what it struggles with, and why it should not be treated as a complete real-world vehicle recognition system.

## Suggested Report Structure

### 1. Introduction

Explain the project context. Why might someone want to classify car models from images? What makes this problem interesting or difficult?

Your introduction should include a clear research question, such as:

**Can a machine learning model accurately classify car models from images, and what limitations appear when the vehicle classes are visually similar?**

### 2. Dataset Description

Describe the CRS Cars Dataset. Include:

- Where the dataset comes from.
- What the images represent.
- How many classes are included in the version you used.
- Whether you used the Micro, Mini, or Extended version.
- How the images were preprocessed.
- Any limitations of the dataset.

### 3. Methods

Explain your modeling approach. You may use:

- a simple convolutional neural network,
- transfer learning,
- a pretrained image model,
- or another reasonable image classification method.

You should explain why your method is appropriate for image classification. You do not need to use the most advanced model, but you do need to explain your choices clearly.

### 4. Results

Present your model performance using metrics such as:

- accuracy,
- precision,
- recall,
- F1-score,
- and/or a confusion matrix.

Do not only report one number. Explain what the results mean. If your model performs poorly, that is acceptable as long as you explain why.

### 5. Discussion

Interpret the results. Consider questions such as:

- Which classes were easiest to classify?
- Which classes were hardest?
- Did the model confuse visually similar cars?
- Did dataset size affect performance?
- Would a larger or higher-resolution dataset help?

### 6. Limitations and Ethics

Discuss the limitations of the project. Consider:

- The images are preprocessed to 128x128 pixels.
- Car classes may be visually similar.
- The dataset is mainly useful for benchmark research, not immediate commercial deployment.
- A real-world car recognition system would need testing across lighting, angle, weather, camera quality, and geographic context.
- The model should not be used for surveillance or enforcement without serious ethical review.

### 7. Conclusion

End with a clear recommendation. Should this approach be developed further? What would need to improve before the model could be trusted in a real-world setting?

## Assessment Criteria

| Category | Meets Expectations | Needs Revision |
|---|---|---|
| Problem Framing | Clearly explains the car classification problem and why fine-grained image classification is difficult. | Gives only a vague topic or does not explain why the project matters. |
| Dataset Understanding | Describes the CRS Cars Dataset, version used, class structure, image format, and limitations. | Uses the dataset without explaining what it contains or how it was prepared. |
| Modeling Approach | Uses a reasonable image classification method and explains why it fits the task. | Runs code without explaining the model choice or uses an approach that does not match the problem. |
| Evaluation | Includes accuracy plus class-level evaluation or a confusion matrix, with interpretation. | Only reports one metric or gives results without explaining them. |
| Reproducibility | GitHub repo includes setup instructions, code, data instructions, and organized outputs. | Another student would not be able to reproduce the work. |
| Limitations | Clearly discusses dataset, model, and real-world limitations. | Makes unsupported claims or ignores weaknesses. |
| Communication | Report is organized, readable, and written for a peer audience. | Report is hard to follow or too technical without explanation. |

## Minimum Technical Requirements

Your project must include:

- Python code or notebook.
- Data access instructions.
- At least one trained or evaluated classification model.
- At least one visualization or table of results.
- A README explaining how to reproduce the work.
- Citations for the dataset and any model/documentation used.

## Tips for Success

- Use the Micro dataset if you want faster training.
- Start with a simple baseline before trying anything complex.
- Focus on explaining your process clearly.
- Use mistakes as part of your analysis. Confusion between similar car models is important evidence.
- Do not oversell your model. A responsible limitation section is part of a strong project.

## Submission Checklist

- [ ] Report is 4–6 pages.
- [ ] GitHub repo has a clear README.
- [ ] Dataset source is cited.
- [ ] Code is included and organized.
- [ ] Results include accuracy and class-level interpretation.
- [ ] Limitations section is specific.
- [ ] Final conclusion answers the research question.
