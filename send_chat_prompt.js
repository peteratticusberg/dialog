const openaiClient = require('./openai_client.js')

const sendChatPrompt = async ({ messages }) => {
  const completion = await openaiClient.createChatCompletion({
    model: 'gpt-3.5-turbo',
    messages
  })
  const message = completion.data.choices[0].message
  return message
}

module.exports = { sendChatPrompt }
