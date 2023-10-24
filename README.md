# russian-word-form-practice
A web app for practicing Russian word forms (conjugations, declensions, etc)

## Quickstart
https://joshm21.github.io/russian-word-form-practice/
* click the sentence to reveal the answer
* click next to load a new sentences
* scroll down to adjust filters and which sentences are used

## Running locally
(no internet needed and can load more sentences)
1. Download index.html, style.css, script.js
2. Download the data.js file you want, unzip, and rename to data.js
3. Open index.html in a browser

## Generating data.js
1. Download the words, sentences, and sentences_words csv files (; separated) from [OpenRussian's database](https://app.togetherdb.com/db/fwoedz5fvtwvq03v/russian3/words).
2. Run generate_data.py; adjust INCLUDE_SENTENCE_LEVELS as desired; can convert apostraphes to accents with [this script](https://github.com/joshm21/russian-text-tools)

## Possible next steps
* add controls to filter by searched word or max/min word rank (from frequency list)
