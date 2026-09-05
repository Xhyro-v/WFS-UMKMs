import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
    state: () => ({
        token: localStorage.getItem("token") || null,
        admin: null,
    }),

    actions: {
        setToken(token) {
            this.token = token;
            localStorage.setItem("token", token);
        },

        setAdmin(admin) {
            this.admin = admin;
        },

        logout() {
            this.token = null;
            this.admin = null;
            localStorage.removeItem("token");
        }
    }
});