import pandas as pd
from datasets import Dataset
from transformers import (
    BertTokenizer,
    BertForSequenceClassification,
    Trainer,
    TrainingArguments
)

# -------------------------------
# 1. Load data
# -------------------------------
df = pd.read_csv("training/data/medical_text_processed.csv")

# Drop empty rows
df = df.dropna()

# -------------------------------
# 2. Encode labels (IMPORTANT FIX)
# -------------------------------
label_map = {label: idx for idx, label in enumerate(df["label"].unique())}
df["label"] = df["label"].map(label_map)

print("Label mapping:", label_map)

# -------------------------------
# 3. Convert to HuggingFace Dataset
# -------------------------------
dataset = Dataset.from_pandas(df)

# -------------------------------
# 4. Tokenizer
# -------------------------------
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def tokenize(batch):
    return tokenizer(
        batch["text"],
        padding="max_length",
        truncation=True,
        max_length=128
    )

dataset = dataset.map(tokenize, batched=True)
dataset = dataset.remove_columns(["text"])
dataset.set_format("torch")

# -------------------------------
# 5. Model
# -------------------------------
model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=len(label_map)
)

# -------------------------------
# 6. Training arguments
# -------------------------------
training_args = TrainingArguments(
    output_dir="backend/app/models/bert_disease_classifier",
    eval_strategy="no",
    per_device_train_batch_size=4,
    num_train_epochs=3,
    logging_steps=5,
    save_strategy="epoch"
)

# -------------------------------
# 7. Trainer
# -------------------------------
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

# -------------------------------
# 8. Train
# -------------------------------
trainer.train()

# -------------------------------
# 9. Save model
# -------------------------------
trainer.save_model("backend/app/models/bert_disease_classifier")
tokenizer.save_pretrained("backend/app/models/bert_disease_classifier")

print("✅ BERT model trained and saved successfully")
