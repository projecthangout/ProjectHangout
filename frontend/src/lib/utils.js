import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs) {
  return twMerge(clsx(inputs));
}

// Read from environment variables if available, otherwise default to local development URLs
export const API_BASE_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";
export const WS_BASE_URL = import.meta.env.VITE_WS_URL || "ws://localhost:8000";
