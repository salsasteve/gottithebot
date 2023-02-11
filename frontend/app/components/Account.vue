<template>
  <v-container v-if="user">
    <v-row class="justify-center">
      <v-col cols="12" sm="12" md="6">
        <v-card>
          <v-row>
            <v-col cols="12" sm="12">
              <Avatar v-if="src" :src="src" />
            </v-col>
            <v-col cols="12" sm="12">
              <form>
                <v-text-field
                  :model-value="username"
                  :counter="15"
                  variant="outlined"
                  label="Username"
                  required
                ></v-text-field>

                <v-text-field
                  :model-value="email"
                  variant="outlined"
                  label="Email"
                  required
                ></v-text-field>

                <v-text-field
                  :model-value="website"
                  variant="outlined"
                  label="Website"
                  required
                ></v-text-field>

                <v-btn
                  :loading="loading"
                  :disabled="loading"
                  @click="
                    updateProfile(
                      userId,
                      username,
                      email,
                      website,
                      avatar,
                      supabase
                    )
                  "
                >
                  Update Profile
                </v-btn>
              </form>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  :loading="loading"
                  :disabled="loading"
                  outline="primary"
                  color="primary"
                  @click="signOut(supabase)"
                >
                  Logout
                </v-btn>
              </v-card-actions>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

    
<script setup>
const props = defineProps(["user"]);

// const user = ref(props.user);
const user = ref(props.user);

const supabase = useSupabaseClient();

const loading = ref(true);
const username = ref("");
const email = ref("");
const website = ref("");
const avatar = ref("");
const src = ref("");
const userId = ref(user.value.id);

if (!user) {
  //Send to index.vue
  const router = useRouter();
  router.push("/");
} else {
  const data = await getProfile(user.value.id, supabase);

  username.value = data.username || parseEmail(user.value.email).username;
  email.value = user.value.email || user.value.email;
  website.value = data.website || "koolkids.ai";
  avatar.value = data.avatar_url;

  downloadImage(avatar, src, supabase);
  loading.value = false;
}
</script>
    