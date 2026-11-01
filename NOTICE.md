# Note su licenze, fonti dei dati e marchi

Questo file spiega da dove vengono i dati e a chi appartengono le cose mostrate dal sito.
Non è una consulenza legale: se vuoi usare il sito per qualcosa di più di una raccolta personale (per esempio a scopo commerciale), controlla le condizioni delle fonti qui sotto.

## Il codice di questo repository

Le pagine (`index.html`, `pokemon.html`, `magic.html`) e gli script nella cartella `tools/` sono distribuiti con licenza **MIT** (file `LICENSE`).
La licenza copre solo il codice scritto per questo progetto, non i dati né le immagini delle carte.

## Elenchi di carte (file `.json`)

I tre file `cards.json`, `pokemon.json` e `magic.json` sono estratti compatti, ricavati automaticamente da fonti pubbliche. Contengono nomi di carte, codici, espansioni e rarità. Non contengono immagini né testi delle carte.

| File | Fonte | Note |
|---|---|---|
| `cards.json` (Yu-Gi-Oh!) | [DawnbrandBots/yaml-yugi](https://github.com/DawnbrandBots/yaml-yugi) | Il progetto indica che la maggior parte dei testi delle carte è © Studio Dice/SHUEISHA, TV TOKYO, KONAMI e che il suo codice sorgente è sotto licenza AGPL-3.0 o successive. Qui si usano solo nomi, codici di stampa e rarità. |
| `pokemon.json` (Pokémon) | [PokemonTCG/pokemon-tcg-data](https://github.com/PokemonTCG/pokemon-tcg-data) | Nel repository non ho trovato un file di licenza. I dati si riferiscono a carte di Nintendo, Creatures e GAME FREAK. Il progetto è dichiarato obsoleto: l'API collegata è prevista offline dal 1 marzo 2027. |
| `magic.json` (Magic) | [Scryfall](https://scryfall.com/docs/api), file "Default Cards" | Usato come descritto nella loro documentazione per sviluppatori. Scryfall non è affiliato a questo progetto. |

## Immagini

Le immagini delle carte **non sono incluse** in questo repository. Il browser di chi visita il sito le richiede direttamente a:

- YGOPRODeck (`images.ygoprodeck.com`) per Yu-Gi-Oh!;
- pokemontcg.io (`images.pokemontcg.io`) per Pokémon;
- Scryfall (`cards.scryfall.io`) per Magic.

Le immagini restano di proprietà dei rispettivi titolari. Visitando il sito, il tuo browser contatta quei servizi, che possono quindi vedere il tuo indirizzo IP. Il sito funziona anche se le immagini non si caricano.

## Marchi e titolari

- *Yu-Gi-Oh!* è un marchio di Konami e di Studio Dice/SHUEISHA/TV TOKYO. Questo sito non è affiliato a Konami.
- *Pokémon* e i nomi delle sue carte appartengono a Nintendo, Creatures Inc. e GAME FREAK inc. Questo sito non è affiliato né approvato da loro.
- *Magic: The Gathering* appartiene a Wizards of the Coast LLC. Questo sito è un progetto non ufficiale, non approvato né sostenuto da Wizards of the Coast. Parte dei materiali usati è proprietà di Wizards of the Coast. ©Wizards of the Coast LLC.

Tutti gli altri nomi e marchi appartengono ai rispettivi proprietari.
