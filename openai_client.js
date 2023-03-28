const { Configuration, OpenAIApi } = require('openai')

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY
})

const openAIClient = new OpenAIApi(configuration)

module.exports = openAIClient
