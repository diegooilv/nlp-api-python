from transformers import pipeline

print("🔄 Carregando modelos em Português (CPU-only)...")

resumidor = pipeline(
    "summarization",
    model="rhaymison/flan-t5-portuguese-small-summarization",
    tokenizer="rhaymison/flan-t5-portuguese-small-summarization",
    device=-1,                    
    framework="pt",              
    max_length=512,               
    min_length=30,
    do_sample=False
)

modelo_qa = pipeline(
    "question-answering",
    model="mrm8488/bert-base-portuguese-cased-finetuned-squad-v1-pt",
    tokenizer="mrm8488/bert-base-portuguese-cased-finetuned-squad-v1-pt",
    device=-1                     
)

def get_resumidor():
    return resumidor

def get_qa_model():
    return modelo_qa
   
print("✅ Modelos carregados com sucesso.")
