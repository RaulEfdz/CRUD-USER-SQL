import daisyui from 'daisyui';

export default {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [daisyui],
  daisyui: {
    themes: ["light", "dark"], // Puedes agregar más temas de DaisyUI aquí
  },
};
