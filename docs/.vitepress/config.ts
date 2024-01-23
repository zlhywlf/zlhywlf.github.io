import {defineConfig} from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
    title: "note",
    description: "a note site",
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        nav: [
            {text: 'Home', link: '/'},
        ],

        sidebar: [
            {
                text: 'java',
                items: [
                    {text: '简介', link: '/java/'},
                    {text: 'gradle', link: '/java/gradle'}
                ]
            }
        ],

        socialLinks: [
            {icon: 'github', link: 'https://github.com/zlhywlf/zlhywlf.github.io'}
        ]
    }
})
