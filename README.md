# russian-word-form-practice
A web app for practicing Russian word forms (conjugations, declensions, etc)

## Quickstart
https://joshm21.github.io/russian-word-form-practice/
* click the sentence to reveal the answer
* click next to load a new sentences
* scroll down to adjust filters and which sentences are used

## Running locally
(no internet needed and can load more sentences)
1. Download the words, sentences, and sentences_words csv files from [OpenRussian's database](https://app.togetherdb.com/db/fwoedz5fvtwvq03v/russian3/words).
2. Run generate_data.py; adjust INCLUDE_SENTENCE_LEVELS as desired; can convert apostraphes to accents with [this script](https://github.com/joshm21/russian-text-tools)
3. Open index.html

## Possible next steps
* pregenerate more sentences; then compress and upload here
* add controls to filter by searched word or max/min word rank (from frequency list)
