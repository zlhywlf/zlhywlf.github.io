<script setup lang="ts">
import { useData } from "vitepress"

const { frontmatter, theme } = useData()
</script>

<template>
  <div v-if="frontmatter.home">
    <ul>
      <li v-for=" page, index in theme.pages" :key="index"><a :href="page.path">{{ page.name }}</a></li>
    </ul>
  </div>
</template>
