<script setup lang="ts">
import { useData, Content } from "vitepress"

const { site, frontmatter } = useData()
</script>

<template>
  <div v-if="frontmatter.home">
    <h1>{{ site.title }}</h1>
    <p>{{ site.description }}</p>
    <ul>
      <li><a href="/gradle/index.html">gradle</a></li>
      <li><a href="/java/gradle.html">java.gradle</a></li>
      <li><a href="/java/index.html">java</a></li>
    </ul>
  </div>
  <div v-else>
    <a href="/">Home</a>
    <Content />
  </div>
</template>
