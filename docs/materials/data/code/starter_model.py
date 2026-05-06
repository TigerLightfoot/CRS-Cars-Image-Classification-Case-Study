"""
Starter model script for the CRS Cars Image Classification Case Study.

This script gives students a basic PyTorch image classification structure.
It assumes images have already been organized into folders like:

data/cars/train/class_name/image.jpg
data/cars/test/class_name/image.jpg

Students can adapt this file depending on how their OpenML download is structured.
"""

from pathlib import Path

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader


DATA_DIR = Path("data/cars")
TRAIN_DIR = DATA_DIR / "train"
TEST_DIR = DATA_DIR / "test"

BATCH_SIZE = 32
EPOCHS = 5
LEARNING_RATE = 0.001
IMG_SIZE = 128


def get_data_loaders():
    transform = transforms.Compose([
        transforms.Resize((IMG_SIZE, IMG_SIZE)),
        transforms.ToTensor(),
    ])

    train_data = datasets.ImageFolder(TRAIN_DIR, transform=transform)
    test_data = datasets.ImageFolder(TEST_DIR, transform=transform)

    train_loader = DataLoader(
        train_data,
        batch_size=BATCH_SIZE,
        shuffle=True
    )

    test_loader = DataLoader(
        test_data,
        batch_size=BATCH_SIZE,
        shuffle=False
    )

    return train_loader, test_loader, train_data.classes


def build_model(num_classes):
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    return model


def train_model(model, train_loader, device):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    model.train()

    for epoch in range(EPOCHS):
        running_loss = 0.0

        for images, labels in train_loader:
            images = images.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()

            outputs = model(images)
            loss = criterion(outputs, labels)

            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        avg_loss = running_loss / len(train_loader)
        print(f"Epoch {epoch + 1}/{EPOCHS}, Loss: {avg_loss:.4f}")


def evaluate_model(model, test_loader, device):
    model.eval()

    correct = 0
    total = 0

    all_preds = []
    all_labels = []

    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            _, predicted = torch.max(outputs, 1)

            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            all_preds.extend(predicted.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    accuracy = correct / total
    print(f"Test Accuracy: {accuracy:.4f}")

    return all_labels, all_preds


def main():
    if not TRAIN_DIR.exists() or not TEST_DIR.exists():
        raise FileNotFoundError(
            "Train/test folders not found. Check data/README.md for setup instructions."
        )

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    train_loader, test_loader, class_names = get_data_loaders()

    model = build_model(num_classes=len(class_names))
    model = model.to(device)

    train_model(model, train_loader, device)

    y_true, y_pred = evaluate_model(model, test_loader, device)

    print("Class names:")
    print(class_names)

    torch.save(model.state_dict(), "car_classifier_model.pth")


if __name__ == "__main__":
    main()
