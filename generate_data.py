import csv
import json

INCLUDE_SENTENCE_LEVELS = ["A2", ]
PRONOUNS_DATA = {
    "6": {
        "form_type": "base",
        "base": "я",
    },
    "24": {
        "form_type": "base",
        "base": "ты",
    },
    "4": {
        "form_type": "base",
        "base": "он",
    },
    "288": {
        "form_type": "base",
        "base": "оно",
    },
    "15": {
        "form_type": "base",
        "base": "она",
    },
    "22": {
        "form_type": "base",
        "base": "мы",
    },
    "25": {
        "form_type": "base",
        "base": "вы",
    },
    "18": {
        "form_type": "base",
        "base": "они",
    },
    "59746": {
        "form_type": "acc_or_gen",
        "base": "я",
    },
    "59750": {
        "form_type": "prep_or_dat",
        "base": "я",
    },
    "60085": {
        "form_type": "inst",
        "base": "я",
    },
    "59747": {
        "form_type": "acc_or_gen",
        "base": "ты",
    },
    "59751": {
        "form_type": "prep_or_dat",
        "base": "ты",
    },
    # no instr entry for ты
    # can't его, её, их assume because they could be adjectives, not pronouns
    # no prep entry for он(о)
    "59752": {
        "form_type": "dat",
        "base": "он(о)",
    },
    # can't assume им because could be instr он(о) or dative они
    "59753": {
        "form_type": "prep_or_dat_or_inst",
        "base": "она",
    },
    "59748": {
        "form_type": "acc_or_gen_or_prep",
        "base": "мы",
    },
    "59754": {
        "form_type": "dat",
        "base": "мы",
    },
    # no instr entry for мы
    "59749": {
        "form_type": "acc_or_gen_or_prep",
        "base": "вы",
    },
    "59755": {
        "form_type": "dat",
        "base": "вы",
    },
    # no instr entry for вы
    "40": {
        "form_type": "acc_or_gen",
        "base": "себя'",
    },
    "32403": {
        "form_type": "prep_or_dat",
        "base": "себя'",
    },
    # no instr entry for себя
}

def load_csv(filename):
    with open(filename, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        return list(reader)


def key_on(dicts, key_name):
    result = {}
    for d in dicts:
        key = d[key_name]
        if not key in result:
            result[key] = []
        result[key].append(d)
    return result



print("LOADING DATA...")
print("sentences")
sentences = load_csv("russian3 - sentences.csv")
sentences = [s for s in sentences if s["disabled"] == "0"]
sentences = [s for s in sentences if s["level"] in INCLUDE_SENTENCE_LEVELS]

print("sentences_words")
sentences_words = load_csv("russian3 - sentences_words.csv")
sentences_words = key_on(sentences_words, "sentence_id")

print("words")
words = load_csv("russian3 - words.csv")
words = [w for w in words if w["disabled"] == "0"]
words = [w for w in words if w["position"] in ["", "1"]]
words = key_on(words, "id")


print("GENERATING...")
data = []
for i, sentence in enumerate(sentences):
    row = {}
    row["ru"] = sentence["ru"]
    row["level"] = sentence["level"]
    row["words"] = []
    this_sentences_words = sentences_words.get(sentence["id"], []) 
    for sentence_word_data in this_sentences_words:
        word = {}
        word["form_type"] = sentence_word_data["form_type"]
        start_index = int(sentence_word_data["start"])
        end_index = start_index + int(sentence_word_data["length"])
        word["form"] = row["ru"][start_index:end_index]
        word_id = sentence_word_data["word_id"]
        word_data = words.get(word_id, [])
        if len(word_data) == 0:
            print(f"No word_data for id={sentence_word_data['word_id']}")
        else:
            word_data = word_data[0]
            word["base"] = word_data["accented"]
            word["type"] = word_data["type"]
            word["rank"] = word_data["rank"]
            word["level"] = word_data["level"]
        
        if word_id in PRONOUNS_DATA:
            word["form_type"] = PRONOUNS_DATA[word_id]["form_type"]
            word["base"] = PRONOUNS_DATA[word_id]["base"]
            word["type"] = "pronoun"

        row["words"].append(word)
    data.append(row)


print("SAVING TO FILE...")
with open("data.js", "w") as f:
    f.write("const sentences = ")
    f.write(json.dumps(data, indent=2, ensure_ascii=False))
