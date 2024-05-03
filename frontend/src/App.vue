<script setup lang="ts">
import { onMounted, ref } from "vue";

import HelloWorld from "./components/HelloWorld.vue";

// Backend status logic
const status = ref<string>("NOK");

const getStatus = async (): Promise<string> => {
  try {
    // @ts-ignore
    const res = await fetch(`${import.meta.env.VITE_API_URL}/ping`);
    if (res.ok) {
      const json = await res.json();
      return json.status;
    } else {
      console.error(await res.text());
      return "NOK";
    }
  } catch (err) {
    console.error(err);
    return "NOK";
  }
};

// Lifecycle
onMounted(async () => {
  status.value = await getStatus();
});
</script>

<template>
  <HelloWorld :msg="status" />
</template>
