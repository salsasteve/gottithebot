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
              <v-card-text>
                <h3>{{ website }}</h3>
              </v-card-text>
              <form>
                <v-text-field
                  v-model="username"
                  :counter="15"
                  label="Username"
                  required
                ></v-text-field>

                <v-text-field
                  v-model="email"
                  label="Email"
                  required
                ></v-text-field>

                <v-text-field
                  v-model="website"
                  :items="website"
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

  username.value = data.username;
  email.value = user.value.email;
  website.value = data.website;
  avatar.value = data.avatar_url;

  downloadImage(avatar, src, supabase);
  loading.value = false;
}
</script>
    