let jsonDataDict;

function loadWordData(url) {
    fetch(url)
        .then(res => res.json())
        .then(data => {
            jsonDataDict = data;
        })
        .then(() => {
            console.log(jsonDataDict);
        }
    )
};

function getWordData(element) {
    const wordData = jsonDataDict[element.id].word_data
    const wordDataHTML = wordData.join('<br>')
    document.getElementById('info-block').innerHTML = wordDataHTML
    wordsArray = Array.from(element.parentElement.children)
    wordsArray.map(function(e) {
        e.style.backgroundColor = 'unset';
    })
    element.style.backgroundColor = '#88C0D0'
};