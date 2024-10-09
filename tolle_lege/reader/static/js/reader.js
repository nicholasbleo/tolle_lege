wordClicked = false;

function getWordParse(event) {
    if (!wordClicked) {
        wordId = event.target.getAttribute('data-id');
        parseElement = document.querySelector(`div.word-parse[data-id="${wordId}"]`);
        console.log(parseElement);
        parseElement.classList.remove("hidden");
        parseElement.classList.add("visible");
    }
}

function hideWordParse(event) {
    if (!wordClicked) {
        wordId = event.target.getAttribute('data-id');
        parseElement = document.querySelector(`div.word-parse[data-id="${wordId}"]`);
        if (!parseElement.classList.contains("clicked-parse")) {
            parseElement.classList.remove("visible");
            parseElement.classList.add("hidden");
        }
    }
}

function handleWordClick(event) {
    wordId = event.target.getAttribute('data-id');
    parseElement = document.querySelector(`div.word-parse[data-id="${wordId}"]`);
    if (!parseElement.classList.contains("clicked-parse")) {

        clickedParse = document.querySelector(".clicked-parse");
        clickedText = document.querySelector(".clicked-text");

        if (clickedParse != null) {
            clickedParse.classList.remove("clicked-parse");
            clickedParse.classList.add("hidden");
            clickedText.classList.remove("clicked-text");
        }
        parseElement.classList.add("clicked-parse");
        parseElement.classList.remove("visible");
        event.target.classList.add("clicked-text");
        wordClicked = true;

    } else {

        parseElement.classList.remove("clicked-parse");
        event.target.classList.remove("clicked-text");
        wordClicked = false;

    }
}