import {createRouter, createWebHistory} from "vue-router";
import GuestPage from "@/components/pages/GuestPage.vue";
import VocabularyPage from "@/components/pages/VocabularyPage.vue";
import ProfilePage from "@/components/pages/ProfilePage.vue";
import PageSettings from "@/components/pages/PageSettings.vue";
import PageGame from "@/components/pages/PageGame.vue";
import PageLogin from "@/components/pages/PageLogin.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'Guest page',
            component: GuestPage
        },
        {
            path:'/vocabulary',
            name: 'Vocabulary page',
            component: VocabularyPage
        },
        {
            path:'/profile',
            name: 'Profile page',
            component: ProfilePage
        },
        {
            path:'/settings',
            name: 'Settings page',
            component: PageSettings
        },
        {
            path:'/test',
            name: 'Game page',
            component: PageGame
        },
        {
            path:'/login',
            name: 'Login page',
            component: PageLogin
        }
    ]

})
export default router
