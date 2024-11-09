"""Game fix for Space Engineers"""

from protonfixes import util


def main() -> None:
    util.protontricks('xaudio29')
    check = util.protontricks('dotnet48')

    if(!check):
        try_show_gui_error("dotnet failed to install, the prefix is likely broken now.")

    base_attibutte = '<runtime>'
    game_opts = """
  	<gcServer enabled = "true" />
"""

    util.set_xml_options(base_attibutte, game_opts, 'SpaceEngineers.exe.config', 'game')

    util.append_argument('-skipintro')
