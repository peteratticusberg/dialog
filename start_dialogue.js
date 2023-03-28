const { getTokenEstimates } = require('./tokens')
const { sendChatPrompt } = require('./send_chat_prompt.js')

const startDialogue = async ({ initialPromptA, initialPromptB }) => {
  const systemMessage = { role: 'system', content: 'You are a helpful assitant.' }
  const messagesA = [systemMessage]
  const messagesB = [systemMessage]
  messagesA.push({ role: 'user', content: initialPromptA })
  messagesB.push({ role: 'user', content: initialPromptB })

  console.log('messagesA:')
  console.log(messagesA)

  let aOrB = 'A'
  const maxMessages = 20
  while (messagesA.length <= maxMessages) {
    console.log(`\n\n 
      message count: ${messagesA.length}
      time: ${new Date().toLocaleTimeString('en-US', { hour12: false })} 
      ${JSON.stringify(getTokenEstimates(messagesA))}
    \n\n`)
    if (aOrB === 'A') {
      const message = await sendChatPrompt({ messages: messagesA })
      console.log(message.content)
      messagesA.push({ ...message })
      messagesB.push({ ...message, role: 'user' })
      aOrB = 'B'
    } else {
      const message = await sendChatPrompt({ messages: messagesB })
      console.log(message.content)
      messagesB.push({ ...message })
      messagesA.push({ ...message, role: 'user' })
      aOrB = 'A'
    }
    // await sleep(5)
  }

  return messagesA
}

module.exports = { startDialogue }
