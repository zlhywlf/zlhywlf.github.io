<script setup lang="ts">
import { useData, Content } from "vitepress"

const { site, frontmatter, theme } = useData()
</script>

<template>
  <div v-if="frontmatter.home">
    <h1>{{ site.title }}</h1>
    <p>{{ site.description }}</p>
    <ul>
      <li v-for=" page, index in theme.pages" :key="index"><a :href="page.path">{{ page.name }}</a></li>
    </ul>
  </div>
  <div v-else>
    <a href="/">Home</a>
    <Content />
  </div>
</template>
