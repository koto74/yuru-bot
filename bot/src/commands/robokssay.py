from discord import app_commands, Interaction


@app_commands.command(
    name="robokssay",
    description="「踏めば助かるのに...」でおなじみのロボカスに何でも言わせることが出来ます。",
)
@app_commands.describe(message="The message to display")
async def robokssay(interaction: Interaction, message: str):
    roboks_art = (
        "    \\\n"
        "     \\          >/一<\\\n"
        "      \\         /ヽ_ノヽ\n"
        "       \\           ﾊ\n"
        "        \\       ———————\n"
        "         \\.  ／         ＼\n"
        "           ／   ●     ●   ＼\n"
        "          /     ❘ニニニ❘     \\\n"
        "        ／|—————-———————————|ヽ\n"
        "       / /|     〇 〇 〇     |ヽヽ\n"
        "     (一) |                 | (一)\n"
        "          |      ／一＼      |\n"
        "          |      | ? |      |\n"
        "          |      ＼一／      |\n"
        "          |＿   ＿＿＿＿   ＿.|\n"
        "              Π         Π   \n"
        "          (ニニ|         |ニニ))\n"
    )
    bar = "-" * len(message) * 2
    comment = f"{bar}\n" f"＜ {message} ＞\n" f"{bar}\n"

    await interaction.response.send_message(f"```\n{comment}\n{roboks_art}```")
