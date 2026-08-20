import { createRouter, createWebHistory } from "vue-router";

import LoginView from "@/views/LoginView.vue";
import DashboardView from "@/views/DashboardView.vue";
import DashboardAdminLayout from "@/layouts/DashboardAdminLayout.vue";
import DashboardAdminWrapper from "@/layouts/DashboardAdminWrapper.vue";

const router = createRouter({
    history: createWebHistory(),

    routes: [
        {
            path: "/",
            component: LoginView,
        },

        {
            path: "/dashboard",
            component: DashboardAdminWrapper,

            children: [
                {
                    path: "",
                    component: DashboardView,
                },
            ],
        },
    ],
});

export default router;