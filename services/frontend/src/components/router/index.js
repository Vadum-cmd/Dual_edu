import { createRouter, createWebHistory } from "vue-router";
import VocabularyPage from "@/components/pages/VocabularyPage.vue";
import ProfilePage from "@/components/pages/ProfilePage.vue";
import PageSettings from "@/components/pages/PageSettings.vue";
import PageGame from "@/components/pages/PageGame.vue";
import PageLogin from "@/components/pages/PageLogin.vue";
import PageGuest from "@/components/pages/PageGuest.vue";
import HomePage from "@/components/pages/HomePage.vue";
import BooksPage from "@/components/pages/BooksPage.vue";
import ResetPassword from "@/components/pages/ResetPassword.vue";
import Verification from "@/components/pages/Verification.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            name: "Guest page",
            component: PageGuest,
        },
        {
            path: "/home",
            name: "Home page",
            component: HomePage,
            meta: {
                requiresAuth: true, // this route requires authentication
            },
        },
        {
            path: "/vocabulary",
            name: "Vocabulary page",
            component: VocabularyPage,
            meta: {
                requiresAuth: true, // this route requires authentication
            },
        },
        {
            path: "/profile",
            name: "Profile page",
            component: ProfilePage,
            meta: {
                requiresAuth: true, // this route requires authentication
            },
        },
        {
            path: "/settings",
            name: "Settings page",
            component: PageSettings,
            meta: {
                requiresAuth: true, // this route requires authentication
            },
        },
        {
            path: "/test",
            name: "Game page",
            component: PageGame,
            meta: {
                requiresAuth: true, // this route requires authentication
            },
        },
        {
            path: "/login",
            name: "Login page",
            component: PageLogin,
        },
        {
            path: "/books",
            name: "Books page",
            component: BooksPage,
            meta: {
                requiresAuth: true, // this route requires authentication
            },
        },
        {
            path: "/resetpassword",
            name: "Reset password",
            component: ResetPassword,
        },
        {
            path: "/verification",
            name: "Verification",
            component: Verification,
        },
    ],
});

// Navigation guard
router.beforeEach((to, from, next) => {
    const jwt = localStorage.getItem("jwt");
    if (to.meta.requiresAuth && !jwt) {
        // User is not authenticated and route requires authentication
        next("/login");
    } else {
        next();
    }
});

export default router;