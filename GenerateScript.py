import openai

openai.api_key = "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"

def summarize(text):

    # "Summarize the item.description in two sentences".
    prompt = "Summarize this in two sentences: " + text

    text_summary = openai.Completion.create(
      model = "text-davinci-003",
      prompt = prompt,
      temperature = 1,
      max_tokens = 600,
      top_p = 1,
      frequency_penalty = 0,
      presence_penalty = 0
    )

    return (text_summary)
