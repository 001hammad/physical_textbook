import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'An Introduction to Physical AI and Humanoid Robotics',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: false, // Disable blog for textbook
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Physical AI & Humanoid Robotics',
      logo: {
        alt: 'Physical AI & Humanoid Robotics Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Modules',
        },
        {
          href: 'https://github.com/facebook/docusaurus',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
    style: 'dark',
    links: [
      {
        title: 'Course',
        items: [
          { label: 'Home', to: '/' },
          { label: 'Modules', to: '/docs/module1' },
          { label: 'Capstone Project', to: '/docs/module4/capstone' },
        ],
      },
      {
        title: 'Resources',
        items: [
          { label: 'ROS 2 Docs', href: 'https://docs.ros.org/en/humble/index.html' },
          { label: 'NVIDIA Isaac Sim', href: 'https://developer.nvidia.com/isaac-sim' },
          { label: 'Gazebo Simulator', href: 'https://gazebosim.org/' },
        ],
      },
      {
        title: 'Community',
        items: [
          { label: 'GitHub', href: 'https://github.com/your-repo/physical-ai-book' },
          { label: 'Discord', href: 'https://discord.gg/your-server' },
          { label: 'Twitter/X', href: 'https://x.com/yourhandle' },
        ],
      },
    ],
    copyright: `
      <div class="footer-copyright">
        © ${new Date().getFullYear()} Physical AI & Humanoid Robotics. 
        Built with ❤️ using Docusaurus & Spec-Kit Plus.
      </div>
    `,
  },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
