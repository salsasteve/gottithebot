<template>
  <v-container>
    <v-spacer></v-spacer>
    <v-col>
      <v-row class="justify-center">
        <v-avatar :size="size" :color="backgroundColor">
          <img
            :src="src"
            :alt="alt"
            :width="150"
            :height="150"
            :style="{
              backgroundColor: backgroundColor,
            }"
          />
        </v-avatar>
      </v-row>
    </v-col>
  </v-container>
</template>

<script setup>
defineProps({
  src: {
    type: String,
    required: true,
  },
  alt: {
    type: String,
    default: "Avatar",
  },
  size: {
    type: [Number, String],
    default: 100,
  },
  backgroundColor: {
    type: String,
    default: "primary",
  },
});
</script>
