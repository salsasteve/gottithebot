<template>
  <div>
    <Avatar v-model:path="avatar_path" />
    <h2>Home</h2>
    <p>
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. Velit doloribus
      laboriosam odit voluptatem et sit ipsa, voluptas, unde ex natus quia id
      dignissimos rerum fugiat. Asperiores incidunt cumque tenetur repellendus?
    </p>
    <p>
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. Velit doloribus
      laboriosam odit voluptatem et sit ipsa, voluptas, unde ex natus quia id
      dignissimos rerum fugiat. Asperiores incidunt cumque tenetur repellendus?
    </p>
  </div>
</template>

<script setup >
import { getProfile } from "@/utils/supabase";
const supabase = useSupabaseClient();

const loading = ref(true);
const username = ref("");
const website = ref("");
const avatar_path = ref("");

loading.value = true;
const user = useSupabaseUser();
console.log("user.value.id", user.value.id);
const data = getProfile(user.value.id, supabase);
data
  .then((data) => {
    // console.log("data", data);

    username.value = data.username;
    website.value = data.website;
    avatar_path.value = data.avatar_url;

    // console.log("data.avatar_url", data.avatar_url);
    // console.log("avatar_path.value", avatar_path.value);
  })
  .catch((error) => {
    console.log("error", error);
    loading.value = false;
  });
// console.log("data", data);
// if (data) {
//   username.value = data.username;
//   website.value = data.website;
//   avatar_path.value = data.avatar_url;
// }
// console.log("data.avatar_url", data.avatar_url);
// console.log("avatar_path.value", avatar_path.value);
// loading.value = false;
</script>