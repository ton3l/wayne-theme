## Uso

### Instalação
````bash
    bun i

    mkdir dist;bunx vsce package -o dist/ 

    code --install-extension .\dist\wayne-theme-1.13.1.vsix
````
Após isso o tema aparecerá listado nos temas do vscode

### Atualização
````bash
    code --uninstall-extension ton3l.wayne-theme

    bunx vsce package -o dist/ 

    code --install-extension .\dist\wayne-theme-1.13.1.vsix
````