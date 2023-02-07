<template>
  <img :src="src" :alt="username" class="user-img" />
</template>

<script setup>
import { getProfile, downloadImage } from "../utils/supabase";

const supabase = useSupabaseClient();

const username = ref("");
const website = ref("");
const avatar_path = ref("");

const user = useSupabaseUser();
const data = getProfile(user.value.id, supabase);
const src = ref("");
data
  .then((data) => {
    console.log("data", data);

    username.value = data.username;
    website.value = data.website;
    avatar_path.value = data.avatar_url;

    src.value = downloadImage(avatar_path.value, supabase);
  })
  .catch((error) => {
    console.log("error", error);
  });
</script>