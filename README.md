# Odoo 16.0 Distribution

This is an all-in-one repository with all Odoo modules for development and 
distribution. It should make fast start easy and simple.

For linking/including the additional modules, git subtree is used. Therefore, it's easy to push back changes. 

# Dependencies

For the package management **pipenv** is used. Therefore, all dependencies (also for development) are tracked in the `Pipfile` and the resulting `Pipfile.lock`.

But some Python packages also have native dependencies, here the packagelist for Ubuntu 20.04:

    apt-get install apt-get install build-essential git virtualenv pipenv poppler-utils bzip2 curl fonts-freefont-ttf fonts-ubuntu fontconfig python3-dev libcairo2-dev libcups2-dev libffi-dev libfontconfig1-dev libfreetype6-dev libssl-dev libldap2-dev libxml2-dev libxslt1-dev libpq-dev libhttp-parser-dev libsasl2-dev libmagickwand-dev


# Development

## Commit Messages

Please use the commit message format described in the [OCA Guidlines](https://github.com/OCA/odoo-community.org/blob/master/website/Contribution/CONTRIBUTING.rst#commit-message) or described in the [Odoo Development Guidlines](https://www.odoo.com/documentation/16.0/developer/misc/other/guidelines.html)

## Commands

For simplifying the Odoo development/handling a smart/small extension was made to Odoo source.
The command line extension `odoo/odoo/cli/config.py` and the odoo start/entry point `odoo/odoo-bin`.

This extend the odoo for simple tasks like update and serve the odoo server or export/import and clean translations.

### Server Update

Following command updates the whole server:

    ./odoo-bin update -d <database>

But also a module update is possible:

    ./odoo-bin update -d <database> --module=<module>

### Server Run

To run the server simply execute:

    ./odoo-bin serve -d <database>

### Translation Export 

This command exports translation (default de_DE):

    ./odoo-bin po_export -d <database> --module=<module>


### Translation Import

And with this command you can import/update all translations

    ./odoo-bin po_import -d <database> --module=<module>

### Testing

Testing is important, therefore you can start individual module tests
with

    ./odoo-bin test -d <database> --module=<module> --test-prefix=<test>

### Further Help

    ./odoo-bin <cmd> --help


## VSCode

This repository already provide a workspace configuration with for vscode. 

### Start Developing

1. Checkout the source
2. Open VSCode workspace
3. Install OS (Ubuntu) packages
4. Setup python environment (open terminal create **.venv** and enter **pipenv install**)

#### .vscode/launch.json (example)

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Odoo: Server",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/odoo/odoo-bin",
            "console": "integratedTerminal",
            "args": ["serve",
             "--db-filter=odoo16_"
            ]
        },
        {
            "name": "Odoo: Test,
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/odoo/odoo-bin",
            "console": "integratedTerminal",
            "args": ["test",
                "-d=<database>",
                "--config=<odoo.conf>",
                "--module=<module>"
            ]
        }


    ]
}
```

