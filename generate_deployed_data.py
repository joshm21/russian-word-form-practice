import json

filenames = [
    "data_a1.js",
    "data_a2.js",
    "data_b1.js",
    "data_b2.js",
    "data_c1.js",
    "data_c2.js",
]

result = []
for filename in filenames:
    with open(filename, "r") as f:
        text = f.read()
    json_str = text.replace("const sentences = ", "")
    sentences = json.loads(json_str)
    result.extend(sentences[:5000])

with open("data_deploy.js", "w") as f:
    f.write("const sentences = ")
    f.write(json.dumps(result, indent=2, ensure_ascii=False))
