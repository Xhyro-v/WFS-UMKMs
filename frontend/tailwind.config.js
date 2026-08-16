/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        canvas: '#FAFAF9',
        surface: '#FFFFFF',
        border: '#E7E5E4',

        primary: {
          50: '#F0FDFA',
          100: '#CCFBF1',
          200: '#99F6E4',
          300: '#5EEAD4',
          400: '#2DD4BF',
          500: '#14B8A6',
          600: '#0F766E',
          700: '#115E59',
          800: '#134E4A',
          900: '#042F2E',
        },

        txt: {
          primary: '#1C1917',
          secondary: '#78716C',
        },

        success: '#059669',
        warning: '#F59E0B',
        danger: '#DC2626',
      },

      borderRadius: {
        card: '1rem',
        button: '0.75rem',
      },

      boxShadow: {
        card: '0 8px 24px rgba(0, 0, 0, 0.08)',
      },

      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },

      spacing: {
        page: '2rem',
        section: '1.5rem',
      },
    },
  },
  plugins: [],
}
