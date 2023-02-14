
const { createClient } = require("@supabase/supabase-js");


const supabaseUrl = 'https://vfuucjqcuyjfwllihoqb.supabase.co'
const supabaseKey = ""
const supabase = createClient(supabaseUrl, supabaseKey)


const prompt = ''
const chatgpt_output = ''

async function insert_into_chatgpt()
{
const { data, error } = await supabase
  .from('chatgpt')
  .insert([
    { "prompt": prompt, "chatgpt_output": chatgpt_output },
  ])
};
insert_into_chatgpt()



const dalle_output = ''

async function insert_into_dalle()
{
const { data, error } = await supabase
  .from('chatgpt')
  .insert([
    { "prompt": prompt, "img_url": dalle_output },
  ])
};
insert_into_dalle()


async function retrieve_prompt_id_from_chatgpt()
{

  let { data: chatgpt, error } = await supabase
  .from('chatgpt')
  .select("id")
  .eq("prompt", prompt)


};
retrieve_prompt_id_from_chatgpt()



