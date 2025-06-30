import os

# Define the folder structure
folder_structure = {
    "Phase-1-Foundations": [
        "big-o-notation",
        "recursion",
        "sorting-searching"
    ],
    "Phase-2-Core-DSA": [
        "arrays",
        "trees",
        "graph-algorithms",
        "dynamic-programming"
    ],
    "Phase-3-Advanced": [
        "tries",
        "string-similarity",
        "union-find",
        "bit-manipulation"
    ],
    "Phase-4-Real-World": [
        "fuzzy-matching-api",
        "rate-limiter-fastapi",
        "referral-network-analysis"
    ]
}

# Create folders and .gitkeep files
for phase, subfolders in folder_structure.items():
    for sub in subfolders:
        path = os.path.join(phase, sub)
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, ".gitkeep"), "w") as f:
            f.write("")