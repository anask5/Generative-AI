from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = """The global shift toward renewable energy is accelerating,
driven by concerns over climate change and energy security. Solar
and wind power installations have reached record levels worldwide."""

summary = summarizer(text, max_length=30, min_length=10, do_sample=False)
print(summary[0])
