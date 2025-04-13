from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

LANG_CODES = {
    "English": "eng_Latn",
    "Telugu": "tel_Telu"
}

def translate(text, src_lang, tgt_lang):
    tokenizer.src_lang = LANG_CODES[src_lang]
    inputs = tokenizer(text, return_tensors="pt")
    tgt_lang_code = LANG_CODES[tgt_lang]
    bos_token_id = tokenizer.convert_tokens_to_ids(tgt_lang_code)

    translated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=bos_token_id,
        max_length=512,
        num_beams=4,
        early_stopping=True
    )
    return tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
