import {createWebHistory, createRouter} from "vue-router";
import Home from "@/views/Home";
import ArticleDetail from "@/views/ArticleDetail";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/article/:id",
        name: "ArticleDetail",
        component: ArticleDetail
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;