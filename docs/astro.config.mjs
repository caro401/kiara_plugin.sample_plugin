import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import { readdirSync } from "fs";
import svelte from "@astrojs/svelte";
import semverSort from "semver-sort";

function getOperations() {
  const versions = readdirSync(`src/content/plugin_data/`);
  const versionNumbers = semverSort.desc(
    versions.map((v) => v.match(/v\d+\.\d+\.\d+/g)[0]),
  );
  return [
    ...versionNumbers.map((v) => ({
      label: v,
      collapsed: true,
      items: [
        {
          label: `How to develop the plugin`,
          link: `/${v}`,
        },
        {
          label: "Operations",
          link: `/${v}/operations`,
        },
        { label: "Modules", link: `/${v}/modules` },
        { label: "Data types", link: `/${v}/datatypes` },
        { label: "Model types", link: `/${v}/modeltypes` },
        {
          label: "Operation types",
          link: `/${v}/operationtypes`,
        },
      ],
    })),
  ];
}
// https://astro.build/config
export default defineConfig({
  integrations: [
    starlight({
      title: "kiara #PLUGIN_NAME",
      editLink: {
        baseUrl: "https://github.com/#GITHUB_USER/#PLUGIN_NAME/edit/main/",
      },
      customCss: ["./src/styles/custom.css"],
      social: {
        github: "https://github.com/#GITHUB_USER/#PLUGIN_NAME",
      },
      sidebar: [
        { label: "Overview", items: [{ label: "Overview", link: "/" }] },
        { label: "Guides", autogenerate: { directory: "guides" } },
        {
          label: "#PLUGIN_NAME contents",
          items: getOperations(),
        },
      ],
    }),
    svelte(),
  ],
});
