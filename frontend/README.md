# Project Hangout - Frontend

This is the frontend application for Project Hangout, built with React and Vite. It provides an immersive, modern user interface utilizing 3D elements and smooth animations.

## 🚀 Tech Stack

- **Framework**: [React 19](https://react.dev/) + [Vite](https://vitejs.dev/)
- **Routing**: [React Router](https://reactrouter.com/)
- **Styling**: [Tailwind CSS v4](https://tailwindcss.com/)
- **UI Components**: [Radix UI](https://www.radix-ui.com/)
- **Animations**: [Framer Motion](https://www.framer.com/motion/)
- **3D Graphics**: [Three.js](https://threejs.org/) & [React Three Fiber](https://docs.pmnd.rs/react-three-fiber/)
- **HTTP Client**: [Axios](https://axios-http.com/)

## 📦 Getting Started

### Prerequisites

Make sure you have Node.js installed (v18+ recommended).

### Installation

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install the dependencies:
   ```bash
   npm install
   ```

### Environment Variables

Create a `.env` file in the root of the `frontend` directory. Make sure to define any required environment variables (e.g., API keys, backend endpoints) before starting the development server.

### Available Scripts

- `npm run dev` - Starts the development server with Hot Module Replacement (HMR).
- `npm run build` - Builds the application for production.
- `npm run preview` - Locally previews the production build.
- `npm run lint` - Runs ESLint to check for code issues.

## 🧪 Testing

This project is configured with [Playwright](https://playwright.dev/) for end-to-end testing.

## 🤝 Contributing

When contributing to this frontend:
- Ensure you run `npm run lint` before committing your changes.
- Follow the existing project structure and styling conventions.
