let filteredSentences = []

const showAnswer = () => {
	document.getElementById("answer").style.visibility = "visible";
}

const displayNewSentence = () => {
	const randomSentenceIndex = Math.floor(Math.random() * filteredSentences.length);
	const sentence = filteredSentences[randomSentenceIndex]
	const randomWordIndex = Math.floor(Math.random() * sentence.words.length);
	const word = sentence.words[randomWordIndex]
	const newPrompt = sentence.ru.replaceAll(word.form, `(${word.base})`)
	const newAnswer = word.form 
	document.getElementById("prompt").innerText = newPrompt
	document.getElementById("answer").style.visibility = "hidden";
	document.getElementById("answer").innerText = newAnswer
}

const filterSentences = () => {
	const allowedSentenceLevels = getCheckedValuesArray("sentenceLevel")
	const allowedWordTypes = getCheckedValuesArray("wordType")
	const allowedFormTypes = getCheckedValuesArray("formType")
	let result = []
	for (const sentence of sentences) {
		const newSentence = {}
		if (!allowedSentenceLevels.includes(sentence.level)) {
			continue
		}
		newSentence.ru = sentence.ru
		newSentence.words = []
		for (const word of sentence.words) {
			const newWord = {}
			if (!allowedWordTypes.includes(word.type)) {
				continue
			}
			//if word.form_type doesn't include any allowedFormTypes
			if (!allowedFormTypes.some(substring => word.form_type.includes(substring))) {
				continue
			}
			newWord.form = word.form
			newWord.base = word.base
			newSentence.words.push(newWord)
		}
		if (newSentence.words.length == 0) {
			continue
		}
		result.push(newSentence)
	}
	filteredSentences = result
	document.getElementById("filteredSentencesCount").innerText = filteredSentences.length
	displayNewSentence()
}

const getCheckedValuesArray = (checkboxName) => {
	return Array.from(document.querySelectorAll(`input[type=checkbox][name=${checkboxName}]:checked`), c => c.value)
}

const checkAll = () => {
	document.querySelectorAll("input[type=checkbox]").forEach(checkbox => {
		checkbox.checked = true
	})
	filterSentences()
}

const uncheckAll = () => {
	document.querySelectorAll("input[type=checkbox]").forEach(checkbox => {
		checkbox.checked = false
	})
	filterSentences()
}

document.getElementById("btnFlip").addEventListener("click", showAnswer)
document.getElementById("btnNext").addEventListener("click", displayNewSentence)
document.querySelectorAll("input[type=checkbox]").forEach(checkbox => {
	checkbox.addEventListener("change", filterSentences)
})
document.getElementById("btnCheckAll").addEventListener("click", checkAll)
document.getElementById("btnUncheckAll").addEventListener("click", uncheckAll)

filterSentences()
displayNewSentence()
