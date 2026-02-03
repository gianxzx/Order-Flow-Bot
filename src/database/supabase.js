import { createClient } from "@supabase/supabase-js";
import { ENV } from "../config/env.js";

// Initialize Supabase client using env variables
export const supabase = createClient(
  ENV.SUPABASE_URL,
  ENV.SUPABASE_ANON_KEY
);
