# Text Summarization Project with PEGASUS

## Overview

This project demonstrates the application of text summarization techniques using the PEGASUS model. It involves training a PEGASUS model on the SAMSum dataset to generate concise summaries from conversational dialogues.

## Dataset

The SAMSum dataset is used for training and evaluation. It consists of dialogues and their corresponding summaries:

- Train Split: 14,732 examples
- Validation Split: 819 examples
- Test Split: 818 examples
- Features:

- id: Unique identifier for each example
- dialogue: The conversational text to be summarized
- summary: The reference summary for the dialogue

## Processing Pipeline

### Tokenization

- Tokenizer: AutoTokenizer from the Hugging Face Transformers library
- Input Tokenization: Dialogue texts are tokenized with a maximum length of 1024 tokens.
- Target Tokenization: Summaries are tokenized with a maximum length of 128 tokens.

## Model

- Model Used: PEGASUS (Pretrained Summarization Model)
- Library: Hugging Face Transformers
- Training:
- Epochs: 1
- Batch Size: 1 (per device)
- Gradient Accumulation Steps: 16
- Warmup Steps: 500
- Weight Decay: 0.01
- Logging Steps: 10
- Evaluation Strategy: Steps

## Data Collation

- Data Collator: DataCollatorForSeq2Seq from Hugging Face Transformers

## Evaluation

- Metric: ROUGE (Recall-Oriented Understudy for Gisting Evaluation)
- ROUGE Scores:
- ROUGE-1: 0.0214
- ROUGE-2: 0.0
- ROUGE-L: 0.0211
- ROUGE-Lsum: 0.0214

## Model and Tokenizer

- Saving Model: The PEGASUS model is saved as pegasus-samsum-model.
- Saving Tokenizer: The tokenizer is saved in the tokenizer directory.
-

## Model Loading

The model and tokenizer are loaded using the Hugging Face Transformers library.

## Prediction

To generate summaries, the pipeline function from the Transformers library is used with the PEGASUS model and tokenizer. The generation parameters include:

- length_penalty: 0.8
- num_beams: 8
- max_length: 128

## Example

### Dialogue:

Hannah: Hey, do you have Betty's number?
Amanda: Lemme check
Hannah: <file_gif>
Amanda: Sorry, can't find it.
Amanda: Ask Larry
Amanda: He called her last time we were at the park together
Hannah: I don't know him well
Hannah: <file_gif>
Amanda: Don't be shy, he's very nice
Hannah: If you say so..
Hannah: I'd rather you texted him
Amanda: Just text him 🙂
Hannah: Urgh.. Alright
Hannah: Bye
Amanda: Bye bye

## Reference Summary:

Hannah needs Betty's number but Amanda doesn't have it. She needs to contact Larry.

## Model Summary:

Amanda: Ask Larry Amanda: He called her last time we were at the park together .<n>Hannah: I'd rather you texted him .<n>Amanda: Just text him .

## Installation

Ensure the following libraries are installed:

- transformers
- datasets
- evaluate
  pip install transformers datasets evaluate

## Usage

1. Load the model and tokenizer:

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
tokenizer = AutoTokenizer.from_pretrained("path_to_tokenizer")
model = AutoModelForSeq2SeqLM.from_pretrained("path_to_model")

2. Generate summaries:

pipe = pipeline("summarization", model=model, tokenizer=tokenizer)
summary = pipe("Your dialogue text here")
