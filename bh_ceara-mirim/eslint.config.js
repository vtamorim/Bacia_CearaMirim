import js from '@eslint/js';
import vue from 'eslint-plugin-vue';
import prettier from '@vue/eslint-config-prettier';

export default [
  js.configs.recommended,
  ...vue.configs['flat/essential'],
  prettier,
  {
    ignores: ['node_modules/', 'dist/', 'public/', '*.config.js'],
  },
  {
    rules: {
      'vue/multi-word-component-names': 'off',
      'no-unused-vars': 'warn',
      'vue/no-unused-vars': 'warn',
    },
  },
];