import sys, os

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('../src'))

extensions = [
        'sphinxcontrib.luadomain',
        'sphinx_lua'
        ]

lua_source_path = ["../src/"]
