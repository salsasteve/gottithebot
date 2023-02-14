
const { createClient } = require("@supabase/supabase-js");


async function auth()
{
let { data, error } = await supabase.auth.signUp({
    email: 'issh_hrc@hotmail.co.uk',
    password: 'eoRgYRjDJcOplGTwpRul'
  })
}; 
auth()
