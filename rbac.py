# Time  ：2022-3-25 10:39
# Author：Houtaroy
import argparse
from translate import Translator

# sql模板
permission_parent_template = 'insert into t_permission values ("%s", null, "%s", 1, "%s", "%s管理", null, null, null, null, null, null, null, %d, 1, 0, now(), "@SYSTEM", null, null, null, null, null, null, null);\n'

api_templates = [
    'insert into t_api values ("api:%s:search", null, "%s", "api:%s:search", "根据条件查询%s", "/api/%s", "GET", 0, "根据条件查询%s", %d, 1, 0, now(), "@SYSTEM", null, null, null, null, null, null, null);\n',
    'insert into t_api values ("api:%s:loadById", null, "%s", "api:%s:loadById", "根据id查询%s", "/api/%s/{id}", "GET", 0, "根据id查询%s", %d, 1, 0, now(), "@SYSTEM", null, null, null, null, null, null, null);\n',
    'insert into t_api values ("api:%s:create", null, "%s", "api:%s:create", "创建%s", "/api/%s", "POST", 0, "创建%s", %d, 1, 0, now(), "@SYSTEM", null, null, null, null, null, null, null);\n',
    'insert into t_api values ("api:%s:updateAll", null, "%s", "api:%s:updateAll", "根据id更新%s全部信息", "/api/%s/{id}", "PUT", 0, "根据id更新%s全部信息", %d, 1, 0, now(), "@SYSTEM", null, null, null, null, null, null, null);\n',
    'insert into t_api values ("api:%s:deleteById", null, "%s", "api:%s:deleteById", "根据id删除%s", "/api/%s/{id}", "DELETE", 0, "根据id删除%s", %d, 1, 0, now(), "@SYSTEM", null, null, null, null, null, null, null);\n'
]

permission_templates = [
    'insert into t_permission values ("%s:search", "%s", "%s", 2, "%s:search", "查询%s", null, null, null, null, null, null, null, %d, 1, 0, now(), "@SYSTEM", null, null, null, null, null, null, null);\n',
    'insert into t_permission values ("%s:view", "%s", "%s", 2, "%s:view", "查看%s", null, null, null, null, null, null, null, %d, 1, 0, now(), "@SYSTEM", null, null, null, null, null, null, null);\n',
    'insert into t_permission values ("%s:create", "%s", "%s", 2, "%s:create", "添加%s", null, null, null, null, null, null, null, %d, 1, 0, now(), "@SYSTEM", null, null, null, null, null, null, null);\n',
    'insert into t_permission values ("%s:update", "%s", "%s", 2, "%s:update", "更新%s", null, null, null, null, null, null, null, %d, 1, 0, now(), "@SYSTEM", null, null, null, null, null, null, null);\n',
    'insert into t_permission values ("%s:delete", "%s", "%s", 2, "%s:delete", "删除%s", null, null, null, null, null, null, null, %d, 1, 0, now(), "@SYSTEM", null, null, null, null, null, null, null);\n'
]

relation_templates = [
    'insert into t_permission_api values ("%s:search", "api:%s:search");\n',
    'insert into t_permission_api values ("%s:view", "api:%s:loadById");\n',
    'insert into t_permission_api values ("%s:create", "api:%s:create");\n',
    'insert into t_permission_api values ("%s:update", "api:%s:updateAll");\n',
    'insert into t_permission_api values ("%s:delete", "api:%s:deleteById");\n'
]


# 驼峰转换为kebab-case
def kebab_case(text):
    result = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            result.append('-')
        result.append(char)
    return "".join(result).lower()


# 提取驼峰单词
def words(text):
    result = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            result.append(' ')
        result.append(char)
    return "".join(result).lower()


if __name__ == '__main__':
    # 读取命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--resource-id', type=str)
    parser.add_argument('--apis', type=str, nargs='+')
    parser.add_argument('--start-index', type=int)
    args = parser.parse_args()
    module_index = int(args.start_index if args.start_index else 101)
    translator = Translator(to_lang="zh")
    api_f = open("t_api.sql", "a", encoding='utf-8')
    permission_f = open("t_permission.sql", "a", encoding='utf-8')
    relation_f = open("t_permission_api.sql", "a", encoding='utf-8')
    for module in args.apis:
        name = translator.translate(words(module))
        permission_f.write(permission_parent_template % (module, args.resource_id, module, name, module_index))
        sort_index = module_index * 100 + 1
        for i in range(len(api_templates)):
            api_f.write(
                api_templates[i] % (module, args.resource_id, module, name, kebab_case(module), name, sort_index))
            permission_f.write(permission_templates[i] % (module, module, args.resource_id, module, name, sort_index))
            relation_f.write(relation_templates[i] % (module, module))
            sort_index += 1
        module_index += 1
    api_f.close()
    permission_f.close()
