# [**kiara**](https://dharpa.org/kiara.documentation) plugin: sample-plugin

This package contains a set of commonly used/useful modules, pipelines, types and metadata schemas for [*Kiara*](https://github.com/DHARPA-project/kiara).

## Description

sample-plugin

## Package content

{% for item_type, item_group in get_context_info().get_all_info().items() %}

### {{ item_type }}
{% for item, details in item_group.item_infos.items() %}
- [`{{ item }}`][kiara_info.{{ item_type }}.{{ item }}]: {{ details.documentation.description }}
{% endfor %}
{% endfor %}

## Links

 - Documentation: [https://caro401.github.io/kiara_plugin.sample_plugin](https://caro401.github.io/kiara_plugin.sample_plugin)
 - Code: [https://github.com/caro401/kiara_plugin.sample_plugin](https://github.com/caro401/kiara_plugin.sample_plugin)
