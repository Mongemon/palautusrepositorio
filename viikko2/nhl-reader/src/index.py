from player import Player, PlayerReader, PlayerStats
from rich import print
import requests
from rich.console import Console
from rich.table import Table

def main():
    console = Console()

    console.print("[bold cyan]NHL-pelaajatilastot[/bold cyan]")
    console.print()

    season = input("Anna kausi (esim. 2024-25): ")
    nationality = input("Anna maan tunnus (esim. FIN): ").upper()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    players = reader.get_players()
    stats = PlayerStats(players)
    top_players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"NHL-pelaajat: {nationality}, kausi {season}")
    table.add_column("Pelaaja", style="cyan")
    table.add_column("Maa", justify="center")
    table.add_column("Joukkue", style="green")
    table.add_column("Maalit", justify="right")
    table.add_column("Syötöt", justify="right")
    table.add_column("Pisteet", justify="right", style="bold yellow")


    for player in top_players:
        points = player.goals + player.assists

        table.add_row(
            player.name, player.nationality, player.team, 
            str(player.goals), str(player.assists), str(points)
            )

    if top_players:
        console.print(table)
    else:
        console.print(f"[red]Pelaajia ei löytynyt maalle {nationality}!!![/red]")



if __name__ == "__main__":
    main()
