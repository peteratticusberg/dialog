require('dotenv').config()
const { startDialogue } = require('./start_dialogue.js')
const { getTokenEstimates } = require('./tokens')
const fs = require('fs');

const sampleDialogues = JSON.parse(fs.readFileSync('./sample_dialogues.json'))

const run = async () => {
  const messages = await startDialogue(sampleDialogues.brainChemistry)
  console.log(getTokenEstimates(messages))
}

run()
