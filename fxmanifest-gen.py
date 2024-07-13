## Imports ##

import os

## Strings ##

credits = 'ImAidanJ'
version = '1.3'

def generate_template():
    try:
        folder_path = input("Enter the file path where the script will be stored: ").strip().strip('"')

        name = input("Enter the script name (default: default_script): ").strip() or 'default_script'
        author = input("Enter the author name (default: ImAidanJ): ").strip() or 'ImAidanJ'
        fx_version = input("Enter the FxVersion (default: cerulean): ").strip() or 'cerulean'
        description = input("Enter the script description (default: FiveM Script Template by ImAidanJ): ").strip() or 'FiveM Script Template by ImAidanJ'
        script_version = input("Enter the script version (default: 1.0.0): ").strip() or '1.0.0'

        fxmanifest_content = f'''
fx_version '{fx_version}'
game 'gta5'

name '{name}'
description '{description}'
author '{author}'
version '{script_version}'

client_scripts {{
    'config.lua',
    'client/*.lua'
}}

server_scripts {{
    'config.lua',
    'server/*.lua'
}}

-- FxManifest by {credits} --
-- FxManifest Generator v{version} --
'''

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(os.path.join(folder_path, 'fxmanifest.lua'), 'w') as f:
            f.write(fxmanifest_content)

        print(f"fxmanifest.lua has been generated successfully in {folder_path}")

    except Exception as e:
        print(f'ERROR: {e}')

if __name__ == "__main__":
    generate_template()