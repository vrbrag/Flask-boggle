
$('.add-word').on('submit', handleSubmit)
let words = new Set()
let score = 0
let secs = 60
let timer = setInterval(keepTime, 1000)

function showMessage(msg) {
   $('.msg')
      .text(msg)
}

function showScore() {

   $('.score').text(score)
}

async function handleSubmit(evt) {
   evt.preventDefault()
   // debugger
   let word = $('.word').val()
   // check if a word was returned and if word already exists in set of words
   if (!word) return

   if (words.has(word)) {
      // $('.msg').clear()
      // let text = document.createTextNode(`Already found ${word}`)
      // $('.msg').append(text)
      let msg = `Already found ${word}.`
      showMessage(msg)
      return
   }

   // check word against dictionary (words.txt) using GET response
   const resp = await axios.get('/check-word', { params: { word: word } })

   if (resp.data.result == 'not-word') {
      let msg = `'${word}' is not a valid word`
      showMessage(msg)
      return
   }
   else if (resp.data.result == 'not-on-board') {
      let msg = `'${word}' is not on board`
      showMessage(msg)
      return
   }
   else {
      words.add(word) // add word to words
      $('.words').append(`<li> ${word}`) // display word
      let msg = `Added: ${word}`  // display new message
      showMessage(msg)

      score += word.length // add score to score
      showScore()
   }

   $('.word').val("").focus()

}

function showTimer() {
   $('.timer').text(secs)
}

async function keepTime() {
   secs -= 1
   showTimer()

   if (secs == 0) {
      clearInterval(timer)
      await scoreGame()
   }
}

async function scoreGame() {
   $('.add-word').hide()
   const resp = await axios.post('/post-score', { score: score })

   if (resp.data.brokeRecord) {
      let msg = `New record: ${score}`
      showMessage(msg)
   }
   else {
      let msg = `Final score: ${score}`
      showMessage(msg)
   }

}


