import gradio as gr                  
from transformers import pipeline

translation_pipeline = pipeline('translation_en_to_fr') # will hold the model :> goes from english to french
def translate_transformers(englishText):
    result = translation_pipeline(englishText)
    return result[0]['translation_text']

interface = gr.Interface(fn=translate_transformers, 
                         inputs=gr.Textbox(lines=2, placeholder='Text to translate'),
                        outputs='text',
                        title = "Translate English to French!")

interface.launch(inline = False)
