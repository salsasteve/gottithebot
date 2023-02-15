const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
  apiKey: "",
});
const openai = new OpenAIApi(configuration);
async function dalle_2()
{
  const response = await openai.createImage({
  prompt: 'Hey there!',
  n: 1,
  size: "512x512",
})
return response;
};

dalle_2();
