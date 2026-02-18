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

const columns = [
  {
    name: "id",
    label: "ID",
    field: (row) => row.id,
  },
  {
    name: "username",
    label: "Username",
    field: (row) => row.username,
  },
];
</script>

<template>
  <q-page class="q-pa-lg">
    <div class="row justify-center">
      <div style="max-width: 800px; width: 100%">
        <h5 class="q-my-md text-center">Users</h5>
        <q-card>
          <q-table
            :rows="users"
            :columns="columns"
            row-key="id"
            flat
            bordered
            class="table-centered"
          />
        </q-card>

        <div class="row justify-center q-mt-lg">
          <img src="@/assets/images/coffee_dev_meme_bruce_almighty.gif" />
        </div>
      </div>
    </div>
  </q-page>
</template>
