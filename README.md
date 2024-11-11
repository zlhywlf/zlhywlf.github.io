# jupiter

## processes

### editorconfig

- [editorconfig](https://editorconfig.org/)

#### `.editorconfig`

- [editorconfig-properties](https://github.com/editorconfig/editorconfig/wiki/EditorConfig-Properties)

### pnpm

- [pnpm](https://pnpm.io/)

#### `package.json`

- [only-allow-pnpm](https://pnpm.io/only-allow-pnpm)
- [package-json](https://docs.npmjs.com/cli/v7/configuring-npm/package-json)
- [pnpm-package_json](https://pnpm.io/package_json)

```shell
# Create a package.json file.
pnpm init
```

#### `.npmrc`

- [pnpm-npmrc](https://pnpm.io/npmrc)

#### `pnpm-workspace.yaml`

- [pnpm-workspace_yaml](https://pnpm.io/pnpm-workspace_yaml)
- [catalogs](https://pnpm.io/catalogs)

```shell
# root 工作区添加依赖
pnpm add -w
# 子工作区添加依赖
pnpm add -F @jupiter/admin
# 添加工作区中的依赖
pnpm add --workspace
```
