<template>
    <BlogHeader/>
    <ArticleList/>
    <BlogFooter/>
</template>

<script>
import BlogHeader from "@/components/BlogHeader";
import ArticleList from "@/components/ArticleList";
import BlogFooter from "@/components/BlogFooter";

export default {
    name: 'Home',
    components: {BlogHeader, ArticleList, BlogFooter},
}
</script>

<style>
#app {
    font-family: Georgia, Arial, sans-serif;
    margin-left: 40px;
    margin-right: 40px;
}
</style>
