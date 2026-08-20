import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {

    state: () => ({
        token: null,
        admin: null,
    }),

    actions: {

        setToken(token) {
            this.token = token;
        },

        setAdmin(admin) {
            this.admin = admin;
        },

        logout() {
            this.token = null;
            this.admin = null;
        }

    }

});