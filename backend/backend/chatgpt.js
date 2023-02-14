const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
  apiKey: "",
});
const openai = new OpenAIApi(configuration);
async function chatgpt_davinci_003()
{
  const response = await openai.createCompletion({
  model: "text-davinci-003",
  prompt: 'Hey there!',
  temperature: 0.5,
  max_tokens: 150,
})
return response;
};

chatgpt_davinci_003();



