<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-row>
        <v-col xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>Sign in via magic link</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field
                  prepend-icon="person"
                  v-model="email"
                  label="Email"
                  type="text"
                ></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                :loading="loading"
                :disabled="loading"
                outline="primary"
                color="primary"
                @click="handleLogin"
              >
                Send Link
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-layout>
  </v-container>
</template>
  
  <script setup>
const supabase = useSupabaseClient();

const loading = ref(false);
const email = ref("");
const handleLogin = async () => {
  try {
    loading.value = true;
    console.log(email.value);
    let redirect_link = "https://www.thingkr.xyz";
    if (checkOnLocal()) {
      redirect_link = "http://localhost:3000";
      console.log("local");
    }

    const { data, error } = await supabase.auth.signInWithOtp({
      email: email.value,
      options: {
        redirect_to: redirect_link,
      },
    });
    console.log("data", data);
    if (error) throw error;
    alert("Check your email for the login link!");
  } catch (error) {
    alert(error.error_description || error.message);
  } finally {
    loading.value = false;
  }
};
</script>