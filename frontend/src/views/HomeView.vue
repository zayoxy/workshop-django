<script setup>
// Composition API

import axios from "axios";
import { ref, onMounted } from "vue";

const users = ref([]);

const fetchUsers = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/users/");
  users.value = res.data;
};

onMounted(() => {
  fetchUsers();
});
</script>

<template>
  {{ users }}
  <q-page padding>
    <img
      class="fixed-center"
      src="@/assets/images/coffee_dev_meme_bruce_almighty.gif"
    />
  </q-page>
</template>
