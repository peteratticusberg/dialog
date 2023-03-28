const getTokenEstimate = (messages) => {
  const fullContent = messages.map(message => {
    return message.content
  }).join(' ')
  const wordCount = fullContent.split(/s+/).length
  return wordCount / 0.75
}

const getTokenUsageEstimate = (messages) => {
  const tokenEstimate = getTokenEstimate(messages)
  return tokenEstimate * messages.length / 2
}

const getTokenCostEstimate = (messages) => {
  const tokenUsageEstimate = getTokenEstimate(messages)
  return tokenUsageEstimate / 1000 * 0.0002
}

const getTokenEstimates = (messages) => {
  return {
    tokenEstimate: getTokenEstimate(messages),
    tokenUsageEstimate: getTokenUsageEstimate(messages),
    tokenCostEstimate: getTokenCostEstimate(messages)
  }
}

module.exports = { getTokenEstimates }
