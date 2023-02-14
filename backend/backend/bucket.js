
const { createClient } = require("@supabase/supabase-js");

const supabaseKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZmdXVjanFjdXlqZndsbGlob3FiIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzU3MTExMjEsImV4cCI6MTk5MTI4NzEyMX0.OE2jHToa6kVZhEpvS1Osb9RfRmPbznwbD4rBxU5jzTI"
const supabaseUrl = 'https://vfuucjqcuyjfwllihoqb.supabase.co'
const supabase = createClient(supabaseUrl, supabaseKey)


// async function create_bucket()
// {
// const { data, error } = await supabase
//   .storage
//   .createBucket("garbage")
// return data ; 
// };

// create_bucket() ; 



var array = ["https://oaidalleapiprodscus.blob.core.windows.net/private/org-7T0nPJfTOGFWpbRNiNbTFMlW/user-0yY4qUGYdYIUA8Fp0GDRUhg0/img-ZJzDqj1lWNqNPXlibsdeuGX7.png?st=2023-02-07T19%3A26%3A41Z&se=2023-02-07T21%3A26%3A41Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-02-07T19%3A43%3A42Z&ske=2023-02-08T19%3A43%3A42Z&sks=b&skv=2021-08-06&sig=cIx5RiD/7FEhwftnwRuIXM8sakJjh7x1%2BBhrbPQtkQ8%3D"];
array.forEach((t) => {
    var img = document.createElement("img");
    img.src = t;
    document.body.appendChild(img);
})



async function insert_into_bucket()
{
const avatarFile = document
const { data, error } = await supabase
  .storage
  .from('avatars')
  .upload('public/avatar1.png', avatarFile, {
    cacheControl: '3600',
    upsert: false
  })
}; 

insert_into_bucket() ; 