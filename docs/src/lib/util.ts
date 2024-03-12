import { getCollection, getDataEntryById } from "astro:content";

/**
 * Generate static paths for all items of a specific datatype for all plugins and versions. See https://docs.astro.build/en/guides/routing/#static-ssg-mode  for the format
 *
 * @param kiaraType - the type of data in Kiara for which static paths are generated (`module_type`, `kiara_model_type` etc)
 * @param pathName - the name of the path parameter where this static path is generated (the bit in square brackets in the file name)
 * @return  an array of objects representing the generated static paths
 */
export async function getStaticPathsForDatatype(
  kiaraType: string,
  pathName: string,
) {
  return (await getCollection("plugin_data")).flatMap((plugin) => {
    const [_, version] = plugin.id.split("-");
    const typeIds = Object.keys(plugin.data[kiaraType].item_infos);
    return typeIds.map((t) => ({
      params: { version: version, [pathName]: t },
    }));
  });
}

export async function getStaticPathsForPluginVersions() {
  return (await getCollection("plugin_data")).map((plugin) => {
    const [_, version] = plugin.id.split("-");
    return { params: { version: version } };
  });
}

export async function getSpecificKiaraType(
  version: string,
  kiaraType: string,
): Promise<Record<string, any>> {
  return (
    await getDataEntryById(
      "plugin_data",
      // TODO replace this with plugin name from cookiecutter
      // @ts-expect-error the build will fail if this string is not one of the files in the `plugins` content collection
      `kiara_plugin.sample_plugin-${version}`,
    )
  ).data[kiaraType].item_infos;
}

export async function getSpecificKiaraTypeInstance(
  version: string,
  kiaraType: string,
  thingId: string,
) {
  return (await getSpecificKiaraType(version, kiaraType))[thingId];
}
