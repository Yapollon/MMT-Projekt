import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_und_speichere_messdaten(dateipfad, ausgabe_name="messdiagramm.png"):
    # Prüfen, ob die Quelldatei existiert
    if not os.path.exists(dateipfad):
        print(f"Fehler: Die Datei '{dateipfad}' wurde nicht gefunden.")
        return

    try:
        # 1. Daten einlesen
        # Trennung durch beliebig viele Leerzeichen, Komma als Dezimaltrenner
        df = pd.read_csv(dateipfad, sep=r'\s+', header=None, decimal=',', engine='python')
        df.columns = ['Zeit', 'Abstand', 'Spannung']

        # 2. Plot erstellen
        fig, ax1 = plt.subplots(figsize=(12, 7), dpi=150)

        # Abstand (Y1) - Blaue durchgehende Linie
        color_dist = 'tab:blue'
        ax1.set_xlabel('Zeit (s)', fontweight='bold')
        ax1.set_ylabel('Abstand (mm)', color=color_dist, fontweight='bold')
        ax1.plot(df['Zeit'], df['Abstand'], label='Messkurve Abstand', color=color_dist, linewidth=1.5, linestyle='-')
        ax1.tick_params(axis='y', labelcolor=color_dist)
        ax1.grid(True, linestyle='--', alpha=0.5)
        ax1.set_ylim(bottom=0)

        # Spannung (Y2) - Rote durchgehende Linie
        ax2 = ax1.twinx()
        color_volt = 'tab:red'
        ax2.set_ylabel('Spannung (V)', color=color_volt, fontweight='bold')
        ax2.plot(df['Zeit'], df['Spannung'], label='Messkurve Spannung', color=color_volt, linewidth=1.5, linestyle='-')
        ax2.tick_params(axis='y', labelcolor=color_volt)
        ax2.set_ylim(bottom=0)

        # Titel & Legenden (Position unten links)
        plt.title('Abstands- und Spannungs-Verlauf', pad=20, fontsize=14)
        
        # Legenden zusammenführen und unten links platzieren
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='lower left', shadow=True, fontsize='small')

        fig.tight_layout()
        
        # 3. Speichern und Anzeigen
        plt.savefig(ausgabe_name, bbox_inches='tight')
        print(f"Erfolg: Das Diagramm wurde als '{ausgabe_name}' gespeichert.")
        plt.show()

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    # Pfad zu deiner Datei (muss im selben Ordner liegen)
    input_file = 'Beispieldaten.txt' 
    output_image = 'Darstellung.png'
    
    plot_und_speichere_messdaten(input_file, output_image)