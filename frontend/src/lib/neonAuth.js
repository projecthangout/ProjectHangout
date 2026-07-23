import { createAuthClient } from "@neondatabase/auth";
import { SupabaseAuthAdapter } from "@neondatabase/auth/vanilla/adapters";

console.log(import.meta.env.VITE_NEON_AUTH_URL);

const auth = createAuthClient(import.meta.env.VITE_NEON_AUTH_URL, {
  adapter: SupabaseAuthAdapter(),
});

export default auth;