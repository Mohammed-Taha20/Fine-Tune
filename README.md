# 🧠 Fine-Tune Qwen 1.5B for Translation & Data Extraction

This project fine-tunes **[Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)** using **LoRA (Low-Rank Adaptation)** to improve performance on **Arabic–English translation** and **JSON-based data extraction** tasks.  
The goal is to adapt Qwen’s general language understanding to handle structured multilingual data transformation and extraction tasks — aiming for GPT-4-like reliability on smaller hardware.

---

## 🚀 Project Overview
The fine-tuning process enables the model to:
- Translate **Arabic text to English** with high accuracy and contextual understanding.  
- Extract structured information from **unstructured text** and output it in **JSON format**.  
- Handle both tasks within a **single multitask fine-tuned model**, improving data processing pipelines.

---

## ⚙️ Technical Details

- **Base Model:** `Qwen/Qwen2.5-1.5B-Instruct`  
- **Fine-tuning Method:** LoRA (Parameter-Efficient Fine-Tuning using PEFT)  
- **Training Framework:** PyTorch + Hugging Face Transformers + PEFT  
- **Dataset Size:** ~2,800 samples  
- **Tasks:**  
  - *Task 1:* Arabic → English Translation  
  - *Task 2:* JSON Data Extraction  
- **Data Format:** JSON-based pairs for both translation and extraction tasks  
- **Hardware:** GPU (Colab / single-GPU setup)

---

## 📂 Repository Structure

Fine-Tune/
├── app/ # (Optional) interface or testing application
├── data/ # training and validation data (not included)
├── notebooks/ # fine-tuning and evaluation notebooks
├── requirements.txt # dependencies
├── README.md # project documentation
└── utils/ # helper functions for preprocessing and evaluation


---

## 📊 Objectives

- Achieve efficient fine-tuning on limited data and hardware.  
- Evaluate model performance against GPT-4-style translation and extraction outputs.  
- Explore multitask fine-tuning for multilingual and structured data tasks.

---

## 💡 Future Work

- Expand dataset for better generalization.  
- Add evaluation metrics (BLEU for translation, accuracy/F1 for extraction).  
- Deploy the fine-tuned model via a web interface or API for real-time use.  

